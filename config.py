import pygame

# Pantalla
ANCHO, ALTO = 1000, 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS   = ( 50,  50,  50)
COLOR_HOVER = (200, 200, 200)

# Rutas a assets
RUTA_FONDO_JUEGO         = "assets/images/fondo_5.png"
RUTA_FONDO_JUEGO_NOCHE   = "assets/images/fondo_7_noche.png"
RUTA_FONDO_MENU          = "assets/images/fondo_menu.png"
RUTA_GAUCHO              = "assets/images/gaucho.png"
RUTA_ZOMBIE_1            = "assets/images/sprite_zombie.gif"
RUTA_ZOMBIE_FUERTE       = "assets/images/zombie_fuerte_0.gif"
RUTA_ZOMBIE_HERIDO       = "assets/images/zombie_herido_0.gif"
RUTA_CAMINAR             = "assets/images/caminar.gif"
RUTA_DISPARO             = "assets/images/disparo.gif"
RUTA_FUENTE              = "assets/fonts/Jersey10-Regular.ttf"
RUTA_ZOMBIE_MUERTO       = "assets/images/zombie_muerto.png"

# Fuentes
pygame.font.init()
FUENTE_GRANDE = pygame.font.Font(RUTA_FUENTE, 40)
FUENTE_MEDIANA = pygame.font.Font(RUTA_FUENTE, 30)
FUENTE_TITULO_PRINCIPAL = pygame.font.Font(RUTA_FUENTE, 80)
FONT_HUD      = pygame.font.Font(RUTA_FUENTE, 36)
FONT_TITLE    = pygame.font.Font(RUTA_FUENTE, 48)

# Rutas de audio
SONIDO_CLICK = "assets/sounds/click.ogg"
RUTA_SONIDO_DISPARO = "assets/sounds/disparo_western_2.wav"
RUTA_MUSICA_JUEGO = "assets/music/musica_juego_PorMilonga.mp3"
RUTA_MUSICA_MENU = "assets/music/musica_menu_milonga.mp3"
RUTA_SONIDO_MENU_CLICK = "assets/sounds/disparo_western_2.wav"
SONIDO_HIT_ZOMBIE = "assets/sounds/zombie_hit.wav"
SONIDO_HURT_GAUCHO = "assets/sounds/hurt_gaucho.ogg"
SONIDO_GAME_OVER = "assets/sounds/game_over_1.wav"

# Configuracion de audio
AUDIO_BUFFER = 256     # menor = menor latencia (pero más CPU)
AUDIO_FREQ   = 44100   # frecuencia de muestreo
AUDIO_SIZE   = -16     # 16 bits signed
AUDIO_CHANS  = 2       # estéreo
VOLUMEN_MUSIC_MENU = {"volumen": 0.2, "fade_ms": 1000}  # volumen de la música del menú y fade-out al cambiar de pantalla
VOLUMEN_MUSIC_JUEGO = {"volumen": 0.3, "fade_ms": 1000}  # volumen de la música del gameplay y fade-out al game over
SFX_VOLUME = {
    "disparo":    0.5,
    "menu_click": 0.2,
    "hit_zombie": 0.4,
    "hurt_gaucho": 0.5,
    "game_over": 0.7
}

# Tamaños
GAUCHO_SIZE = (111, 120)
ZOMBIE_SIZE = (100, 100)
BALA_SIZE   = (15, 5)
FONDO_SIZE = (ANCHO, ALTO)

# Gameplay
COOLDOWN_DISPARO = 500   # ms mínimo entre disparos
ZOMBIE_SPEED = 2
GAUCHO_SPEED = 5
BACKGROUND_SPEED = 2

# Archivos de datos
RANKING_PATH = "data/ranking.json"
BALA_SPEED = 15

# ENEMIGOS
SPAWN_TIEMPO = 1000
SPAWN_DISPONIBLES = [50, 150, 250, 350, 450] # cambiar por random

# Menu
MODE_QUIT = "quit"
MODE_MENU = "menu"

