import json
import os
import pygame, sys
from config import *

def cargar_puntuaciones(path=RANKING_PATH):
    """
    Lee el archivo JSON y devuelve siempre el top-5 ordenado.
    Si no existe, está vacío o no contiene JSON válido, devuelve [].
    """
    # Si no existe o está completamente vacío
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            lista = json.load(f)
    except json.JSONDecodeError:
        # El archivo existe pero no tiene JSON válido
        return []

    # Ordenamos de mayor a menor y truncamos a 5
    lista.sort(key=lambda x: x["puntaje"], reverse=True)
    return lista[:5]

def guardar_puntuaciones(puntuaciones, path=RANKING_PATH):
    """
    Escribe la lista de dicts 'puntuaciones' en el archivo JSON.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(puntuaciones, f, ensure_ascii=False, indent=2)


def agregar_puntuacion(nombre: str, puntaje: int, path=RANKING_PATH) -> bool:
    """
    Si hay menos de 5 puntajes o el nuevo es >= mínimo del top-5,
    lo inserta, reordena, graba y devuelve True. Si no, no graba
    y devuelve False.
    """
    scores = cargar_puntuaciones(path)
    if len(scores) < 5 or puntaje >= scores[-1]["puntaje"]:
        scores.append({"nombre": nombre, "puntaje": puntaje})
        scores.sort(key=lambda x: x["puntaje"], reverse=True)
        scores = scores[:5]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(scores, f, indent=2, ensure_ascii=False)
        return True
    return False


def obtener_mejores_puntuaciones(puntuaciones, top_n=5):
    """
    Recibe la lista 'puntuaciones' y devuelve las primeras top_n
    ordenadas por 'puntaje' de mayor a menor.
    """
    # Ordenamos en sitio (no modifica el original si hacemos copia)
    puntuaciones_ordenadas = sorted(puntuaciones, key=lambda x: x["puntaje"], reverse=True)
    return puntuaciones_ordenadas[:top_n]


def mostrar_ranking(screen, path=RANKING_PATH):
    """
    Dibuja el top-5 en pantalla:
    - screen: Surface de Pygame donde dibujar.
    - path: ruta al JSON de ranking.
    Espera a que el jugador presione ESC o cierre la ventana
    para volver al flujo principal.
    """
    # 4.1) Carga y prepara datos
    puntuaciones = cargar_puntuaciones(path)
    top5 = obtener_mejores_puntuaciones(puntuaciones, top_n=5)

    # 4.2) Bucle de pantalla
    clock = pygame.time.Clock()
    running = True

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                # Salir de la pantalla de ranking
                running = False

        # 4.3) Dibujado fondo
        screen.fill(GRIS)

        # 4.4) Título
        titulo_surf = FUENTE_MEDIANA.render("Top 5 Gaucho Defense", True, BLANCO)
        titulo_rect = titulo_surf.get_rect(center=(ANCHO//2, 60))
        screen.blit(titulo_surf, titulo_rect)

        # 4.5) Dibujar cada score
        # Acá se maneja el espaciado y alineación
        base_y = 150
        espacio = 60
        for idx, entry in enumerate(top5):
            text = f"{idx+1}. {entry['nombre']} — {entry['puntaje']}"
            surf = FUENTE_MEDIANA.render(text, True, BLANCO)
            rect = surf.get_rect(center=(ANCHO//2, base_y + idx * espacio))
            screen.blit(surf, rect)

        info = "Presiona ESC para volver"
        info_surf = FUENTE_MEDIANA.render(info, True, BLANCO)
        info_rect = info_surf.get_rect(center=(ANCHO//2, ALTO - 40))
        screen.blit(info_surf, info_rect)

        pygame.display.flip()
        clock.tick(60)

