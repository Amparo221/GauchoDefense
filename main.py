import pygame, sys
from menu import mostrar_menu
from ui.ranking import mostrar_ranking
from game.utils import mostrar_creditos
from game.ejecutar_juego import iniciar_juego
from assets.assets import cargar_assets
from game.audio import inicializar_audio, cargar_sonido, cambiar_musica, play_click
from config import *


def main():
    pygame.init()
    inicializar_audio()  # Inicializa el mixer de Pygame
    sonido = cargar_sonido()

    assets = cargar_assets()
    pantalla = assets["pantalla"]

    cambiar_musica("menu")  # Arranca música del menú

    ejecucion = True
    while ejecucion:
        accion = mostrar_menu(assets, sonido) 

        if accion == "jugar":
            play_click(sonido)
            cambiar_musica("juego")
            # Arranca el juego
            iniciar_juego(assets)
            # Reproduce música del menú
            cambiar_musica("menu")

        elif accion == "ranking":
            play_click(sonido)
            mostrar_ranking(pantalla)
            pygame.time.delay(250)

        elif accion in ("créditos", "creditos"):
            play_click(sonido)
            mostrar_creditos(pantalla)
            pygame.time.delay(250)

        elif accion == "salir":
            play_click(sonido)
            pygame.time.delay(1300)
            pygame.quit()
            sys.exit()

        else:
            # Si ocurre algo sin manejar volver al menú por default
            print(f"Opción inválida ({accion}), regresando al menú...")
            pygame.time.delay(500)


if __name__ == "__main__":
    main()