from config import *
from game.utils import pedir_nombre_jugador
from ui.ranking import agregar_puntuacion, mostrar_ranking


# Define un diccionario con el estado inicial del juego 
def crear_estado_inicial():
    '''
    Crea y devuelve un diccionario con el estado inicial del juego.
    Contiene:
    - jugador: posición, velocidad y estado de movimiento.
    - balas: lista de balas disparadas.
    - enemigos: lista de enemigos (zombies).
    - tiempos: último spawn de enemigos y último disparo.
    - flags: indicadores de estado del juego (game_over, ejecucion, disparar).
    - puntuacion: puntuacion inicial del jugador.
    - vidas: número de vidas iniciales del jugador.'''
    return {
        "jugador": {
            "x":0,
            "y":0,
            "velocidad_movimiento":5, 
            "en_movimiento": False
        },
        "balas": [],
        "enemigos": [],
        "tiempos": {
            "ultimo_spawn":0, 
            "ultimo_disparo":0,
            "tiempo_inicio_disparo": 0
        },
        "flags":  {
            "game_over": False, 
            "ejecucion": True, 
            "disparar": False,
            "disparo_playing": 0
        },
        "puntuacion":  0,
        "vidas":  3
    }

def accionar_game_over(pantalla, estado):
    # muestra “Perdiste”, pide nombre con pedir_nombre_jugador(),
    # agregar_puntuacion(name, estado["puntuacion"])
    # pantalla de game over
    pantalla.fill(NEGRO)
    texto_partida_perdida = FONT_TITLE.render('Perdiste, Canejo', True, BLANCO)
    pantalla.blit(texto_partida_perdida, texto_partida_perdida.get_rect(center=(ANCHO//2, ALTO//2 - 50)))
    pygame.display.flip()
    pygame.time.delay(3000)

    # pedir nombre y guardar score
    name = pedir_nombre_jugador(pantalla)
    agregar_puntuacion(name, estado["puntuacion"])
    mostrar_ranking(pantalla)