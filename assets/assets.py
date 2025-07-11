import pygame, gif_pygame
import config

def cargar_assets():
    """Carga todos los assets necesarios para el juego.
    Devuelve un diccionario con las referencias a los assets cargados.
    """
    # Ventana
    pygame.display.set_caption("Gaucho Defense")  # Título de la ventana

    icono = pygame.image.load("assets/images/gaucho_logo.ico")
    pygame.display.set_icon(icono)

    # Fondo
    fondo_juego = pygame.image.load(config.RUTA_FONDO_JUEGO).convert_alpha()
    ancho_fondo_juego, alto_fondo_juego = fondo_juego.get_size()

    # Fondo de noche
    fondo_noche = pygame.image.load(config.RUTA_FONDO_JUEGO_NOCHE).convert_alpha()
    fondo_noche = pygame.transform.scale(fondo_noche, config.FONDO_SIZE)
    ancho_fondo_noche, altura_fondo_noche = fondo_noche.get_size()

    # Fondo del menú
    fondo_menu = pygame.transform.scale(pygame.image.load(config.RUTA_FONDO_MENU), config.FONDO_SIZE)
    ancho_fondo_menu, alto_fondo_menu = fondo_menu.get_size()

    # Fuentes
    pygame.font.init()
    FUENTE_GRANDE = pygame.font.Font(config.RUTA_FUENTE, config.FUENTE_TAM_GRANDE)
    FUENTE_MEDIANA = pygame.font.Font(config.RUTA_FUENTE, config.FUENTE_TAM_MEDIANA)
    FUENTE_TITULO_PRINCIPAL = pygame.font.Font(config.RUTA_FUENTE, config.FUENTE_TAM_TITULO)
    FUENTE_HUD      = pygame.font.Font(config.RUTA_FUENTE, config.FUENTE_TAM_HUD)
    FUENTE_JUGADOR    = pygame.font.Font(config.RUTA_FUENTE, config.FUENTE_TAM_JUGADOR)

    # Gaucho
    gaucho = pygame.image.load(config.RUTA_GAUCHO).convert_alpha()
    gaucho = pygame.transform.scale(gaucho, config.GAUCHO_SIZE)

    # Animaciones GIF
    caminar = gif_pygame.load(config.RUTA_CAMINAR)
    disparo = gif_pygame.load(config.RUTA_DISPARO)

    # Bala
    bala_img = pygame.Surface(config.BALA_SIZE)
    bala_img.fill(config.NEGRO)

    # Enemigos:
    zombie_img = gif_pygame.load(config.RUTA_ZOMBIE_1)

    zombie_muerto = pygame.image.load(config.RUTA_ZOMBIE_MUERTO).convert_alpha()
    zombie_muerto = pygame.transform.scale(zombie_muerto, config.ZOMBIE_SIZE)

    zombie_fuerte = gif_pygame.load(config.RUTA_ZOMBIE_FUERTE)

    zombie_herido = gif_pygame.load(config.RUTA_ZOMBIE_HERIDO)


    return {
        "imagenes": {
            "fondo_menu": fondo_menu,
            "fondo_juego": fondo_juego,
            "fondo_noche": fondo_noche,
            "fondo_actual": fondo_juego,
            "ultimo_cambio_fondo": 0,
            "ancho_fondo_juego": ancho_fondo_juego,
            "alto_fondo_juego": alto_fondo_juego,
            "ancho_fondo_menu": ancho_fondo_menu,
            "alto_fondo_menu": alto_fondo_menu,
        },
        "fuentes":{
            "fuente_grande": FUENTE_GRANDE,
            "fuente_mediana": FUENTE_MEDIANA,
            "fuente_titulo_principal": FUENTE_TITULO_PRINCIPAL,
            "fuente_jugador": FUENTE_JUGADOR,
            "fuente_hud": FUENTE_HUD,
        },
        "sprites":{
            "gaucho": gaucho,
            "caminar": caminar,
            "disparo": disparo,
            "bala_img": bala_img,
            "zombie_img": zombie_img,
            "zombie_fuerte": zombie_fuerte,
            "zombie_herido": zombie_herido,
            "zombie_muerto": zombie_muerto
        }
    }
