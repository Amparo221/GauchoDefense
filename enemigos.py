import pygame
import random
from config import SPAWN_DISPONIBLES, SPAWN_TIEMPO, ZOMBIE_SIZE, ZOMBIE_SPEED


def spawn_zombie(tiempo_ahora, ultimo_spawn, ancho_screen, lista_enemigos, zombie_img):
    if tiempo_ahora - ultimo_spawn >= SPAWN_TIEMPO:
        # y = SPAWN_DISPONIBLES[spawn_indice % len(SPAWN_DISPONIBLES)] # chequea esto
        y = random.choice(SPAWN_DISPONIBLES)
        # spawn_indice += 1

        zombie_rect = pygame.Rect(ancho_screen, y, *ZOMBIE_SIZE)
        lista_enemigos.append({"rect": zombie_rect, "img": zombie_img})
        return tiempo_ahora #, spawn_indice
    return ultimo_spawn #, spawn_indice

def mover_zombies(lista_enemigos):
    for z in lista_enemigos:
        z["rect"].x -= ZOMBIE_SPEED

def detectar_colisiones(balas, puntuacion, lista_enemigos):
    for bala in balas[:]:
        bala_rect = pygame.Rect(bala[0], bala[1], 15, 5)
        for z in lista_enemigos[:]:
            if bala_rect.colliderect(z["rect"]):
                lista_enemigos.remove(z)
                balas.remove(bala)
                puntuacion += 1
                break
    return puntuacion


def verificar_choque_con_jugador(gaucho_rect, vidas, lista_enemigos):
    for zombie in lista_enemigos:
        if gaucho_rect.colliderect(zombie['rect']):
            vidas -= 1
            lista_enemigos.remove(zombie)  
            break  
    return vidas