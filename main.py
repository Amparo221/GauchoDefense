import pygame, gif_pygame
from pygame.locals import *
from jugador import *
from menu import *
from config import *
from enemigos import *
from ranking import mostrar_ranking, add_score
from utils import pedir_nombre_jugador, mostrar_creditos

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
fondo = pygame.image.load("assets/fondo.png").convert()
ancho_fondo, altura_fondo = fondo.get_size()  

gaucho = pygame.image.load("assets/gaucho.png").convert_alpha()
gaucho_size=(111,120)
gaucho = pygame.transform.scale(gaucho, gaucho_size)


caminar = gif_pygame.load("assets/caminar_3.gif")
disparo = gif_pygame.load("assets/disparo_4.gif")

tecla_presionada = pygame.key.get_pressed()

# BALAS
bala_img = pygame.Surface((15, 5))  
bala_img.fill(NEGRO) 
balas = []  #Lista pa las balas 
cooldown = 400  



disparo_playing = False
disparo_start_time = 0
disparo_duration = 400  



def crear_fondo():
    for y in range(0, pantalla.get_height(), altura_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))









#LAAAA
def iniciar_juego():
    disparo_playing = False
    disparo_start_time = 0
    disparo_duracion = 400


    ultimo_spawn = 0
    puntaje = 0
    vidas = 3
    


    # Posición y estado inicial del gaucho
    gaucho_x = 0
    gaucho_y = 0
    gaucho_velocidad = 5
    gaucho_rect = pygame.Rect(gaucho_x, gaucho_y, *gaucho_size)

    ultimo_disparo = 0  

    
    disparar = False

    is_moving = False
    disparar = False

    running = True
    game_over = False
    reloj = pygame.time.Clock()

    while running:

        tiempo_actual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                running = False

        if game_over:
            pantalla.fill((0, 0, 0))
            texto_partida_perdida = fuente.render(f'Perdiste, Canejo', True, (255, 255, 255))
            pantalla.blit(texto_partida_perdida, (300, 250))
            pygame.display.flip()
            pygame.time.delay(5000)

            nombre_jugador = pedir_nombre_jugador(pantalla)
            add_score(nombre_jugador, puntaje)
            mostrar_ranking(pantalla)

            # Salir del loop y volver al menú
            running = False
            continue


        ultimo_spawn = spawn_zombie(tiempo_actual, ultimo_spawn, pantalla.get_width())

        mover_zombies()

        # Detectar zombies que se escapan
        for z in zombies[:]:
            if z["rect"].right < 0:
                zombies.remove(z)
                vidas -= 1
                if vidas <= 0:
                    vidas = 0
                    game_over = True

        # Colisiones bala→zombie
        puntaje = detectar_colisiones(balas, puntaje)

        # Colisiones zombie→jugador
        gaucho_rect = pygame.Rect(gaucho_x, gaucho_y, *gaucho_size)
        vidas = verificar_choque_con_jugador(gaucho_rect, vidas)
        if vidas <= 0:
            game_over = True
            vidas = 0  # Ensure it doesn't go negative
            continue  # Skip the rest of the game loop


        # Movimiento del jugador y disparo
        gaucho_y, is_moving = movimiento_jugador(gaucho_y, gaucho_velocidad, ALTO)

        ultimo_disparo, disparar = disparar_balas(
            balas, 
            tiempo_actual, 
            ultimo_disparo, 
            cooldown,
            gaucho_x, 
            gaucho_y,
            gaucho_size
        )

        # Dibujado
        crear_fondo()
        crear_balas(pantalla, balas, bala_img)
        
        disparo_playing, disparo_start_time = animaciones(
            pantalla, 
            gaucho, 
            disparar, 
            tiempo_actual, 
            disparo, 
            disparo_duracion, 
            is_moving, 
            caminar,
            gaucho_x, 
            gaucho_y, 
            disparo_playing, 
            disparo_start_time)

        dibujar_zombies(pantalla)

        fuente = pygame.font.SysFont(None, 36)
        texto = fuente.render(f'Puntaje: {puntaje}  Vidas: {vidas}', True, (255, 255, 255))
        pantalla.blit(texto, (10, 10))
        
        pygame.display.flip()
        reloj.tick(60)
#LAAAAA

ejecucion = True

def main():
    while ejecucion:
        accion = mostrar_menu() 

        if accion == "jugar":
            iniciar_juego()

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