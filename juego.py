import pygame, sys
from jugador     import movimiento_jugador, disparar_balas, crear_balas, generar_animaciones
from enemigos   import spawn_zombie, mover_zombies, detectar_colisiones, verificar_choque_con_jugador
from ranking    import agregar_puntuacion
from utils      import pedir_nombre_jugador
from config import *
from renderer import dibujar_fondo, dibujar_hud, dibujar_enemigos
from ranking import mostrar_ranking

MODE_QUIT = "quit"
MODE_MENU = "menu"

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

def procesar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return MODE_QUIT
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            return MODE_MENU

def actualizar_juego(estado, assets):
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
        lista_enemigos = estado["enemigos"]
    )

    # Colisiones zombie-jugador = restar vidas
    player_rect = pygame.Rect(
        estado["jugador"]["x"],
        estado["jugador"]["y"],
        *GAUCHO_SIZE
    )
    estado["vidas"] = verificar_choque_con_jugador(
        player_rect,
        estado["vidas"],
        lista_enemigos = estado["enemigos"]
    )

    # Si se queda sin vidas, marca Game Over y sale
    if estado["vidas"] <= 0:
        estado["flags"]["game_over"] = True
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
        cooldown         = COOLDOWN_DISPARO,
        jugador_x        = estado["jugador"]["x"],
        jugador_y        = estado["jugador"]["y"],
        jugador_size     = GAUCHO_SIZE,
        ancho_pantalla   = ANCHO
    )
    estado["tiempos"]["ultimo_disparo"] = ultimo_tiro
    estado["flags"]["disparar"]         = disparar_flag



def renderizar_juego(pantalla, estado, assets):
    # crear_fondo, crear_balas, animaciones, dibujar_zombies, HUD…
    # fondo infinito
    dibujar_fondo(pantalla, assets["fondo"], assets["ancho_fondo"], assets["altura_fondo"])

    crear_balas(pantalla, estado.get("balas", []), assets["bala_img"])

    dp_playing, dp_start = generar_animaciones(
    pantalla             = pantalla,
    jugador_img          = assets["gaucho"],
    disparar_flag        = estado["flags"]["disparar"],
    tiempo_actual        = pygame.time.get_ticks(),
    anim_disparo         = assets["disparo"],
    duracion_disparo     = 400,
    en_movimiento        = estado["jugador"]["en_movimiento"],
    anim_caminar         = assets["caminar"],
    pos_x                = estado["jugador"]["x"],
    pos_y                = estado["jugador"]["y"],
    disparo_playing      = estado["flags"]["disparo_playing"],
    disparo_start_time   = estado["tiempos"]["tiempo_inicio_disparo"],
    sonido_disparo       = assets["sonido_disparo"] # sonido del diparo en la animación, ya que probé ejecutar el sonido despues de llamar a la funcion disparar_balas y se ejecutaba antes de que se dibuje el disparo, osea mucho delay
    )
    estado["flags"]["disparo_playing"]      = dp_playing
    estado["tiempos"]["tiempo_inicio_disparo"] = dp_start
    
    # dibujar zombies
    dibujar_enemigos(pantalla, estado["enemigos"])

    # HUD
    dibujar_hud(pantalla, estado["puntuacion"], estado["vidas"])
    
    pygame.display.flip()

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

def iniciar_juego(assets):
    pantalla = assets["pantalla"]
    clock = pygame.time.Clock()
    estado = crear_estado_inicial()      

    # Musica de fondo
    pygame.mixer.music.load(assets["musica_juego"])
    pygame.mixer.music.set_volume(0.1)     # volumen (0.0 a 1.0)
    pygame.mixer.music.play(-1)            # -1 = bucle infinito 
    
    modo = None

    while estado["flags"]["ejecucion"]:
        modo = procesar_eventos()
        if modo == "quit":   
            pygame.quit()
            sys.exit()
        if modo == "menu":   
            return

        # logica del juego
        actualizar_juego(estado, assets)
        if estado["flags"]["game_over"]: 
            pygame.mixer.music.fadeout(1000)
            accionar_game_over(pantalla, estado)
            return

        renderizar_juego(pantalla, estado, assets)
        clock.tick(60)

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()