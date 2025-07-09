import pygame
import audio
from assets import cargar_assets
from renderer import dibujar_fondo
from config import *

# Creamos reloj local para controlar FPS
eclock = pygame.time.Clock()


def crear_botones(musica_pausada: bool) -> list[dict]:
    """
    Genera la lista de diccionarios con información de cada botón:
    - clave: acción en minúsculas
    - normal, hover: superficies
    - rect: posición
    Incluye Pausar/Reanudar Música según el estado.
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
        surf_norm = FUENTE_GRANDE.render(texto, True, BLANCO)
        surf_hover = FUENTE_GRANDE.render(texto, True, COLOR_HOVER)
        rect = surf_norm.get_rect(center=(ANCHO // 2, y))
        botones.append({
            "clave": texto.lower(),
            "normal": surf_norm,
            "hover": surf_hover,
            "rect": rect
        })
    return botones


def dibujar_botones(pantalla: pygame.Surface, botones: list[dict]) -> None:
    """
    Dibuja cada botón en pantalla, cambiando a hover si el cursor está encima.
    """
    pos_mouse = pygame.mouse.get_pos()
    for btn in botones:
        surf = btn["hover"] if btn["rect"].collidepoint(pos_mouse) else btn["normal"]
        pantalla.blit(surf, btn["rect"])


def manejar_eventos(botones: list[dict], sonidos_menu: dict, musica_pausada: bool) -> tuple[ str|None, bool ]:
    """
    Procesa eventos del menú:
      - Clic en botón: retorna (clave, nuevo_estado_musica)
      - Tecla ESC o ventana cerrar: retorna ("salir", musica_pausada)
      - Si se clickea Pausar/Reanudar Música: alterna estado y retorna (None, nuevo_estado)
      - ENTER sobre botón: equivalente a clic
    """
    seleccion = None
    pos_mouse = pygame.mouse.get_pos()
    for i, btn in enumerate(botones):
        if btn["rect"].collidepoint(pos_mouse):
            seleccion = i
            break

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return "salir", musica_pausada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return "salir", musica_pausada
            if evento.key == pygame.K_RETURN and seleccion is not None:
                return botones[seleccion]["clave"], musica_pausada
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and seleccion is not None:
            audio.reproducir_sonido(sonidos_menu, "click")
            clave = botones[seleccion]["clave"]
            if clave in ("pausar música", "reanudar música"):
                # Alternar música de fondo
                if not musica_pausada:
                    audio.detener_musica(VOLUMEN_MUSIC_MENU["fade_ms"])
                else:
                    audio.reproducir_musica(
                        RUTA_MUSICA_MENU,
                        loops=-1,
                        volume=VOLUMEN_MUSIC_MENU["volumen"],
                        fade_ms=VOLUMEN_MUSIC_MENU["fade_ms"]
                    )
                musica_pausada = not musica_pausada
                return None, musica_pausada
            return clave, musica_pausada
    return None, musica_pausada


def mostrar_menu() -> str:
    """
    Bucle principal del menú:
      1. Carga assets y sonidos
      2. Itera: draw fondo, draw título, draw botones, manejar eventos
      3. Retorna la acción seleccionada
    """
    # 1) Inicialización local
    datos = cargar_assets()
    pantalla = datos["pantalla"]
    fondo = datos["fondo"]
    ancho_fondo = datos["ancho_fondo"]
    alto_fondo = datos["altura_fondo"]
    sonidos_menu = audio.cargar_sonido()
    musica_pausada = False

    ejecucion = True

    while ejecucion:
        # Dibujo de fondo tileado
        dibujar_fondo(pantalla, fondo, ancho_fondo, alto_fondo)

        # Título centrado
        titulo_surf = FUENTE_TITULO_PRINCIPAL.render("Gaucho Defense", True, BLANCO)
        titulo_rect = titulo_surf.get_rect(center=(ANCHO // 2, 100))
        pantalla.blit(titulo_surf, titulo_rect)

        # Botones y dibujo
        botones = crear_botones(musica_pausada)
        dibujar_botones(pantalla, botones)

        # Manejo de eventos
        accion, musica_pausada = manejar_eventos(botones, sonidos_menu, musica_pausada)
        if accion:
            return accion

        # Refresh
        pygame.display.flip()
        eclock.tick(60)