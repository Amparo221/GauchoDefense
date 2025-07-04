import pygame

spawn_indice = 0 
alturas_disponibles = [50, 150, 250, 350, 450]

zombie_img = pygame.image.load("assets/result.png")
zombie_tamanio = (150, 150)
zombie_img = pygame.transform.scale(zombie_img, zombie_tamanio) #fijate de arreglar esto

zombies = []

zombie_velocidad = 3 

SPAWN_TIME = 2000
ultimo_spawn = 0 

def spawn_zombie(tiempo_ahora, ultimo, ancho_screen, spawn_indice):
    if tiempo_ahora - ultimo >= SPAWN_TIME:
        y = alturas_disponibles[spawn_indice % len(alturas_disponibles)] # chequea esto
        spawn_indice += 1

        nuevo = {
            "rect": pygame.Rect(ancho_screen, y, *zombie_tamanio),
            "img": zombie_img
        }
        zombies.append(nuevo)
        return tiempo_ahora, spawn_indice
    return ultimo, spawn_indice

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


def verificar_golpe_jugador(gaucho_rect, vidas):
    for z in zombies[:]:
        if z["rect"].colliderect(gaucho_rect):
            zombies.remove(z)
            vidas -= 1
    return vidas
