import pygame
from pygame.locals import *
from config import GAUCHO_SIZE, GAUCHO_SPEED
from audio import reproducir_sonido

def crear_balas(pantalla, balas, bala_img):
    for bala in balas:
        pantalla.blit(bala_img, (bala[0], bala[1]))


def movimiento_jugador(y_actual, GAUCHO_SPEED, ALTO):
    tecla_presionada = pygame.key.get_pressed()
    movimiento = False
    
    if tecla_presionada[K_w]:
        y_actual -= GAUCHO_SPEED
        movimiento = True
    if tecla_presionada[K_s]:
        y_actual += GAUCHO_SPEED
        movimiento = True

    if y_actual < 0:
        y_actual = 0
    if y_actual > ALTO - GAUCHO_SIZE[1]:
        y_actual = ALTO - GAUCHO_SIZE[1]
        
    return y_actual, movimiento



def disparar_balas(lista_de_balas: list, tiempo_actual: int, ultimo_disparo: int, cooldown: int, jugador_x: int, jugador_y: int, jugador_size: int, 
                   ancho_pantalla: int, sonido_disparo: dict) -> tuple[int, bool]:
    """
    - Gestiona movimiento y expiración de balas.
    - Si SPACE y cooldown ok, crea una bala y suena el SFX.
    Devuelve (nuevo_ultimo_disparo, disparar_flag).
    """
    bala_velocidad = 15
    for bala in lista_de_balas[:]:
        bala[0] += bala_velocidad
        if bala[0] > ancho_pantalla:
            lista_de_balas.remove(bala)
    
    disparar = False
    tecla_presionada = pygame.key.get_pressed()
    if tecla_presionada[K_SPACE] and tiempo_actual - ultimo_disparo >= cooldown:
        disparar=True
        bala_x = jugador_x + jugador_size[0]
        bala_y = jugador_y + ((jugador_size[1] // 2)-15)
        lista_de_balas.append([bala_x, bala_y])

        # sonido disparo despues de crear la bala
        reproducir_sonido(sonido_disparo, "disparo")

        return tiempo_actual, disparar

    if tiempo_actual - ultimo_disparo < 300:
        return ultimo_disparo, disparar
    
    return ultimo_disparo, disparar

def generar_animaciones(
    pantalla,
    jugador_img,
    disparar_flag,
    tiempo_actual,
    anim_disparo,
    duracion_disparo,
    en_movimiento,
    anim_caminar,
    pos_x,
    pos_y,
    disparo_playing,
    disparo_start_time
):
    """
    Gestiona la animación de disparo y de caminar:
      - Si disparar_flag==True: arranca la animación de disparo.
      - Mientras disparo_playing: renderiza anim_disparo.
      - Si no: si en_movimiento, renderiza anim_caminar.
      - Si no: pinta el sprite estático (jugador_img).
    Devuelve (nuevo_disparo_playing, nuevo_disparo_start_time).
    """
    # disparo justo disparado
    if disparar_flag and not disparo_playing:
        disparo_playing = True
        disparo_start_time = tiempo_actual
        anim_disparo.reset()

    # render de disparo
    if disparo_playing:
        anim_disparo.render(pantalla, (pos_x, pos_y))
        if tiempo_actual - disparo_start_time >= duracion_disparo:
            disparo_playing = False

    # render de caminar
    elif en_movimiento:
        anim_caminar.render(pantalla, (pos_x, pos_y))

    # render estático
    else:
        pantalla.blit(jugador_img, (pos_x, pos_y))

    return disparo_playing, disparo_start_time

