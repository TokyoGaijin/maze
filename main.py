import pygame
import colorswatch as cs
from enum import Enum


pygame.init()

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)

WINDOW = pygame.display.set_mode(SCREEN)
BG = cs.black["pygame"]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.display.update()
    WINDOW.fill(BG)
