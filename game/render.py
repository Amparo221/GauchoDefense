import pygame
from ui.renderer import dibujar_fondo, dibujar_hud, dibujar_enemigos
from entities.jugador import crear_balas, generar_animaciones

def renderizar_juego(pantalla, estado, assets):
    """Renderiza el estado actual del juego en la pantalla.
    Args:
        pantalla (pygame.Surface): Superficie donde se dibuja el juego.
        estado (dict): Estado actual del juego, incluyendo jugador, enemigos, balas, etc.
        assets (dict): Diccionario con los assets cargados (imágenes, sonidos, etc.).
    """
    # Limpiar pantalla
    pantalla.fill((0, 0, 0))  # Color

    dibujar_fondo(pantalla, assets["imagenes"]["fondo_juego"], assets["imagenes"]["ancho_fondo_juego"], assets["imagenes"]["alto_fondo_juego"])

    crear_balas(pantalla, estado.get("balas", []), assets["sprites"]["bala_img"])

    dp_playing, dp_start = generar_animaciones(
    pantalla             = pantalla,
    jugador_img          = assets["sprites"]["gaucho"],
    disparar_flag        = estado["flags"]["disparar"],
    tiempo_actual        = pygame.time.get_ticks(),
    anim_disparo         = assets["sprites"]["disparo"],
    duracion_disparo     = 400,
    en_movimiento        = estado["jugador"]["en_movimiento"],
    anim_caminar         = assets["sprites"]["caminar"],
    pos_x                = estado["jugador"]["x"],
    pos_y                = estado["jugador"]["y"],
    disparo_playing      = estado["flags"]["disparo_playing"],
    disparo_start_time   = estado["tiempos"]["tiempo_inicio_disparo"]
    )
    estado["flags"]["disparo_playing"]      = dp_playing
    estado["tiempos"]["tiempo_inicio_disparo"] = dp_start
    
    # dibujar zombies
    dibujar_enemigos(pantalla, estado["enemigos"])

    # HUD
    dibujar_hud(pantalla, assets["fuentes"]["fuente_hud"], estado["puntuacion"], estado["vidas"])
    
    pygame.display.flip()