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
FONT_HUD      = pygame.font.SysFont(None, 36)
FONT_TITLE    = pygame.font.SysFont(None, 48)

# Sonidos
SONIDO_CLICK = "assets/sounds/click.ogg"
RUTA_SONIDO_DISPARO = "assets/sounds/disparo_western_1.wav"
RUTA_MUSICA_JUEGO = "assets/sounds/musica_western_1.wav"

# Tamaños
GAUCHO_SIZE = (111, 120)
ZOMBIE_SIZE = (100, 100)
BALA_SIZE   = (15, 5)

# Gameplay
COOLDOWN_DISPARO = 400   # ms mínimo entre disparos
ZOMBIE_SPEED = 4
GAUCHO_SPEED = 5

# Rutas a assets
RUTA_FONDO           =  "assets/fondo.png"
RUTA_GAUCHO          =  "assets/gaucho.png"
RUTA_ZOMBIE_1        =  "assets/sprite_zombie_2.gif"
RUTA_CAMINAR         =  "assets/caminar_3.gif"
RUTA_DISPARO         =  "assets/disparo_4.gif"
RUTA_ZOMBIE_MUERTO   =  "assets/zombie_muerto.png"

# Archivos de datos
RANKING_PATH = "data/ranking.json"

# ENEMIGOS
SPAWN_TIEMPO = 1000
SPAWN_DISPONIBLES = [50, 150, 250, 350, 450] # cambiar por random

