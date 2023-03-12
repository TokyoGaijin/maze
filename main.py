import pygame
import player as p
import colorswatch as cs
import maze
from enum import Enum


pygame.init()

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)

WINDOW = pygame.display.set_mode(SCREEN)
BG = cs.black["pygame"]

CLOCK = pygame.time.Clock()
FPS = 60

inPlay = True
player = p.Player(WINDOW)
board = maze.WallBlock(WINDOW)
board.build_level()

def stage_player():
    x, y = 0, 0
    for row in board.maze_pattern:
        for col in row:
            if col == "S":
                player.posX = x
                player.posY = y

            x += 20

        y += 20
        x = 0
    player.player_rect.x = player.posX
    player.player_rect.y = player.posY

stage_player()

def update():
    player.update()


def draw():
    player.draw()
    board.draw()


def main():
    global inPlay

    while inPlay:
        CLOCK.tick(FPS)

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            inPlay = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False

        update()
        draw()
        pygame.display.update()
        WINDOW.fill(BG)


if __name__ == "__main__":
    main()