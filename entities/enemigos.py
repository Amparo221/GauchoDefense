import pygame
import random
from config import SPAWN_DISPONIBLES, SPAWN_TIEMPO, ZOMBIE_SIZE, ZOMBIE_SPEED, RUTA_ZOMBIE_MUERTO
from game.audio import reproducir_sonido


def spawn_zombie(tiempo_ahora, ultimo_spawn, ancho_screen, lista_enemigos, assets):
    if tiempo_ahora - ultimo_spawn >= SPAWN_TIEMPO:
        y = random.choice(SPAWN_DISPONIBLES)

        zombie_rect = pygame.Rect(ancho_screen, y, *ZOMBIE_SIZE)

        # Por medio de random se puede manejar la probabilidad de aparicion de un enemigo fuerte, en este caso 30%
        es_fuerte = random.random() < 0.3 

        if es_fuerte:
            enemigo = {
                "rect": zombie_rect,
                "img": assets["zombie_fuerte"],
                "img_herido": assets["zombie_herido"],
                "vivo": True,
                "vida": 2
            }
        else:
            enemigo = {
                "rect": zombie_rect,
                "img": assets["zombie_img"],
                "vivo": True,
                "vida": 1
            }

        lista_enemigos.append(enemigo)
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
                z["vida"] -= 1

                if z["vida"] == 1 and "img_herido" in z:
                    z["img"] = z["img_herido"]

                if z["vida"] <= 0:
                    z["vivo"] = False
                    z["img"] = zombie_muerto_img
                    z["tiempo_muerte"] = tiempo_ahora
                    puntuacion += 1

                reproducir_sonido(sonido_hit, "hit_zombie")
                balas.remove(bala)
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