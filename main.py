import pygame, sys
from menu import *
from ranking import mostrar_ranking
from utils import mostrar_creditos
from juego import iniciar_juego
from assets import cargar_assets
from audio import inicializar_audio, reproducir_musica, cargar_sonido, detener_musica, reproducir_sonido
from config import *


def main():
    pygame.init()
    inicializar_audio()  # Inicializa el mixer de Pygame
    sonido = cargar_sonido()

    reproducir_musica(RUTA_MUSICA_MENU, volume=VOLUMEN_MUSIC_MENU["volumen"], fade_ms=VOLUMEN_MUSIC_MENU["fade_ms"])  # Reproduce música del menú
    
    ejecucion = True

    assets = cargar_assets()
    pantalla = assets["pantalla"]

    while ejecucion:
        accion = mostrar_menu() 

        if accion == "jugar":
            detener_musica(VOLUMEN_MUSIC_MENU["fade_ms"])  # Detiene música del menú
            reproducir_sonido(sonido, "menu_click")
            # Arranca el juego
            iniciar_juego(assets)
            # Reproduce música del menú
            reproducir_musica(RUTA_MUSICA_MENU, volume=VOLUMEN_MUSIC_MENU["volumen"], fade_ms=VOLUMEN_MUSIC_MENU["fade_ms"])  


        elif accion == "ranking":
            reproducir_sonido(sonido, "menu_click")
            mostrar_ranking(pantalla)
            pygame.time.delay(250)

        elif accion in ("créditos", "creditos"):
            reproducir_sonido(sonido, "menu_click")
            mostrar_creditos(pantalla)
            pygame.time.delay(250)

        elif accion == "salir":
            reproducir_sonido(sonido, "menu_click")
            pygame.time.delay(1300)
            pygame.quit()
            sys.exit()

        else:
            # Si ocurre algo sin manejar volver al menú por default
            print(f"Opción inválida ({accion}), regresando al menú...")
            pygame.time.delay(500)


if __name__ == "__main__":
    main()