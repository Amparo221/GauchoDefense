import config
import pygame

def dibujar_fondo_estatico(pantalla: pygame.surface, fondo: pygame.surface, ancho_fondo: int, alto_fondo: int) -> None:
    """
    Emplaza el fondo estatico en pantalla

    Args:
        pantalla (pygame.surface): superficie de la pantalla del juego.
        fondo (pygame.surface): superficie con el fondo del juego.
        ancho_fondo (int): ancho del fondo.
        alto_fondo (int): alto del fondo.
    """
    for y in range(0, pantalla.get_height(), alto_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))

def dibujar_fondo_juego(pantalla, fondo, ancho_fondo, alto_fondo, estado):    
    estado["fondo_x"] -= config.BACKGROUND_SPEED

    if estado["fondo_x"] <= -ancho_fondo:
        estado["fondo_x"] = 0

    for y in range(0, pantalla.get_height(), alto_fondo):
        for x in range(0, pantalla.get_width() + ancho_fondo, ancho_fondo):
            pantalla.blit(fondo, (x + estado["fondo_x"], y))

def dibujar_hud(pantalla, fuente_hud, puntaje, vidas):
    """Dibuja el HUD con la puntuación y las vidas del jugador.
    """
    texto = fuente_hud.render(f'Puntuación: {puntaje}  Vidas: {vidas}', True, config.BLANCO)
    pantalla.blit(texto, (10, 10))

def dibujar_enemigos(pantalla: pygame.surface, lista_enemigos: list) -> None:
    """
    Itera sobre enemies_list y:
    - Si es un GIF de gif_pygame lo dibuja -> si tiene render como atributo
    - Si es una Surface estática lo dibuja

    Args:
        pantalla (pygame.surface): superficie de la pantalla del juego.
        lista_enemigos (list): lista de diccionarios con informacion de los enemigos.
    """
    for e in lista_enemigos:
        if hasattr(e["img"], "render"):
            # Es un GIF de gif_pygame
            e["img"].render(pantalla, (e["rect"].x, e["rect"].y))
        else:
            # Es una Surface estática
            pantalla.blit(e["img"], (e["rect"].x, e["rect"].y))

def dibujar_titulo(pantalla, fuente_titulo):
    """Dibuja el título del juego en la pantalla."""
    titulo_surf = fuente_titulo.render("Gaucho Defense", True, config.BLANCO)
    titulo_rect = titulo_surf.get_rect(center=(config.ANCHO // 2, 100))
    pantalla.blit(titulo_surf, titulo_rect)

def dibujar_game_over(pantalla, fuente_titulo):
    """Dibuja la pantalla de Game Over."""
    pantalla.fill(config.NEGRO)
    texto_partida_perdida = fuente_titulo.render('Perdiste, Canejo', True, config.BLANCO)
    pantalla.blit(texto_partida_perdida, texto_partida_perdida.get_rect(center=(config.ANCHO//2, config.ALTO//2 - 50)))
    pygame.display.flip()
    pygame.time.delay(3000)