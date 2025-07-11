# src/audio.py
import pygame
from config import *

def inicializar_audio() -> None:
    """
    Inicializa el mixer de Pygame.
    Llamar una sola vez al arrancar la app.
    """
    pygame.mixer.init(
        frequency=AUDIO_FREQ,
        size=AUDIO_SIZE,
        channels=AUDIO_CHANS,
        buffer=AUDIO_BUFFER
    )

def play_click(sonido: dict, delay_ms=250) -> None:
    """
    Recibe diccionario de sonidos.
    Invoca el sonido de click.
    
    Args:
        sonido: dict
        delay_ms: int
    """
    reproducir_sonido(sonido, "menu_click")
    pygame.time.delay(delay_ms)

def cambiar_musica(modo: str) -> None:
    """
    Recibe el modo del juego: menu o juego.
    Detiene la que esté sonando y arranca la nueva con fade.

    Args:
        modo: str
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

def cargar_sonido() -> dict:
    """
    Carga y devuelve un diccionario con todos los efectos a usar.

    Returns:
        dict{
        "disparo": pygame.mixer.Sound(n),
        "menu_click": pygame.mixer.Sound(n),
        "hit_zombie": pygame.mixer.Sound(n),
        "hurt_gaucho": pygame.mixer.Sound(n),
        "game_over": pygame.mixer.Sound(n)
    }
    """
    sonidos = {
        "disparo": pygame.mixer.Sound(RUTA_SONIDO_DISPARO),
        "menu_click": pygame.mixer.Sound(RUTA_SONIDO_MENU_CLICK),
        "hit_zombie": pygame.mixer.Sound(SONIDO_HIT_ZOMBIE),
        "hurt_gaucho": pygame.mixer.Sound(SONIDO_HURT_GAUCHO),
        "game_over": pygame.mixer.Sound(SONIDO_GAME_OVER)
    }

    for clave, sound in sonidos.items():
        vol = SFX_VOLUME.get(clave, 1.0)
        sound.set_volume(vol)
    return sonidos

def reproducir_sonido(sounds_dict: dict, clave: str) -> None:
    """
    Recibe un diccionario de sonidos (sounds_dict) y una cadena (clave) que indica qué sonido se quiere reproducir.

    Args:
        sounds_dict: dict
        clave: str
    """
    s = sounds_dict.get(clave)
    if s:
        s.play()


def reproducir_musica(ruta: str, volume: float, fade_ms: int, loops=-1) -> None:
    """
    Recibe ruta, volumen y fadeout.
    Invoca la reproducción de la musica.

    Args:
        ruta: str
        volume: float
        fade_ms: int
        loops: int
    """
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=loops, fade_ms=fade_ms)

def detener_musica(fade_ms: int) -> None:
    """
    Recibe fadeout.
    Invoca la parada de la musica.

    Args:
        fade_ms: int
    """
    pygame.mixer.music.fadeout(fade_ms)

def toggle_music(paused: bool, mode: str ="menu") -> bool:
    """
    Si paused==False: pausa la música de fondo y devuelve True.
    Si paused==True: reanuda (o carga) la música según el modo y devuelve False.
    mode: 'menu' (by default) o 'game'
    Si mode=='menu', pausa la musica de juego y carga la de menu.
    Si mode=='game', pausa la musica de menu y carga la de juego.

    Args:
        paused: bool
        mode: str
    Returns:
        bool
    """
    if not paused:
        if mode == "menu":
            detener_musica(VOLUMEN_MUSIC_MENU["fade_ms"])
        else:
            detener_musica(VOLUMEN_MUSIC_JUEGO["fade_ms"])
        return True

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
