import pygame
from config import FONT_HUD, BLANCO, BACKGROUND_SPEED

def dibujar_fondo_estatico(pantalla: pygame.surface, fondo: pygame.surface, ancho_fondo: int, alto_fondo: int) -> None:
    """
    Emplaza el fondo estatico en pantalla

    Args:
        pantalla (pygame.surface): superficie de la pantalla del juego.
        fondo (pygame.surface): superficie con el fondo del juego.
        ancho_fondo (int): ancho del fondo.
        alto_fondo (int): alto del fondo.
    """
    for y in range(0, pantalla.get_height(), alto_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))

def dibujar_fondo(pantalla: pygame.surface, fondo: pygame.surface, ancho_fondo: int, alto_fondo: int, estado: dict) -> None:  
    """
    Emplaza el fondo dinámico en pantalla, se mueve a la izquierda a una velocidad constante.
    Actualiza la pantalla para que nunca se deje de mostrar la imagen.

    Args:
        pantalla (pygame.surface): superficie de la pantalla del juego.
        fondo (pygame.surface): superficie con el fondo del juego.
        ancho_fondo (int): ancho del fondo.
        alto_fondo (int): alto del fondo.
        estado (dict): diccionario con el estado del juego.
    """  
    estado["fondo_x"] -= BACKGROUND_SPEED

    if estado["fondo_x"] <= -ancho_fondo:
        estado["fondo_x"] = 0

    for y in range(0, pantalla.get_height(), alto_fondo):
        for x in range(0, pantalla.get_width() + ancho_fondo, ancho_fondo):
            pantalla.blit(fondo, (x + estado["fondo_x"], y))

def dibujar_hud(pantalla: pygame.surface, puntaje: int, vidas: int) -> None:
    """
    Dibuja la informacion vital para el jugador: el puntaje y las vidas (HUD)

    Args:
        pantalla (pygame.surface): superficie de la pantalla del juego.
        puntaje (int): puntaje del jugador.
        vidas (int): vidas del jugador.
    """
    texto = FONT_HUD.render(f'Puntuación: {puntaje}  Vidas: {vidas}', True, BLANCO)
    pantalla.blit(texto, (10, 10))

def dibujar_enemigos(pantalla: pygame.surface, lista_enemigos: list) -> None:
    """
    Itera sobre enemies_list y:
    - Si es un GIF de gif_pygame lo dibuja -> si tiene render como atributo
    - Si es una Surface estática lo dibuja

    Args:
        pantalla (pygame.surface): superficie de la pantalla del juego.
        lista_enemigos (list): lista de diccionarios con informacion de los enemigos.
    """
    for e in lista_enemigos:
        if hasattr(e["img"], "render"):
            # Es un GIF de gif_pygame
            e["img"].render(pantalla, (e["rect"].x, e["rect"].y))
        else:
            # Es una Surface estática
            pantalla.blit(e["img"], (e["rect"].x, e["rect"].y))