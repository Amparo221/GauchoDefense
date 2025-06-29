import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((1000, 600))
tile_image = pygame.image.load("GauchoDefense/assets/tile.png").convert()
tile_width, tile_height = tile_image.get_size()  

default = pygame.image.load("GauchoDefense/assets/default.png").convert_alpha()
default_size=(150,150)
default = pygame.transform.scale(default, default_size)
default_x = 0
default_y = 0
speed = 5




# BALAS
bullet_img = pygame.Surface((15, 5))  
bullet_img.fill((250, 0, 0)) 
bullet_speed = 10
bullets = []  #Lista pa las balas
last_shot_time = 0  
cooldown = 400  


def draw_tiled_background():
    for y in range(0, pantalla.get_height(), tile_height):
        for x in range(0, pantalla.get_width(), tile_width):
            pantalla.blit(tile_image, (x, y))


def player_movement(current_y, speed):
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w]:
        current_y -= speed
    if pressed_keys[K_s]:
        current_y += speed

    #eeeh que no se vaya de pantalla
    if current_y < 0:
        current_y = 0
    if current_y > pantalla.get_height() - default_size[1]:
        current_y = pantalla.get_height() - default_size[1]
        
    return current_y




#disparar balas (a traducir)
def shoot_bullet(bullets_list, current_time, last_shot, cooldown_time):
    for bullet in bullets_list[:]:
        bullet[0] += bullet_speed
        if bullet[0] > pantalla.get_width():
            bullets_list.remove(bullet)
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE] and current_time - last_shot >= cooldown_time:
        bullet_x = default_x + default_size[0]
        bullet_y = default_y + default_size[1] // 2
        bullets_list.append([bullet_x, bullet_y])
        return current_time
    
    return last_shot

    




def draw_bullets():
    for bullet in bullets:
        pantalla.blit(bullet_img, (bullet[0], bullet[1]))

running = True
clock = pygame.time.Clock()

while running:

    current_time = pygame.time.get_ticks()

    print(current_time)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
            
        
    default_y = player_movement(default_y, speed)

    
    last_shot_time = shoot_bullet(
        bullets, 
        current_time, 
        last_shot_time, 
        cooldown
    )

    
    draw_tiled_background()
    draw_bullets()
    
    pantalla.blit(default, (default_x, default_y))

     
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
    