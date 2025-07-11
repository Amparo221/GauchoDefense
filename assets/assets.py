import pygame
import gif_pygame
from config import *

def cargar_assets() -> dict:
    """
    Carga y devuelve un diccionario con todos los assets a usar.
    Returns:
        dict{
        "pantalla": pantalla,
        "fondo": fondo,
        "fondo_noche": fondo_noche,
        "fondo_actual": "fondo",
        "ultimo_cambio_fondo": 0,
        "fondo_menu": fondo_menu,
        "ancho_fondo": ancho_fondo,
        "altura_fondo": altura_fondo,
        "gaucho": gaucho,
        "caminar": caminar,
        "disparo": disparo,
        "bala_img": bala_img,
        "zombie_img": zombie_img,
        "zombie_fuerte": zombie_fuerte,
        "zombie_herido": zombie_herido,
        "zombie_muerto": zombie_muerto
    }
    """
    # Ventana
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Gaucho Defense")  # Título de la ventana

    icono = pygame.image.load("assets/images/gaucho_logo.ico")
    pygame.display.set_icon(icono)

    # Fondo
    fondo = pygame.image.load(RUTA_FONDO_JUEGO).convert_alpha()
    fondo = pygame.transform.scale(fondo, FONDO_SIZE)
    ancho_fondo, altura_fondo = fondo.get_size()

    # Fondo de noche
    fondo_noche = pygame.image.load(RUTA_FONDO_JUEGO_NOCHE).convert_alpha()
    fondo_noche = pygame.transform.scale(fondo_noche, FONDO_SIZE)
    ancho_fondo, altura_fondo = fondo_noche.get_size()

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

    zombie_fuerte = gif_pygame.load(RUTA_ZOMBIE_FUERTE)

    zombie_herido = gif_pygame.load(RUTA_ZOMBIE_HERIDO)


    return {
        "pantalla": pantalla,
        "fondo": fondo,
        "fondo_noche": fondo_noche,
        "fondo_actual": "fondo",
        "ultimo_cambio_fondo": 0,
        "fondo_menu": fondo_menu,
        "ancho_fondo": ancho_fondo,
        "altura_fondo": altura_fondo,
        "gaucho": gaucho,
        "caminar": caminar,
        "disparo": disparo,
        "bala_img": bala_img,
        "zombie_img": zombie_img,
        "zombie_fuerte": zombie_fuerte,
        "zombie_herido": zombie_herido,
        "zombie_muerto": zombie_muerto
    }
