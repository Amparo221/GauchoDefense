import pygame, gif_pygame
from pygame.locals import *
from jugador import *

pygame.init()

pantalla = pygame.display.set_mode((1000, 600))
fondo = pygame.image.load("GauchoDefense/assets/fondo.png").convert()
ancho_fondo, altura_fondo = fondo.get_size()  

gaucho = pygame.image.load("GauchoDefense/assets/gaucho.png").convert_alpha()
gaucho_size=(155,175)
gaucho = pygame.transform.scale(gaucho, gaucho_size)
gaucho_x = 0
gaucho_y = 0
gaucho_velocidad = 5

caminar = gif_pygame.load("GauchoDefense/assets/caminar_2.gif")
disparo = gif_pygame.load("GauchoDefense/assets/disparo_3.gif")

tecla_presionada = pygame.key.get_pressed()

# BALAS
bala_img = pygame.Surface((15, 5))  
bala_img.fill((0, 0, 0)) 
balas = []  #Lista pa las balas
ultimo_disparo = 0  
cooldown = 400  



disparo_playing = False
disparo_start_time = 0
disparo_duration = 400  














def crear_fondo():
    for y in range(0, pantalla.get_height(), altura_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))


def crear_balas():
    for bala in balas:
        pantalla.blit(bala_img, (bala[0], bala[1]))


running = True
reloj = pygame.time.Clock()
movimiento = False
disparar = False

while running:

    tiempo_actual = pygame.time.get_ticks()


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
            
        
    gaucho_y, is_moving = movimiento_jugador(gaucho_y, gaucho_velocidad)

    
    ultimo_disparo, disparar = disparar_balas(
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
    
    if disparar:
        disparo_playing = True
        disparo_start_time = tiempo_actual
        disparo.reset() 
    if disparo_playing:
        
        disparo.render(pantalla, (gaucho_x, gaucho_y))
    
        if tiempo_actual - disparo_start_time >= disparo_duration:
            disparo_playing = False
    elif is_moving:
        caminar.render(pantalla, (gaucho_x, gaucho_y))
    else:
        pantalla.blit(gaucho, (gaucho_x, gaucho_y))



     
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
quit()
    