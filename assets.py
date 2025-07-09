import pygame
import gif_pygame
from config import *

def cargar_assets():
    # Ventana
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Gaucho Defense")  # Título de la ventana

    # Fondo
    fondo = pygame.image.load(RUTA_FONDO).convert()
    ancho_fondo, altura_fondo = fondo.get_size()

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
        "fondo": fondo,
        "ancho_fondo": ancho_fondo,
        "altura_fondo": altura_fondo,
        "gaucho": gaucho,
        "caminar": caminar,
        "disparo": disparo,
        "bala_img": bala_img,
        "zombie_img": zombie_img,
        "zombie_muerto": zombie_muerto
    }
