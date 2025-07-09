from config import MODE_QUIT, MODE_MENU
import pygame


def procesar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return MODE_QUIT
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            return MODE_MENU