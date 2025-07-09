from config import FONT_HUD, BLANCO


def dibujar_fondo(pantalla, fondo, ancho_fondo, alto_fondo):
    """
    Tilea el surface `fondo` por todo el `screen`.
    """
    for y in range(0, pantalla.get_height(), alto_fondo):
        for x in range(0, pantalla.get_width(), ancho_fondo):
            pantalla.blit(fondo, (x, y))

# informacion en pantalla: puntuación y vidas
def dibujar_hud(pantalla, puntaje, vidas):
    texto = FONT_HUD.render(f'Puntuación: {puntaje}  Vidas: {vidas}', True, BLANCO)
    pantalla.blit(texto, (10, 10))

def dibujar_enemigos(pantalla, lista_enemigos):
    """
    Itera sobre enemies_list y blitea cada imagen en su rect.
    """
    for e in lista_enemigos:
        if hasattr(e["img"], "render"):
            # Es un GIF de gif_pygame
            e["img"].render(pantalla, (e["rect"].x, e["rect"].y))
        else:
            # Es una Surface estática
            pantalla.blit(e["img"], (e["rect"].x, e["rect"].y))