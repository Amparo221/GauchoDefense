import pygame, sys
import config


def pedir_nombre_jugador(pantalla, fuente_jugador):
    """
    Muestra en pantalla un prompt para que el jugador escriba su nombre.
    Devuelve el string que teclee (sin caracteres de control).
    """
    nombre = ""
    cursor_visible = True
    tiempo_cursor = 0

    # Fuente y rectángulo de prompt
    prompt_surf = fuente_jugador.render("Ingresa tu nombre:", True, config.BLANCO)
    prompt_rect = prompt_surf.get_rect(center=(config.ANCHO//2, config.ALTO//2 - 50))

    # Bucle de entrada
    entrando = True
    clock_input = pygame.time.Clock()

    while entrando:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    # Si no escribió nada, usar ANÓNIMO x default
                    return nombre if nombre.strip() else "ANÓNIMO"
                elif ev.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < 12: # limite de caracteres ingreso del nombre.
                        nombre += ev.unicode

        # Parpadeo del cursor: alterna visible/invisible cada 500ms
        tiempo_cursor += clock_input.get_time()
        if tiempo_cursor >= 500:
            tiempo_cursor = 0
            cursor_visible = not cursor_visible

        # Dibujado
        pantalla.fill(config.NEGRO)
        pantalla.blit(prompt_surf, prompt_rect)

        # Renderizado del teclado
        text_surf = fuente_jugador.render(nombre, True, config.BLANCO)
        # Calculo del rect de texto para centrar horizontalmente
        text_rect = text_surf.get_rect(midtop=(config.ANCHO//2, config.ALTO//2))
        pantalla.blit(text_surf, text_rect)

        # Dibujar cursor si está visible
        if cursor_visible:
            cursor_x = text_rect.right + 5
            cursor_y = text_rect.y
            cursor_h = text_rect.height
            pygame.draw.rect(pantalla, config.BLANCO, (cursor_x, cursor_y, 3, cursor_h))

        pygame.display.flip()
        clock_input.tick(60)

def mostrar_creditos(pantalla, assets):
    """
    Muestra la pantalla de créditos con los nombres de los creadores.
    Espera a que se cierre la ventana o se pulse ESC para volver.
    """
    clock = pygame.time.Clock()

    fuente_grande = assets["fuentes"]["fuente_grande"]
    fuente_mediana = assets["fuentes"]["fuente_mediana"]


    # Lista de creadores
    nombres = ["Paula Ortega", "Amparo Moreno", "León Puddini"]

    # Pre-renderizo el título
    titulo_surf = fuente_grande.render("Créditos", True, config.BLANCO)
    titulo_rect = titulo_surf.get_rect(center=(config.ANCHO//2, 80))

    # Pre-renderizo de cada nombre
    nombre_surfs = []
    separacion = 50
    y_inicial = 180
    for i, nombre in enumerate(nombres):
        surf = fuente_mediana.render(nombre, True, config.BLANCO)
        rect = surf.get_rect(center=(config.ANCHO//2, y_inicial + i * separacion))
        nombre_surfs.append((surf, rect))

    # Texto para volver al menu principal
    volver_surf = fuente_mediana.render("Presiona ESC para volver", True, config.BLANCO)
    volver_rect = volver_surf.get_rect(center=(config.ANCHO//2, config.ALTO - 40))

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                ejecutando = False

        pantalla.fill(config.NEGRO)
        pantalla.blit(titulo_surf, titulo_rect)
        for surf, rect in nombre_surfs:
            pantalla.blit(surf, rect)
        pantalla.blit(volver_surf, volver_rect)

        pygame.display.flip()
        clock.tick(60)