import pygame, sys
from config import *


def pedir_nombre_jugador(pantalla: pygame.surface) -> str:
    """
    Muestra en pantalla un prompt para que el jugador escriba su nombre.
    Tiene un limite de caracteres, un parpadeo del cursor.
    Devuelve el string que teclee o ANONIMO si no ingresó nada.
    """
    nombre = ""
    cursor_visible = True
    tiempo_cursor = 0

    prompt_surf = FONT_TITLE.render("Ingresa tu nombre:", True, BLANCO)
    prompt_rect = prompt_surf.get_rect(center=(ANCHO//2, ALTO//2 - 50))

    entrando = True
    clock_input = pygame.time.Clock()

    while entrando:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    return nombre if nombre.strip() else "ANÓNIMO"
                elif ev.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < 12:
                        nombre += ev.unicode

        tiempo_cursor += clock_input.get_time()
        if tiempo_cursor >= 500:
            tiempo_cursor = 0
            cursor_visible = not cursor_visible

        pantalla.fill(NEGRO)
        pantalla.blit(prompt_surf, prompt_rect)

        text_surf = FONT_TITLE.render(nombre, True, BLANCO)

        text_rect = text_surf.get_rect(midtop=(ANCHO//2, ALTO//2))
        pantalla.blit(text_surf, text_rect)

        if cursor_visible:
            cursor_x = text_rect.right + 5 
            cursor_y = text_rect.y 
            cursor_h = text_rect.height
            pygame.draw.rect(pantalla, BLANCO, (cursor_x, cursor_y, 3, cursor_h))

        pygame.display.flip()
        clock_input.tick(60)

def mostrar_creditos(pantalla: pygame.surface) -> None:
    """
    Muestra la pantalla de créditos con los nombres de los creadores.
    Espera a que se cierre la ventana o se pulse ESC para volver.
    """
    clock = pygame.time.Clock()
    ejecutando = True

    nombres = ["Paula Ortega", "Amparo Moreno", "León Puddini"]

    titulo_surf = FUENTE_GRANDE.render("Créditos", True, BLANCO)
    titulo_rect = titulo_surf.get_rect(center=(ANCHO//2, 80))

    nombre_surfs = []
    separacion = 50
    y_inicial = 180
    
    for i, nombre in enumerate(nombres):
        surf = FUENTE_MEDIANA.render(nombre, True, BLANCO)
        rect = surf.get_rect(center=(ANCHO//2, y_inicial + i * separacion))
        nombre_surfs.append((surf, rect))

    volver_surf = FUENTE_MEDIANA.render("Presiona ESC para volver", True, BLANCO)
    volver_rect = volver_surf.get_rect(center=(ANCHO//2, ALTO - 40))

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                ejecutando = False

        pantalla.fill(NEGRO)
        pantalla.blit(titulo_surf, titulo_rect)
        for surf, rect in nombre_surfs:
            pantalla.blit(surf, rect)
        pantalla.blit(volver_surf, volver_rect)

        pygame.display.flip()
        clock.tick(60)