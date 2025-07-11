import pygame
from ui.renderer import dibujar_fondo_juego, dibujar_hud, dibujar_enemigos
from entities.jugador import crear_balas, generar_animaciones

def renderizar_juego(pantalla, estado, assets):
    # crear_fondo, crear_balas, animaciones, dibujar_zombies, HUD…
    if estado["puntuacion"] // 5 > estado["ultimo_cambio_fondo"]:
        fondos                        = ["fondo_juego", "fondo_noche"]
        idx_actual                        = fondos.index(estado["fondo_actual"])
        idx_nuevo                         = (idx_actual + 1) % len(fondos)
        estado["fondo_actual"]        = fondos[idx_nuevo]
        estado["ultimo_cambio_fondo"] = estado["puntuacion"] // 5

    fondo_usado = assets["imagenes"][estado["fondo_actual"]] 
    dibujar_fondo_juego(pantalla, fondo_usado, assets["imagenes"]["ancho_fondo_juego"], assets["imagenes"]["alto_fondo_juego"], estado)

    crear_balas(pantalla, estado.get("balas", []), assets["sprites"]["bala_img"])

    dp_playing, dp_start = generar_animaciones(
    pantalla             = pantalla,
    jugador_img          = assets["sprites"]["gaucho"],
    disparar_flag        = estado["flags"]["disparar"],
    tiempo_actual        = pygame.time.get_ticks(),
    anim_disparo         = assets["sprites"]["disparo"],
    duracion_disparo     = 400,
    en_movimiento        = estado["jugador"]["en_movimiento"],
    anim_caminar         = assets["sprites"]["caminar"],
    pos_x                = estado["jugador"]["x"],
    pos_y                = estado["jugador"]["y"],
    disparo_playing      = estado["flags"]["disparo_playing"],
    disparo_start_time   = estado["tiempos"]["tiempo_inicio_disparo"]
    )
    estado["flags"]["disparo_playing"]      = dp_playing
    estado["tiempos"]["tiempo_inicio_disparo"] = dp_start
    
    # dibujar zombies
    dibujar_enemigos(pantalla, estado["enemigos"])

    # HUD
    dibujar_hud(pantalla, assets["fuentes"]["fuente_hud"], estado["puntuacion"], estado["vidas"])
    
    pygame.display.flip()