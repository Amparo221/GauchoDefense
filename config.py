import pygame

ANCHO, ALTO = 1000, 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS   = ( 50,  50,  50)
COLOR_HOVER = (200, 200, 200)

# Rutas a assets
RUTA_FONDO         = "GauchoDefense/assets/images/fondo.png"
RUTA_GAUCHO        = "GauchoDefense/assets/images/gaucho.png"
RUTA_ZOMBIE_1      = "GauchoDefense/assets/images/sprite_zombie.gif"
RUTA_CAMINAR       = "GauchoDefense/assets/images/caminar.gif"
RUTA_DISPARO       = "GauchoDefense/assets/images/disparo.gif"
RUTA_FUENTE        = "GauchoDefense/assets/fonts/Jersey10-Regular.ttf"
RUTA_ZOMBIE_MUERTO = "GauchoDefense/assets/images/zombie_muerto.png"

# Fuentes
pygame.font.init()
fuente_grande = pygame.font.Font(RUTA_FUENTE, 40)
fuente_mediana = pygame.font.Font(RUTA_FUENTE, 30)
FONT_HUD      = pygame.font.Font(RUTA_FUENTE, 36)
FONT_TITLE    = pygame.font.Font(RUTA_FUENTE, 48)

# Sonidos
SONIDO_CLICK = "GauchoDefense/assets/sounds/click.ogg"
RUTA_SONIDO_DISPARO = "GauchoDefense/assets/sounds/disparo_western_1.wav"
RUTA_MUSICA_JUEGO = "GauchoDefense/assets/sounds/musica_western_1.wav"

# Tamaños
GAUCHO_SIZE = (111, 120)
ZOMBIE_SIZE = (91, 120)
BALA_SIZE   = (15, 5)

# Gameplay
COOLDOWN_DISPARO = 500   # ms mínimo entre disparos
ZOMBIE_SPEED = 4
BALA_SPEED = 15

# ENEMIGOS
SPAWN_TIEMPO = 1000
SPAWN_DISPONIBLES = [50, 150, 250, 350, 450] # cambiar por random

