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

# Estos 2 helpers los agregué para quitar logica de main.
def play_click(sonido, delay_ms=250):
    reproducir_sonido(sonido, "menu_click")
    pygame.time.delay(delay_ms)

def cambiar_musica(modo):
    """
    modo: 'menu' o 'game'
    Detiene la que esté sonando y arranca la nueva con fade.
    """
    if modo == "menu":
        pygame.mixer.music.fadeout(VOLUMEN_MUSIC_JUEGO["fade_ms"])
        reproducir_musica(
            RUTA_MUSICA_MENU,
            volume=VOLUMEN_MUSIC_MENU["volumen"],
            fade_ms=VOLUMEN_MUSIC_MENU["fade_ms"]
        )
    elif modo == "juego":
        pygame.mixer.music.fadeout(VOLUMEN_MUSIC_MENU["fade_ms"])
        reproducir_musica(
            RUTA_MUSICA_JUEGO,
            volume=VOLUMEN_MUSIC_JUEGO["volumen"],
            fade_ms=VOLUMEN_MUSIC_JUEGO["fade_ms"]
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


def reproducir_musica(ruta, volume, fade_ms, loops=-1):
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=loops, fade_ms=fade_ms)

def detener_musica(fade_ms):
    pygame.mixer.music.fadeout(fade_ms)

def toggle_music(paused, mode="menu"):
    """
    Si paused==False: pausa la música de fondo y devuelve True.
    Si paused==True: reanuda (o carga) la música según el modo y devuelve False.
    mode: 'menu' o 'game'
    """
    if not paused:
        # pausar
        if mode == "menu":
            detener_musica(VOLUMEN_MUSIC_MENU["fade_ms"])
        else:
            detener_musica(VOLUMEN_MUSIC_JUEGO["fade_ms"])
        return True

    # reanudar / arrancar según modo
    if mode == "menu":
        reproducir_musica(
            RUTA_MUSICA_MENU,
            volume=VOLUMEN_MUSIC_MENU["volumen"],
            fade_ms=VOLUMEN_MUSIC_MENU["fade_ms"]
        )
    else:
        reproducir_musica(
            RUTA_MUSICA_JUEGO,
            volume=VOLUMEN_MUSIC_JUEGO["volumen"],
            fade_ms=VOLUMEN_MUSIC_JUEGO["fade_ms"]
        )
    return False
