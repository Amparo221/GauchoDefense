import pygame
from config import FONT_HUD, BLANCO, BACKGROUND_SPEED

def dibujar_fondo_estatico(pantalla: pygame.surface, fondo: pygame.surface, ancho_fondo: int, alto_fondo: int) -> None:
    """
    Emplaza el fondo estatico en pantalla
    """
    for y in range(0, pantalla.get_height(), alto_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))

def dibujar_fondo(pantalla: pygame.surface, fondo: pygame.surface, ancho_fondo: int, alto_fondo: int, estado: dict) -> None:  
    """
    Emplaza el fondo dinámico en pantalla, se mueve a la izquierda a una velocidad constante.
    Actualiza la pantalla para que nunca se deje de mostrar la imagen.
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
    """
    texto = FONT_HUD.render(f'Puntuación: {puntaje}  Vidas: {vidas}', True, BLANCO)
    pantalla.blit(texto, (10, 10))

def dibujar_enemigos(pantalla: pygame.surface, lista_enemigos: list) -> None:
    """
    Itera sobre enemies_list y:
    - Si es un GIF de gif_pygame lo dibuja -> si tiene render como atributo
    - Si es una Surface estática lo dibuja
    """
    for e in lista_enemigos:
        if hasattr(e["img"], "render"):
            # Es un GIF de gif_pygame
            e["img"].render(pantalla, (e["rect"].x, e["rect"].y))
        else:
            # Es una Surface estática
            pantalla.blit(e["img"], (e["rect"].x, e["rect"].y))