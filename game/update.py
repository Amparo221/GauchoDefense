import pygame
from entities.jugador import (movimiento_jugador, disparar_balas)
from entities.enemigos import (spawn_zombie, mover_zombies, detectar_colisiones, verificar_choque_con_jugador, remover_zombies_muertos)
from config import (ANCHO, ALTO, GAUCHO_SIZE)
from game.audio import reproducir_sonido

def actualizar_juego(estado, assets, sonido):
    """
    Actualiza una iteración de juego:
      1. Genera y mueve enemigos.
      2. Detecta y descuenta vidas por escapes y colisiones.
      3. Mueve al jugador y dispara balas.
      4. Marca game_over si vidas <= 0.
    """
    tiempo_actual = pygame.time.get_ticks()

    # Spawn y movimiento de zombies
    estado["tiempos"]["ultimo_spawn"] = spawn_zombie(
        tiempo_actual,
        estado["tiempos"]["ultimo_spawn"],
        ANCHO,
        estado["enemigos"],
        assets["zombie_img"]
    )

    # Mover zombies
    mover_zombies(estado["enemigos"])

    # Si los zombies que escapan = restar vidas
    for z in estado["enemigos"][:]:
        if z["rect"].right < 0:
            estado["enemigos"].remove(z)
            estado["vidas"] -= 1

    # Colisiones bala-zombie = sumar puntuacion
    estado["puntuacion"] = detectar_colisiones(
        balas = estado["balas"],
        puntuacion = estado["puntuacion"],
        lista_enemigos = estado["enemigos"],
        zombie_muerto_img=assets["zombie_muerto"],
        tiempo_ahora = tiempo_actual,
        sonido_hit = sonido
    )

    remover_zombies_muertos(estado["enemigos"], tiempo_actual)

    # Colisiones zombie-jugador = restar vidas
    player_rect = pygame.Rect(
        estado["jugador"]["x"],
        estado["jugador"]["y"],
        *GAUCHO_SIZE
    )
    estado["vidas"] = verificar_choque_con_jugador(
        player_rect,
        estado["vidas"],
        lista_enemigos = estado["enemigos"],
        sonido_hurt_gaucho = sonido
    )

    # Si se queda sin vidas, marca Game Over y sale
    if estado["vidas"] <= 0:
        estado["flags"]["game_over"] = True
        reproducir_sonido(sonido, "game_over")
        return

    # Movimiento del jugador (W/S)
    estado["jugador"]["y"], estado["jugador"]["en_movimiento"] = movimiento_jugador(
        estado["jugador"]["y"],
        estado["jugador"]["velocidad_movimiento"],
        ALTO
    )

    # Disparo de balas (space + cooldown)
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