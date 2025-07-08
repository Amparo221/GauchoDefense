import pygame
from menu import *
from ranking import mostrar_ranking
from utils import mostrar_creditos
from juego import iniciar_juego
from assets import cargar_assets


def main():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=64)
    pygame.init()

    ejecucion = True

    assets = cargar_assets()

    while ejecucion:
        accion = mostrar_menu() 

        if accion == "jugar":
            iniciar_juego(assets) # si hago return acá adentro

        elif accion == "ranking":
            mostrar_ranking(pantalla)
            pygame.time.delay(1000)

        elif accion in ("créditos", "creditos"):
            mostrar_creditos(pantalla)
            pygame.time.delay(1000)

        elif accion == "salir":
            pygame.quit()
            sys.exit()

        else:
            # Si ocurre algo sin manejar volver al menú por default
            print(f"Opción inválida ({accion}), regresando al menú...")
            pygame.time.delay(500)


if __name__ == "__main__":
    main()