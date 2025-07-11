import pygame
import sys
from pygame.locals import *
from config import ANCHO, ALTO, NEGRO, BLANCO

def mostrar_introduccion(pantalla, assets):
    """
    Muestra la pantalla de introduccion con el texto proporcionado.
    Retorna cuando se presiona ESC o despues del tiempo de espera.
    """
    texto = [
        "Año 18XX",
        "[nombre] se encuentraba intentando descansar",
        "de los efectos de la guerra, después de haber sido",
        "reclutado para luchar junto con Martín Miguel de Güemes,",
        "como muchos otros gauchos. Cuando de repente escucha",
        "gruñidos de agonía, acercándose en su dirección...",
        "",
        "Asi es como avista, a lo lejos, uniformes realistas,",
        "manchados y rotos, soldados caídos que volvieron",
        "de la muerte y quieren venganza."
    ]

    textos = []
    for i, linea in enumerate(texto):
        texto = assets["fuentes"]["fuente_mediana"].render(linea, True, BLANCO)
        textos.append(texto)

    skip_text = assets["fuentes"]["fuente_mediana"].render("Presiona ESC para saltar", True, BLANCO)

    #calcular posiciones de Y para cada linea
    posiciones_y = [ALTO // 4 - 50]
    for i in range(1, len(textos)):
        posiciones_y.append(posiciones_y[i-1] + 40)


    tiempo_inicio = pygame.time.get_ticks()
    duracion = 10000

    en_intro = True
    while en_intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and  evento.key == pygame.K_ESCAPE:
                en_intro = False
        if pygame.time.get_ticks() - tiempo_inicio >= duracion:
            en_intro = False


        pantalla.fill(NEGRO)

        for i, texto in enumerate(textos):
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, posiciones_y[i]))
        
        pantalla.blit(skip_text, (ANCHO - skip_text.get_width() - 20, ALTO - 40))

        pygame.display.flip()
        pygame.time.delay(30)

