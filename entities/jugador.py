import pygame
from pygame.locals import *
import config
from game.audio import reproducir_sonido

def crear_balas(pantalla: pygame.surface, balas: list, bala_img: pygame.surface) -> None:
    """
    Dibuja las balas
    """
    for bala in balas:
        pantalla.blit(bala_img, (bala[0], bala[1]))


def movimiento_jugador(y_actual, velcidad_movimiento):
    tecla_presionada = pygame.key.get_pressed()
    movimiento = False

    if tecla_presionada[K_w]:
        y_actual -= velcidad_movimiento
        movimiento = True
    if tecla_presionada[K_s]:
        y_actual += velcidad_movimiento
        movimiento = True

    if y_actual < 0:
        y_actual = 0
    if y_actual > config.ALTO - config.GAUCHO_SIZE[1]:
        y_actual = config.ALTO - config.GAUCHO_SIZE[1]
        
    return y_actual, movimiento



def disparar_balas(lista_de_balas: list, tiempo_actual: int, ultimo_disparo: int, jugador_x: int, jugador_y: int, 
                   sonido_disparo: dict) -> tuple[int, bool]:
    """
    Gestiona movimiento y expiración de balas.
    - Si SPACE y cooldown ok, crea una bala y suena el SFX.
    Devuelve (nuevo_ultimo_disparo, disparar_flag).
    Args:
        lista_de_balas: list
        tiempo_actual: int
        ultimo_disparo: int
        jugador_x: int
        jugador_y: int
        sonido_disparo: dict
    Returns:
        tuple[int, bool] (ultimo_disparo, disparar)
    """
    bala_velocidad = 15
    for bala in lista_de_balas[:]:
        bala[0] += bala_velocidad
        if bala[0] > config.ANCHO:
            lista_de_balas.remove(bala)
    
    disparar = False
    tecla_presionada = pygame.key.get_pressed()
    if tecla_presionada[K_SPACE] and tiempo_actual - ultimo_disparo >= config.COOLDOWN_DISPARO:
        disparar=True
        bala_x = jugador_x + config.GAUCHO_SIZE[0]
        bala_y = jugador_y + ((config.GAUCHO_SIZE[1] // 2)-15)
        lista_de_balas.append([bala_x, bala_y])

        reproducir_sonido(sonido_disparo, "disparo")

        return tiempo_actual, disparar
    
    return ultimo_disparo, disparar


def generar_animaciones(
    pantalla: pygame.surface,
    jugador_img: pygame.surface,
    disparar_flag: bool,
    tiempo_actual: int,
    anim_disparo: pygame.sprite.Group,
    duracion_disparo: int,
    en_movimiento: bool,
    anim_caminar: pygame.sprite.Group,
    pos_x: int,
    pos_y: int,
    disparo_playing: bool,
    disparo_start_time: int
) -> tuple[bool, int]:
    """
    Gestiona la animación de disparo y de caminar:
    Si está disparando: muestra la animación de disparo.
    Si está caminando: muestra la animación de caminar.
    Si está quieto: muestra el sprite estático.
      - Si disparar_flag==True: arranca la animación de disparo.
      - Mientras disparo_playing: renderiza anim_disparo.
      - Si no: si en_movimiento, renderiza anim_caminar.
      - Si no: pinta el sprite estático (jugador_img).
    Devuelve:
    Si el disparo sigue activo (nuevo_disparo_playing)
    Cuándo empezó (nuevo_disparo_start_time)
    
    Args:    
        pantalla: pygame.surface
        jugador_img: pygame.surface
        disparar_flag: bool
        tiempo_actual: int
        anim_disparo: pygame.sprite.Group
        duracion_disparo: int
        en_movimiento: bool
        anim_caminar: pygame.sprite.Group
        pos_x: int
        pos_y: int
        disparo_playing: bool
        disparo_start_time: int
    Returns:
        tuple[bool, int] (disparo_playing, disparo_start_time)
    """

    if disparar_flag and not disparo_playing:
        disparo_playing = True
        disparo_start_time = tiempo_actual
        anim_disparo.reset()

    if disparo_playing:
        anim_disparo.render(pantalla, (pos_x, pos_y))
        if tiempo_actual - disparo_start_time >= duracion_disparo:
            disparo_playing = False

    elif en_movimiento:
        anim_caminar.render(pantalla, (pos_x, pos_y))

    else:
        pantalla.blit(jugador_img, (pos_x, pos_y))

    return disparo_playing, disparo_start_time