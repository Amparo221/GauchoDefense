import pygame
from game.audio import reproducir_musica, detener_musica, reproducir_sonido
from ui.renderer import dibujar_fondo_estatico, dibujar_titulo
import config

# Creamos reloj local para controlar FPS
eclock = pygame.time.Clock()

def crear_botones(fuente_grande, musica_pausada: bool) -> list[dict]:
    """
    Declara una lista de tuplas con todas las variables de botones y su altura.
    - Incluye Pausar/Reanudar Música según el estado.
    Desempaqueta las tuplas y genera la lista de diccionarios botones con información de cada botón:
    - clave: acción en minúsculas
    - normal, hover: declara y asigna superficies para cada estado
    - rect: posición
    Retorna botones

    Args:
        musica_pausada (bool): Estado de la música.

    Returns:
        list[dict]: botones
    """
    etiquetas = [
        ("Jugar", 200),
        ("Ranking", 270),
        ("Créditos", 340),
        ("Pausar Música" if not musica_pausada else "Reanudar Música", 410),
        ("Salir", 480)
    ]
    botones = []
    for texto, y in etiquetas:
        surf_norm = fuente_grande.render(texto, True, config.BLANCO)
        surf_hover = fuente_grande.render(texto, True, config.COLOR_HOVER)
        rect = surf_norm.get_rect(center=(config.ANCHO // 2, y))
        botones.append({
            "clave": texto.lower(),
            "normal": surf_norm,
            "hover": surf_hover,
            "rect": rect
        })
    return botones


def dibujar_botones(pantalla: pygame.Surface, botones: list[dict]) -> None:
    """
    Recibe pantalla, donde dibuja botones. 
    Declara una colision con el mouse: en estado pasivo la superficie surf_norm,
    en estado activo la superficie surf_hover

    Args:
        pantalla (pygame.surface): superficie de la pantalla del juego.
        botones (list[dict]): lista de diccionarios con informacion de los botones.
    """
    pos_mouse = pygame.mouse.get_pos()
    for btn in botones:
        surf = btn["hover"] if btn["rect"].collidepoint(pos_mouse) else btn["normal"]
        pantalla.blit(surf, btn["rect"])


def manejar_eventos(botones: list[dict], sonidos_menu: dict, musica_pausada: bool) -> tuple[ str|None, bool ]:
    """
    Procesa eventos en el menú:
      - Enumera cada botón
      - Retorna tupla (clave, nuevo_estado_musica):
      - Tecla ESC o ventana cerrar: retorna ("salir", musica_pausada)
      - Si se clickea Pausar/Reanudar Música: alterna estado y retorna (None, nuevo_estado)
      - ENTER sobre botón: equivalente a clic
      - El evento click izquierdo: reproduce sonido de click

    Args:
        botones (list[dict]): lista de diccionarios con informacion de los botones.
        sonidos_menu (dict): diccionario con sonidos del menu.
        musica_pausada (bool): Estado de la musica.

    Returns:
        tuple[ str|None, bool ]: (clave, musica_pausada)
    """
    seleccion = None
    pos_mouse = pygame.mouse.get_pos()
    for i, btn in enumerate(botones):
        if btn["rect"].collidepoint(pos_mouse):
            seleccion = i
            break

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return config.MODE_QUIT, musica_pausada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return config.MODE_SALIR, musica_pausada
            if evento.key == pygame.K_RETURN and seleccion is not None:
                return botones[seleccion]["clave"], musica_pausada
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and seleccion is not None:
            reproducir_sonido(sonidos_menu, "click")
            clave = botones[seleccion]["clave"]
            if clave in ("pausar música", "reanudar música"):
                if not musica_pausada:
                    detener_musica(config.VOLUMEN_MUSIC_MENU["fade_ms"])
                else:
                    reproducir_musica(
                        config.RUTA_MUSICA_MENU,
                        loops=-1,
                        volume=config.VOLUMEN_MUSIC_MENU["volumen"],
                        fade_ms=config.VOLUMEN_MUSIC_MENU["fade_ms"]
                    )
                musica_pausada = not musica_pausada
                return None, musica_pausada
            return clave, musica_pausada
    return None, musica_pausada


def mostrar_menu(pantalla, assets, sonido: list[dict]) -> str:
    """
    Bucle principal del menú:
      1. Carga assets y sonidos necesarios
      2. Dibuja fondo tileado, título y botones
      3. Maneja eventos y retorna la acción seleccionada
      3. Retorna la acción seleccionada

    Args:
        assets (dict): diccionario con assets del juego.
        sonido (dict): diccionario con sonidos del juego.

    Returns:
        str: accion seleccionada
    """
    # 1) Inicialización local
    musica_pausada = False

    ejecucion = True

    while ejecucion:
        # Dibujo de fondo tileado
        dibujar_fondo_estatico(pantalla, assets["imagenes"]["fondo_menu"], assets["imagenes"]["ancho_fondo_menu"], assets["imagenes"]["alto_fondo_menu"])

        # Título centrado
        dibujar_titulo(pantalla, assets["fuentes"]["fuente_titulo_principal"])

        # Botones y dibujo
        botones = crear_botones(assets["fuentes"]["fuente_grande"], musica_pausada)
        dibujar_botones(pantalla, botones)

        # Manejo de eventos
        accion, musica_pausada = manejar_eventos(botones, sonido, musica_pausada)
        if accion:
            return accion

        pygame.display.flip()
        eclock.tick(60)