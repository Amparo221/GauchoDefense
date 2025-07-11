import pygame
import random
import config
from game.audio import reproducir_sonido


def spawn_zombie(tiempo_ahora, ultimo_spawn, lista_enemigos, assets):
    if tiempo_ahora - ultimo_spawn >= config.SPAWN_TIEMPO:
        y = random.choice(config.SPAWN_DISPONIBLES)

        zombie_rect = pygame.Rect(config.ANCHO, y, *config.ZOMBIE_SIZE)

        # Por medio de random se puede manejar la probabilidad de aparicion de un enemigo fuerte, en este caso 30%
        es_fuerte = random.random() < 0.3 

        if es_fuerte:
            enemigo = {
                "rect": zombie_rect,
                "img": assets["sprites"]["zombie_fuerte"],
                "img_herido": assets["sprites"]["zombie_herido"],
                "vivo": True,
                "vida": 2
            }
        else:
            enemigo = {
                "rect": zombie_rect,
                "img": assets["sprites"]["zombie_img"],
                "vivo": True,
                "vida": 1
            }

        lista_enemigos.append(enemigo)
        return tiempo_ahora
    return ultimo_spawn

def mover_zombies(lista_enemigos: list) -> None:
    """"
    Se mueven los enemigos hacia la izquierda
    Args:
        lista_enemigos: list
    """
    for z in lista_enemigos:
        z["rect"].x -= config.ZOMBIE_SPEED

def detectar_colisiones(balas: list, puntuacion: int, lista_enemigos: list, zombie_muerto_img: pygame.surface, tiempo_ahora: int, sonido_hit: dict) -> int:
    """
    Detecta colisiones y actualiza la puntuacion
    Args:
        balas: list
        puntuacion: int
        lista_enemigos: list
        zombie_muerto_img: pygame.surface
        tiempo_ahora: int
        sonido_hit: dict
    Returns:
        int (puntuacion)
    """
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


def verificar_choque_con_jugador(gaucho_rect: pygame.rect, vidas: int, lista_enemigos: list, sonido_hurt_gaucho: dict) -> int:
    """
    Si el gaucho choca con un zombie se le resta una vida y se reproduce el sonido de hurt_gaucho.
    Se remueve el zombie y se devuelve la cantidad de vidas restantes
    Args:
        gaucho_rect: pygame.rect
        vidas: int
        lista_enemigos: list
        sonido_hurt_gaucho: dict
    Returns:
        int (vidas)
    """
    for zombie in lista_enemigos:
        if gaucho_rect.colliderect(zombie['rect']):
            vidas -= 1

            reproducir_sonido(sonido_hurt_gaucho, "hurt_gaucho")

            lista_enemigos.remove(zombie)  
            break  
    return vidas

def remover_zombies_muertos(lista_enemigos: list, tiempo_actual: int, delay: int=300) -> None:
    """
    Si un zombie muere se remueve de la lista
    Args:
        lista_enemigos: list
        tiempo_actual: int
        delay: int
    """
    for z in lista_enemigos[:]:
        if not z["vivo"] and "tiempo_muerte" in z:
            if tiempo_actual - z["tiempo_muerte"] > delay:
                lista_enemigos.remove(z)