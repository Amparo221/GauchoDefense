from game.utils import pedir_nombre_jugador
from ui.ranking import agregar_puntuacion, mostrar_ranking
from ui.renderer import dibujar_game_over

def crear_estado_inicial() -> dict:
    """
    Crea y devuelve un diccionario con el estado inicial del juego.
    Contiene:
    - jugador: posición, velocidad y estado de movimiento.
    - balas: lista de balas disparadas.
    - enemigos: lista de enemigos (zombies).
    - tiempos: último spawn de enemigos y último disparo.
    - flags: indicadores de estado del juego (game_over, ejecucion, disparar).
    - puntuacion: puntuacion inicial del jugador.
    - vidas: número de vidas iniciales del jugador.
    - datos para la transicion del fondo

    Returns:
        dict {
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
        "vidas":  3,
        "fondo_x": 0,
        "fondo_actual": "fondo",
        "ultimo_cambio_fondo": 0
    }
    """
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
        "vidas":  3,
        "fondo_x": 0,
        "fondo_actual": "fondo_juego",
        "ultimo_cambio_fondo": 0
    }

def accionar_game_over(pantalla, estado, assets):
    '''Muestra la pantalla de Game Over y guarda la puntuación del jugador.'''
    dibujar_game_over(pantalla, assets["fuentes"]["fuente_grande"])
    agregar_puntuacion(pedir_nombre_jugador(pantalla, assets["fuentes"]["fuente_jugador"]), estado["puntuacion"])
    mostrar_ranking(pantalla, assets)