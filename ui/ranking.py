import json
import os
import pygame
import sys
from config import (
    ANCHO, ALTO, BLANCO, NEGRO,
    RANKING_PATH, FUENTE_MEDIANA
)


def get_puntaje(entry: dict) -> int:
    """
    Extrae el valor "puntaje" de una diccionario de ranking.
    """
    return entry["puntaje"]


def cargar_puntuaciones(path=RANKING_PATH) -> list:
    """
    Abre el archivo JSON de ranking en 'path', lo lee, convierte a dict Python
    y retorna el top-5 ordenado.
    Si el archivo no existe o está vacío, devuelve [].
    """
    if not os.path.exists(path):
        return []

    tamaño = os.path.getsize(path)
    if tamaño == 0:
        return []

    with open(path, "r", encoding="utf-8") as f:
        datos = json.load(f)

    return obtener_mejores_puntuaciones(datos, top_n=5)


def guardar_puntuaciones(puntuaciones: list, path=RANKING_PATH) -> None:
    """
    Escribe la lista 'puntuaciones' en formato JSON en 'path'.
    Chequea que el directorio exista, si es asi no hace nada.
    Si no existe, lo crea.
    """
    carpeta = os.path.dirname(path)
    if carpeta != "":
        os.makedirs(carpeta, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(puntuaciones, f, ensure_ascii=False, indent=2)


def obtener_mejores_puntuaciones(puntuaciones: list, top_n=5) -> list:
    """
    Ordena la lista 'puntuaciones' de mayor a menor, y devuelve las primeras 'top_n'.
    """
    if puntuaciones is None:
        return []

    copia = []
    for entrada in puntuaciones:
        copia.append(entrada)

    ordenada = sorted(copia, key=get_puntaje, reverse=True)

    resultado = []
    contador = 0
    for entrada in ordenada:
        if contador < top_n:
            resultado.append(entrada)
            contador += 1
        else:
            break

    return resultado


def agregar_puntuacion(nombre: str, puntaje: int, path=RANKING_PATH) -> bool:
    """
    Inserta un nuevo puntaje si hay < 5 o es >= al mínimo del top-5.
    Retorna True si se guardó, False en caso contrario.
    """
    scores = cargar_puntuaciones(path)

    debe_insertar = False
    if len(scores) < 5:
        debe_insertar = True
    else:
        minimo = scores[-1]
        if puntaje >= minimo["puntaje"]:
            debe_insertar = True

    if debe_insertar:
        nueva_entrada = {"nombre": nombre, "puntaje": puntaje}
        scores.append(nueva_entrada)
        top5 = obtener_mejores_puntuaciones(scores, top_n=5)
        guardar_puntuaciones(top5, path)
        return True

    return False


def mostrar_ranking(screen: pygame.Surface, path=RANKING_PATH) -> None:
    """
    Carga, muestra y da formato en pantalla el top-5 de puntuaciones.
    Espera ESC o cierre de ventana para volver.
    """
    puntuaciones = cargar_puntuaciones(path)
    top5 = obtener_mejores_puntuaciones(puntuaciones, top_n=5)

    clock = pygame.time.Clock()
    en_ranking = True

    while en_ranking:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    en_ranking = False

        screen.fill(NEGRO)

        titulo_surf = FUENTE_MEDIANA.render("Top 5 Gaucho Defense", True, BLANCO)
        titulo_rect = titulo_surf.get_rect(center=(ANCHO // 2, 60))
        screen.blit(titulo_surf, titulo_rect)

        base_y = 150
        espacio = 60
        y_actual = base_y
        for i in range(len(top5)):
            entrada = top5[i]
            texto = str(i+1) + ". " + entrada["nombre"] + " — " + str(entrada["puntaje"])
            surf = FUENTE_MEDIANA.render(texto, True, BLANCO)
            rect = surf.get_rect(center=(ANCHO // 2, y_actual))
            screen.blit(surf, rect)
            y_actual += espacio

        info_surf = FUENTE_MEDIANA.render("Presiona ESC para volver", True, BLANCO)
        info_rect = info_surf.get_rect(center=(ANCHO // 2, ALTO - 40))
        screen.blit(info_surf, info_rect)

        pygame.display.flip()
        clock.tick(60)
