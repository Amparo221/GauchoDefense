import pygame
import random
from config import SPAWN_DISPONIBLES, SPAWN_TIEMPO, ZOMBIE_SIZE, ZOMBIE_SPEED, RUTA_ZOMBIE_MUERTO
from audio import reproducir_sonido


def spawn_zombie(tiempo_ahora, ultimo_spawn, ancho_screen, lista_enemigos, zombie_img):
    if tiempo_ahora - ultimo_spawn >= SPAWN_TIEMPO:
        y = random.choice(SPAWN_DISPONIBLES)

        zombie_rect = pygame.Rect(ancho_screen, y, *ZOMBIE_SIZE)
        lista_enemigos.append({
            "rect": zombie_rect, 
            "img": zombie_img,
            "vivo": True
        })

        return tiempo_ahora
    return ultimo_spawn

def mover_zombies(lista_enemigos):
    for z in lista_enemigos:
        z["rect"].x -= ZOMBIE_SPEED

def detectar_colisiones(balas, puntuacion, lista_enemigos, zombie_muerto_img, tiempo_ahora, sonido_hit):
    for bala in balas[:]:
        bala_rect = pygame.Rect(bala[0], bala[1], 15, 5)
        for z in lista_enemigos[:]:
            if z["vivo"] and bala_rect.colliderect(z["rect"]):
                z["vivo"] = False
                z["img"] = zombie_muerto_img
                z["tiempo_muerte"] = tiempo_ahora  # guardo el momento que murió

                reproducir_sonido(sonido_hit, "hit_zombie")

                balas.remove(bala)
                puntuacion += 1
                break
    return puntuacion


def verificar_choque_con_jugador(gaucho_rect, vidas, lista_enemigos, sonido_hurt_gaucho):
    for zombie in lista_enemigos:
        if gaucho_rect.colliderect(zombie['rect']):
            vidas -= 1

            reproducir_sonido(sonido_hurt_gaucho, "hurt_gaucho")

            lista_enemigos.remove(zombie)  
            break  
    return vidas

def remover_zombies_muertos(lista_enemigos, tiempo_actual, delay=300):
    for z in lista_enemigos[:]:
        if not z["vivo"] and "tiempo_muerte" in z:
            if tiempo_actual - z["tiempo_muerte"] > delay:
                lista_enemigos.remove(z)