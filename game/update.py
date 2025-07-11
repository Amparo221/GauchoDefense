import pygame
from entities.jugador import (movimiento_jugador, disparar_balas)
from entities.enemigos import (spawn_zombie, mover_zombies, detectar_colisiones, verificar_choque_con_jugador, remover_zombies_muertos)
import config
from game.audio import reproducir_sonido

def actualizar_juego(estado: dict, assets: dict, sonido: dict) -> None:
    """
    Recibe tres diccionarios: estado, assets y sonido.
    Actualiza una iteración de juego:
      1. Trackea tiempo  mueve enemigos.
      2. Si se escapa por la izquierda, pierde vida.
      3. Invoca la deteccion de colisiones.
      4. Remueve enemigos muertos.
      5. Mueve al jugador y invoca el disparo de balas.
      6. Marca game_over si vidas <= 0.
      7. Actualiza la puntuacion.

    Args:
        estado: dict
        assets: dict
        sonido: dict
    """
    tiempo_actual = pygame.time.get_ticks()

    estado["tiempos"]["ultimo_spawn"] = spawn_zombie(
        tiempo_actual,
        estado["tiempos"]["ultimo_spawn"],
        estado["enemigos"],
        assets
    )

    mover_zombies(estado["enemigos"])

    for z in estado["enemigos"][:]:
        if z["rect"].right < 0:
            estado["enemigos"].remove(z)
            estado["vidas"] -= 1

    estado["puntuacion"] = detectar_colisiones(
        balas = estado["balas"],
        puntuacion = estado["puntuacion"],
        lista_enemigos = estado["enemigos"],
        zombie_muerto_img=assets["sprites"]["zombie_muerto"],
        tiempo_ahora = tiempo_actual,
        sonido_hit = sonido
    )

    remover_zombies_muertos(estado["enemigos"], tiempo_actual)

    player_rect = pygame.Rect(
        estado["jugador"]["x"],
        estado["jugador"]["y"],
        *config.GAUCHO_SIZE
    )
    estado["vidas"] = verificar_choque_con_jugador(
        player_rect,
        estado["vidas"],
        lista_enemigos = estado["enemigos"],
        sonido_hurt_gaucho = sonido
    )

    if estado["vidas"] <= 0:
        estado["flags"]["game_over"] = True
        reproducir_sonido(sonido, "game_over")
        return

    estado["jugador"]["y"], estado["jugador"]["en_movimiento"] = movimiento_jugador(
        estado["jugador"]["y"],
        estado["jugador"]["velocidad_movimiento"],
    )

    ultimo_tiro, disparar_flag = disparar_balas(
        lista_de_balas   = estado["balas"],
        tiempo_actual    = tiempo_actual,
        ultimo_disparo   = estado["tiempos"]["ultimo_disparo"],
        jugador_x        = estado["jugador"]["x"],
        jugador_y        = estado["jugador"]["y"],
        sonido_disparo   = sonido
    )
    estado["tiempos"]["ultimo_disparo"] = ultimo_tiro
    estado["flags"]["disparar"]         = disparar_flag