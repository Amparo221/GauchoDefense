import pygame
import random

SPAWN_TIEMPO = 2000
spawn_indice = 0
ultimo_spawn = 0 
alturas_disponibles = [50, 150, 250, 350, 450] # cambiar por random

zombie_img = pygame.image.load("GauchoDefense/assets/soldado1_1.png")
zombie_tamanio = (120, 120)
zombie_img = pygame.transform.scale(zombie_img, zombie_tamanio) #fijate de arreglar esto

zombie_velocidad = 2

zombies = []

def spawn_zombie(tiempo_ahora, ultimo, ancho_screen):
    if tiempo_ahora - ultimo >= SPAWN_TIEMPO:
        # y = alturas_disponibles[spawn_indice % len(alturas_disponibles)] # chequea esto
        y = random.choice(alturas_disponibles)
        # spawn_indice += 1

        nuevo = {
            "rect": pygame.Rect(ancho_screen, y, *zombie_tamanio),
            "img": zombie_img
        }
        zombies.append(nuevo)
        return tiempo_ahora #, spawn_indice
    return ultimo #, spawn_indice

def mover_zombies():
    for z in zombies:
        z["rect"].x -= zombie_velocidad 


def dibujar_zombies(pantalla):
    for z in zombies:
        pantalla.blit(z["img"], z["rect"]) 

def detectar_colisiones(balas, puntaje):
    for bala in balas[:]:
        bala_rect = pygame.Rect(bala[0], bala[1], 15, 5)
        for z in zombies[:]:
            if bala_rect.colliderect(z["rect"]):
                zombies.remove(z)
                balas.remove(bala)
                puntaje += 1
                break
    return puntaje


def verificar_choque_con_jugador(gaucho_rect, vidas):
    for zombie in zombies:
        if gaucho_rect.colliderect(zombie['rect']):
            vidas -= 1
            zombies.remove(zombie)  # Remove the zombie that hit the player
            break  # Only count one hit per frame
    return vidas