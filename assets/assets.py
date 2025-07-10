import pygame
import gif_pygame
from config import *

def cargar_assets():
    # Ventana
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Gaucho Defense")  # Título de la ventana

    # Fondo
    fondo_juego = pygame.image.load(RUTA_FONDO_JUEGO).convert_alpha()
    ancho_fondo_juego, alto_fondo_juego = fondo_juego.get_size()

    # Fondo del menú
    fondo_menu = pygame.image.load(RUTA_FONDO_MENU).convert_alpha()
    fondo_menu = pygame.transform.scale(fondo_menu, FONDO_SIZE)

    # Gaucho
    gaucho = pygame.image.load(RUTA_GAUCHO).convert_alpha()
    gaucho = pygame.transform.scale(gaucho, GAUCHO_SIZE)

    # Animaciones GIF
    caminar = gif_pygame.load(RUTA_CAMINAR)
    disparo = gif_pygame.load(RUTA_DISPARO)

    # Bala
    bala_img = pygame.Surface(BALA_SIZE)
    bala_img.fill(NEGRO)

    # Enemigos:
    zombie_img = gif_pygame.load(RUTA_ZOMBIE_1)

    zombie_muerto = pygame.image.load(RUTA_ZOMBIE_MUERTO).convert_alpha()
    zombie_muerto = pygame.transform.scale(zombie_muerto, ZOMBIE_SIZE)


    return {
        "pantalla": pantalla,
        "fondo_juego": fondo_juego,
        "fondo_menu": fondo_menu,
        "ancho_fondo_juego": ancho_fondo_juego,
        "alto_fondo_juego": alto_fondo_juego,
        "ancho_fondo_menu": ANCHO,
        "alto_fondo_menu": ALTO,
        "gaucho": gaucho,
        "caminar": caminar,
        "disparo": disparo,
        "bala_img": bala_img,
        "zombie_img": zombie_img,
        "zombie_muerto": zombie_muerto
    }
