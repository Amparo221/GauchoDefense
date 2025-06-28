import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((1000, 600))
tile_image = pygame.image.load("assets/tile.png").convert()
tile_width, tile_height = tile_image.get_size()  # Get its dimensions

default = pygame.image.load("assets\default.png").convert_alpha()#convert_alpha paar que funcione el fondo transparente
default_size=(150,150)
default = pygame.transform.scale(default, default_size)
default_x = 0
default_y = 0
speed = 5


shoot_cooldown = 0

# BALAS
bullet_img = pygame.Surface((15, 5))  
bullet_img.fill((250, 0, 0)) 
bullet_speed = 10
bullets = []  #Lista pa las balas



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
def shoot_bullet():
    if shoot_cooldown == 0 and pygame.key.get_pressed()[K_SPACE]:
        bullet_x = default_x + default_size[0]
        bullet_y = default_y + default_size[1] // 2
        bullets.append([bullet_x, bullet_y])
        shoot_cooldown = 10
    
    


def update_bullet():
    # Move all bullets and remove those off-screen
    bullets_to_keep = []
    for bullet in bullets:
        bullet[0] += bullet_speed  # Move bullet right
        # Keep bullet if it's still on screen
        if bullet[0] < pantalla.get_width():
            bullets_to_keep.append(bullet)
    
    # Update bullets list
    bullets[:] = bullets_to_keep

def draw_bullets():
    for bullet in bullets:
        pantalla.blit(bullet_img, (bullet[0], bullet[1]))

running = True
clock = pygame.time.Clock()

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
            
        
    default_y = player_movement(default_y, speed)

    shoot_bullet()
    update_bullet()

    
    draw_tiled_background()  # Draw the tiled image
    draw_bullets()
    
    pantalla.blit(default, (default_x, default_y))

     
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
    