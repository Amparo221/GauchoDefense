import pygame, sys
from ui.menu import mostrar_menu
from ui.ranking import mostrar_ranking
from ui.intro import mostrar_introduccion
from game.utils import mostrar_creditos
from game.ejecutar_juego import iniciar_juego
from assets.assets import cargar_assets
from game.audio import inicializar_audio, cargar_sonido, cambiar_musica, play_click
import config


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
    pantalla = pygame.display.set_mode((config.ANCHO, config.ALTO))

    assets = cargar_assets()

    cambiar_musica("menu")  

    ejecucion = True
    while ejecucion:
        accion = mostrar_menu(pantalla, assets, sonido) 

        if accion == config.MODE_JUGAR:
            play_click(sonido)
            mostrar_introduccion(pantalla, assets)
            cambiar_musica("juego")
            # Arranca el juego
            iniciar_juego(assets, sonido, pantalla)
            # Reproduce música del menú
            cambiar_musica(config.MODE_MENU)

        elif accion == config.MODE_RANKING:
            play_click(sonido)
            mostrar_ranking(pantalla, assets)
            pygame.time.delay(250)

        elif accion == config.MODE_CREDITOS:
            play_click(sonido)
            mostrar_creditos(pantalla, assets)
            pygame.time.delay(250)

        elif accion == config.MODE_SALIR:
            play_click(sonido)
            pygame.time.delay(1300)
            pygame.quit()
            sys.exit()

        else:
            print(f"Opción inválida ({accion}), regresando al menú...")
            pygame.time.delay(500)


if __name__ == "__main__":
    main()