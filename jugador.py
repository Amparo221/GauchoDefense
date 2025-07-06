import pygame
from pygame.locals import *



gaucho_size = (150, 150)

gaucho_x = 0
gaucho_y = 0
gaucho_velocidad = 5





def movimiento_jugador(y_actual, gaucho_velocidad):
    tecla_presionada = pygame.key.get_pressed()
    movimiento = False
    
    if tecla_presionada[K_w]:
        y_actual -= gaucho_velocidad
        movimiento = True
    if tecla_presionada[K_s]:
        y_actual += gaucho_velocidad
        movimiento = True

    if y_actual < 0:
        y_actual = 0
    if y_actual > 600 - gaucho_size[1]:
        y_actual = 600 - gaucho_size[1]
        
    return y_actual, movimiento



def disparar_balas(lista_de_balas, tiempo_actual, ultimo_disparo, cooldown, jugador_x, jugador_y, jugador_size):
    disparar=False
    bala_velocidad = 15
    for bala in lista_de_balas[:]:
        bala[0] += bala_velocidad
        if bala[0] > 1000:
            lista_de_balas.remove(bala)
    
    tecla_presionada = pygame.key.get_pressed()
    if tecla_presionada[K_SPACE] and tiempo_actual - ultimo_disparo >= cooldown:
        disparar=True
        bala_x = jugador_x + jugador_size[0]
        bala_y = jugador_y + ((jugador_size[1] // 2)-15)
        lista_de_balas.append([bala_x, bala_y])
        return tiempo_actual, disparar

    if tiempo_actual - ultimo_disparo < 300:
        return ultimo_disparo, disparar
    
    return ultimo_disparo, disparar

