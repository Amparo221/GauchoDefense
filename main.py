import pygame
from pygame.locals import *
from jugador import *

pygame.init()

pantalla = pygame.display.set_mode((1000, 600))
fondo = pygame.image.load("GauchoDefense/assets/fondo.png").convert()
ancho_fondo, altura_fondo = fondo.get_size()  

gaucho = pygame.image.load("GauchoDefense/assets/default.png").convert_alpha()
gaucho_size=(150,150)
gaucho = pygame.transform.scale(gaucho, gaucho_size)
gaucho_x = 0
gaucho_y = 0
gaucho_velocidad = 5


# BALAS
bala_img = pygame.Surface((15, 5))  
bala_img.fill((250, 0, 0)) 
balas = []  #Lista pa las balas
ultimo_disparo = 0  
cooldown = 400  


def crear_fondo():
    for y in range(0, pantalla.get_height(), altura_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))


def crear_balas():
    for bala in balas:
        pantalla.blit(bala_img, (bala[0], bala[1]))


running = True
reloj = pygame.time.Clock()


while running:

    tiempo_actual = pygame.time.get_ticks()


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
            
        
    gaucho_y = movimiento_jugador(gaucho_y, gaucho_velocidad)

    
    ultimo_disparo = disparar_balas(
        balas, 
        tiempo_actual, 
        ultimo_disparo, 
        cooldown,
        gaucho_x, 
        gaucho_y,
        gaucho_size
    )

    
    crear_fondo()
    crear_balas()
    
    pantalla.blit(gaucho, (gaucho_x, gaucho_y))

     
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
quit()
    