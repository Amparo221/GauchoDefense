# src/ranking.py

import json
import os
import pygame
from config import ANCHO, ALTO, fuente_mediana, BLANCO, GRIS


def load_scores(path="datos/ranking.json"):
    """
    Lee el archivo JSON y devuelve una lista de dicts:
    [
      {"nombre": "Pepe", "puntaje": 1200},
      {"nombre": "Ana",  "puntaje":  900},
      ...
    ]
    Si no existe el archivo, devuelve lista vacía.
    """
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # En caso de archivo corrupto, lo sobrescribimos después
            return []

def save_scores(scores, path="datos/ranking.json"):
    """
    Escribe la lista de dicts 'scores' en el archivo JSON.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)


def add_score(nombre, puntaje, path="ranking.json"):
    """
    Carga los scores existentes, añade el nuevo, guarda de nuevo.
    """
    scores = load_scores(path)
    # Añadimos al final
    scores.append({"nombre": nombre, "puntaje": puntaje})
    save_scores(scores, path)


def get_top_scores(scores, top_n=5):
    """
    Recibe la lista 'scores' y devuelve las primeras top_n
    ordenadas por 'puntaje' de mayor a menor.
    """
    # Ordenamos en sitio (no modifica el original si hacemos copia)
    sorted_scores = sorted(scores, key=lambda x: x["puntaje"], reverse=True)
    return sorted_scores[:top_n]


def show_ranking(screen, path="ranking.json"):
    """
    Dibuja el top-5 en pantalla:
    - screen: Surface de Pygame donde dibujar.
    - path: ruta al JSON de ranking.
    Espera a que el jugador presione ESC o cierre la ventana
    para volver al flujo principal.
    """
    # 4.1) Carga y prepara datos
    scores = load_scores(path)
    top5 = get_top_scores(scores, top_n=5)

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
        titulo_surf = fuente_mediana.render("Top 5 Gaucho Defense", True, BLANCO)
        titulo_rect = titulo_surf.get_rect(center=(ANCHO//2, 60))
        screen.blit(titulo_surf, titulo_rect)

        # 4.5) Dibujar cada score
        # Acá se maneja el espaciado y alineación
        base_y = 150
        espacio = 60
        for idx, entry in enumerate(top5):
            text = f"{idx+1}. {entry['nombre']} — {entry['puntaje']}"
            surf = fuente_mediana.render(text, True, BLANCO)
            rect = surf.get_rect(center=(ANCHO//2, base_y + idx * espacio))
            screen.blit(surf, rect)

        info = "Presiona ESC para volver"
        info_surf = fuente_mediana.render(info, True, BLANCO)
        info_rect = info_surf.get_rect(center=(ANCHO//2, ALTO - 40))
        screen.blit(info_surf, info_rect)

        pygame.display.flip()
        clock.tick(60)
