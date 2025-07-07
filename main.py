import pygame
from pygame.locals import *
from jugador import *
from menu import *
from config import *
from ranking import show_ranking, add_score

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
fondo = pygame.image.load("assets/fondo.png").convert()
ancho_fondo, altura_fondo = fondo.get_size()  

gaucho = pygame.image.load("assets/default.png").convert_alpha()
GAUCHO_SIZE=(150,150)
gaucho = pygame.transform.scale(gaucho, gaucho_size)

# BALAS
bala_img = pygame.Surface((15, 5))  
bala_img.fill((250, 0, 0)) 
BALAS = []  #Lista pa las balas
COOLDOWN = 400  


def crear_fondo():
    for y in range(0, pantalla.get_height(), altura_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))


def crear_balas():
    for bala in BALAS:
        pantalla.blit(bala_img, (bala[0], bala[1]))

def iniciar_juego():
    # Posición y estado inicial del gaucho
    gaucho_x = 0
    gaucho_y = 0
    gaucho_velocidad = 5

    ultimo_disparo = 0  


    running = True
    reloj = pygame.time.Clock()

    while running:

        tiempo_actual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                running = False
                
        gaucho_y = movimiento_jugador(gaucho_y, gaucho_velocidad)

        #estos variables quizas deban venir por parámetro?
        ultimo_disparo = disparar_balas(
            BALAS, # esta no se si deba ser una constante. 
            tiempo_actual, 
            ultimo_disparo, 
            COOLDOWN,
            gaucho_x, 
            gaucho_y,
            GAUCHO_SIZE
        )

        crear_fondo()

        crear_balas()
        
        pantalla.blit(gaucho, (gaucho_x, gaucho_y))

        
        pygame.display.flip()
        reloj.tick(60)

ejecucion = True
def main():
    while ejecucion:
        accion = mostrar_menu() 

        if accion == "jugar":
            iniciar_juego()

        elif accion == "ranking":
            show_ranking(pantalla)
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