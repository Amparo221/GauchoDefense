# src/audio.py
import pygame
from config import *

def inicializar_audio():
    """
    Inicializa el mixer de Pygame 
    Llamar una sola vez al arrancar la app.
    """
    pygame.mixer.init(
        frequency=AUDIO_FREQ,
        size=AUDIO_SIZE,
        channels=AUDIO_CHANS,
        buffer=AUDIO_BUFFER
    )

def cargar_sonido():
    """
    Carga y devuelve un dict con todos los efectos que vas a usar.
    """
    sonidos = {
        "disparo": pygame.mixer.Sound(RUTA_SONIDO_DISPARO),
        "menu_click": pygame.mixer.Sound(RUTA_SONIDO_MENU_CLICK),
        "hit_zombie": pygame.mixer.Sound(SONIDO_HIT_ZOMBIE),
        "hurt_gaucho": pygame.mixer.Sound(SONIDO_HURT_GAUCHO),
        "game_over": pygame.mixer.Sound(SONIDO_GAME_OVER)
    }
    # Ajustar volúmenes desde config.SFX_VOLUME
    for clave, sound in sonidos.items():
        vol = SFX_VOLUME.get(clave, 1.0)
        sound.set_volume(vol)
    return sonidos

def reproducir_sonido(sounds_dict, clave):
    """
    Reproduce uno de los efectos pre-cargados.
      sounds_dict: dict devuelto por load_sounds()
      key: "disparo", "menu_click"
    """
    s = sounds_dict.get(clave)
    if s:
        s.play()


def reproducir_musica(path, loops=-1, start=0.0, volume=1.0, fade_ms=0):
    """
    Carga y reproduce música de fondo.
    
    Parámetros:
    - path: ruta al archivo de música (string).
    - loops: -1 para bucle infinito, 0 para una sola vez, >0 repeticiones.
    - start: segundo (float) desde donde empezar.
    - volumen: float 0.0–1.0.
    - fade_ms: fade-in en milisegundos.
    """
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=loops, start=start, fade_ms=fade_ms)

def detener_musica(fade_ms=0):
    """
    Detiene la música actual. Si fade_ms>0, hace fade-out.
    """
    if fade_ms:
        pygame.mixer.music.fadeout(fade_ms)
    else:
        pygame.mixer.music.stop()

# Ajusta en caliente el volumen de un efecto específico
def set_volumen_sonido(sounds_dict, clave, volumen):
    s = sounds_dict.get(clave)
    if s:
        s.set_volume(volumen)

# Ajusta en caliente el volumen de la música
def set_volumen_musica(volumen: float):
    pygame.mixer.music.set_volume(volumen)
