import pygame
import sys
from config import ANCHO, ALTO, fuente_grande, BLANCO, GRIS, COLOR_HOVER, SONIDO_CLICK

pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
pygame.mixer.init()                         # Inicializa el mixer de sonido
#click_sound = pygame.mixer.Sound(SONIDO_CLICK)  # efecto click, a confirmar si se quiere usar.

def crear_botones():
    """
    Genera una lista de tuplas con la información de cada botón:
    (texto, superficie_render, rectángulo, color_normal, color_hover)
    """
    labels = [("Jugar", 200), ("Ranking", 270), ("Créditos", 340), ("Salir", 410)]
    botones = []
    for texto, y in labels:
        # Se renderizan las dos versiones del texto: normal y hover, para cambiar la apariencia de cada boton. Aca debemos definir la paleta de colores
        surf_normal = fuente_grande.render(texto, True, BLANCO)
        surf_hover  = fuente_grande.render(texto, True, COLOR_HOVER)
        rect = surf_normal.get_rect(center=(ANCHO // 2, y))
        # Guarda todo en la lista
        botones.append({
            "texto": texto.lower(),     # clave de acción
            "normal": surf_normal,      # superficie Pygame normal
            "hover":  surf_hover,       # superficie Pygame cuando está encima
            "rect":   rect              # posición y tamaño
        })
    return botones

def dibujar_botones(botones):
    """
    Dibuja cada botón en pantalla. Si el mouse está sobre él,
    usamos la superficie 'hover', sino la 'normal'.
    """
    mouse_pos = pygame.mouse.get_pos()    # posición actual del cursor
    for btn in botones:
        if btn["rect"].collidepoint(mouse_pos):
            pantalla.blit(btn["hover"], btn["rect"])
        else:
            pantalla.blit(btn["normal"], btn["rect"])

def manejar_eventos(botones):
    """
    Procesa eventos del menú:
    - Si se hace click en un botón, devuelve su 'texto'. 
    - Teclas ARRIBA/ABAJO para navegar y ENTER para confirmar.
    - Devuelve None si no se seleccionó nada aún.
    """
    # Índice del botón seleccionado: se calcula cuál está en hover
    seleccion = None
    mouse_pos = pygame.mouse.get_pos()
    for i, btn in enumerate(botones):
        if btn["rect"].collidepoint(mouse_pos):
            seleccion = i
            break

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            # click izquierdo
            if seleccion is not None:
                #click_sound.play()   # sonido de click a definir si usaremos sonidos.
                return botones[seleccion]["texto"]
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and seleccion is not None:
                seleccion = max(0, seleccion - 1)
            if evento.key == pygame.K_DOWN and seleccion is not None:
                seleccion = min(len(botones) - 1, seleccion + 1)
            if evento.key == pygame.K_RETURN and seleccion is not None:
                #click_sound.play()
                return botones[seleccion]["texto"]
    return None

def mostrar_menu():
    """
    Ejecuta el bucle principal del menú. Devuelve la acción seleccionada.
    """
    botones = crear_botones()

    seleccion = 0

    while True:
        pantalla.fill(GRIS)        # color de fondo
        dibujar_botones(botones)   # visualizar todos

        accion = manejar_eventos(botones)
        if accion:
            return accion         # "jugar", "ranking", "salir"

        pygame.display.flip()      # actualiza pantalla completa
        clock.tick(60)             # limitacion a 60 fps
