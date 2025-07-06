import pygame, gif_pygame
from pygame.locals import *
from jugador import *
from menu import *
from config import *
from enemigos import *


pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
fondo = pygame.image.load("GauchoDefense/assets/fondo.png").convert()
ancho_fondo, altura_fondo = fondo.get_size()  

gaucho = pygame.image.load("GauchoDefense/assets/gaucho.png").convert_alpha()
gaucho_size=(155,175)
gaucho = pygame.transform.scale(gaucho, gaucho_size)


caminar = gif_pygame.load("GauchoDefense/assets/caminar_2.gif")
disparo = gif_pygame.load("GauchoDefense/assets/disparo_3.gif")

tecla_presionada = pygame.key.get_pressed()

# BALAS
bala_img = pygame.Surface((15, 5))  
bala_img.fill((0, 0, 0)) 
balas = []  #Lista pa las balas 
cooldown = 400  



disparo_playing = False
disparo_start_time = 0
disparo_duration = 400  














def crear_fondo():
    for y in range(0, pantalla.get_height(), altura_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))


def crear_balas():
    for bala in balas:
        pantalla.blit(bala_img, (bala[0], bala[1]))






#LAAAA
def iniciar_juego():
    disparo_playing = False
    disparo_start_time = 0
    disparo_duration = 400


    ultimo_spawn = 0
    puntaje = 0
    vidas = 3
    


    # Posición y estado inicial del gaucho
    gaucho_x = 0
    gaucho_y = 0
    gaucho_velocidad = 5
    gaucho_rect = pygame.Rect(gaucho_x, gaucho_y, *gaucho_size)

    ultimo_disparo = 0  

    movimiento = False
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
            running = False
            continue # ------------- ACA DEBERIA VOLVER AL MENU


        ultimo_spawn = spawn_zombie(tiempo_actual, ultimo_spawn, pantalla.get_width())

        mover_zombies()

        puntaje = detectar_colisiones(balas, puntaje)

        gaucho_rect = pygame.Rect(gaucho_x, gaucho_y, *gaucho_size)
        vidas = verificar_choque_con_jugador(gaucho_rect, vidas)

        

        if vidas <= 0:
            game_over = True
            vidas = 0  # Ensure it doesn't go negative
            continue  # Skip the rest of the game loop



        gaucho_y, is_moving = movimiento_jugador(gaucho_y, gaucho_velocidad)

        #estos variables quizas deban venir por parámetro?
        ultimo_disparo, disparar = disparar_balas(
            balas, 
            tiempo_actual, 
            ultimo_disparo, 
            cooldown,
            gaucho_x, 
            gaucho_y,
            gaucho_size
        )

        crear_fondo()
        crear_balas()
        
        if disparar:
            disparo_playing = True
            disparo_start_time = tiempo_actual
            disparo.reset() 
        if disparo_playing:
            disparo.render(pantalla, (gaucho_x, gaucho_y))
    
            if tiempo_actual - disparo_start_time >= disparo_duration:
                disparo_playing = False
        elif is_moving:
            caminar.render(pantalla, (gaucho_x, gaucho_y))
        else:
            pantalla.blit(gaucho, (gaucho_x, gaucho_y))

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
            print("Ranking:")  
            pygame.time.delay(1000)

        elif accion in ("créditos", "creditos"):
            print("Créditos: Equipo Gaucho Defense")
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