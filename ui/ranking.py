import json
import os
import pygame
import sys
import config


def get_puntaje(entry: dict) -> int:
    """
    Extrae el valor "puntaje" de una diccionario de ranking.

    Args:
        entry: dict

    Returns:
        int (puntaje)
    """
    return entry["puntaje"]


def cargar_puntuaciones() -> list:
    """
    Abre el archivo JSON de ranking en 'path', lo lee, convierte a dict Python
    y retorna el top-5 ordenado.
    Si el archivo no existe o está vacío, devuelve [].

    Args:
        path: str

    Returns:
        list (mejores 5 puntuaciones)
    """
    if not os.path.exists(config.RANKING_PATH):
        return []

    tamaño = os.path.getsize(config.RANKING_PATH)
    if tamaño == 0:
        return []

    with open(config.RANKING_PATH, "r", encoding="utf-8") as f:
        datos = json.load(f)

    return obtener_mejores_puntuaciones(datos, top_n=5)


def guardar_puntuaciones(puntuaciones: list) -> None:
    """
    Escribe la lista 'puntuaciones' en formato JSON en 'path'.
    Chequea que el directorio exista, si es asi no hace nada.
    Si no existe, lo crea.

    Args:
        puntuaciones: list
        path: str
    """
    carpeta = os.path.dirname(config.RANKING_PATH)
    if carpeta != "":
        os.makedirs(carpeta, exist_ok=True)

    with open(config.RANKING_PATH, "w", encoding="utf-8") as f:
        json.dump(puntuaciones, f, ensure_ascii=False, indent=2)


def obtener_mejores_puntuaciones(puntuaciones: list, top_n: int = 5) -> list:
    """
    Ordena la lista 'puntuaciones' de mayor a menor, y devuelve las primeras 'top_n'.

    Args:
        puntuaciones: list
        top_n: int

    Returns:
        list
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


def agregar_puntuacion(nombre: str, puntaje: int) -> bool:
    """
    Inserta un nuevo puntaje si hay < 5 o es >= al mínimo del top-5.
    Retorna True si se guardó, False en caso contrario.

    Args:
        nombre: str
        puntaje: int
        path: str

    Returns:
        bool
    """
    scores = cargar_puntuaciones(config.RANKING_PATH)

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
        guardar_puntuaciones(top5, config.RANKING_PATH)
        return True

    return False


def mostrar_ranking(screen: pygame.Surface) -> None:
    """
    Carga, muestra y da formato en pantalla el top-5 de puntuaciones.
    Espera ESC o cierre de ventana para volver.

    Args:
        screen: pygame.surface
        path: str
    """
    puntuaciones = cargar_puntuaciones()
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

        screen.fill(config.NEGRO)

        titulo_surf = config.FUENTE_MEDIANA.render("Top 5 Gaucho Defense", True, config.BLANCO)
        titulo_rect = titulo_surf.get_rect(center=(config.ANCHO // 2, 60))
        screen.blit(titulo_surf, titulo_rect)

        base_y = 150
        espacio = 60
        y_actual = base_y
        for i in range(len(top5)):
            entrada = top5[i]
            texto = str(i+1) + ". " + entrada["nombre"] + " — " + str(entrada["puntaje"])
            surf = config.FUENTE_MEDIANA.render(texto, True, config.BLANCO)
            rect = surf.get_rect(center=(config.ANCHO // 2, y_actual))
            screen.blit(surf, rect)
            y_actual += espacio

        info_surf = config.FUENTE_MEDIANA.render("Presiona ESC para volver", True, config.BLANCO)
        info_rect = info_surf.get_rect(center=(config.ANCHO // 2, config.ALTO - 40))
        screen.blit(info_surf, info_rect)

        pygame.display.flip()
        clock.tick(60)
