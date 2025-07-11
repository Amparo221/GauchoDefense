import pygame, sys
from menu import mostrar_menu
from ui.ranking import mostrar_ranking
from ui.intro import mostrar_introduccion
from game.utils import mostrar_creditos
from game.ejecutar_juego import iniciar_juego
from assets.assets import cargar_assets
from game.audio import inicializar_audio, cargar_sonido, cambiar_musica, play_click
from config import *


def main() -> None:
    """
    Inicializa el juego:
    - Carga el sonido
    - Carga la Pantalla
    - Muestra el menú
    - En el bucle principal, define los escenarios:
    1. Jugar
    2. Ranking
    3. Créditos
    4. Salir
    5. Opción inválida (Manejo de errores -> Vuelve al menú)
    """
    pygame.init()
    inicializar_audio() 
    sonido = cargar_sonido()

    assets = cargar_assets()
    pantalla = assets["pantalla"]

    cambiar_musica("menu")  

    ejecucion = True
    while ejecucion:
        accion = mostrar_menu(assets, sonido) 

        if accion == "jugar":
            play_click(sonido)
            mostrar_introduccion(pantalla)
            cambiar_musica("juego")
            iniciar_juego(assets)
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
            print(f"Opción inválida ({accion}), regresando al menú...")
            pygame.time.delay(500)


if __name__ == "__main__":
    main()