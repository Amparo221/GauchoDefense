import pygame, sys
from config import *
from game.audio import reproducir_musica, cargar_sonido
from game.state import crear_estado_inicial, accionar_game_over
from game.input_handler import procesar_eventos
from game.update import actualizar_juego
from game.render import renderizar_juego

def iniciar_juego(assets: dict) -> None:
    """
    Recibe diccionario de assets.
    Inicializa la musica y activa la actualizacion constante de estado del juego.
    Invoca la renderizacion del juego.
    Args:
        assets: dict
    """
    pantalla = assets["pantalla"]
    clock = pygame.time.Clock()
    estado = crear_estado_inicial()     
    sonido = cargar_sonido()

    reproducir_musica(RUTA_MUSICA_JUEGO, volume=VOLUMEN_MUSIC_JUEGO["volumen"], fade_ms=VOLUMEN_MUSIC_JUEGO["fade_ms"]) 
    
    modo = None

    while estado["flags"]["ejecucion"]:
        modo = procesar_eventos()
        if modo == "quit":   
            pygame.quit()
            sys.exit()
        if modo == "menu":   
            return

        actualizar_juego(estado, assets, sonido)
        if estado["flags"]["game_over"]: 
            pygame.mixer.music.fadeout(1000)
            accionar_game_over(pantalla, estado)
            return

        renderizar_juego(pantalla, estado, assets)
        clock.tick(60)


