import pygame

ANCHO, ALTO = 1000, 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS   = ( 50,  50,  50)
COLOR_HOVER = (200, 200, 200)

# Fuentes
pygame.font.init()
fuente_grande = pygame.font.SysFont("arial", 40)
fuente_mediana = pygame.font.SysFont("arial", 30)

# Sonidos
SONIDO_CLICK = "assets/sounds/click.ogg"