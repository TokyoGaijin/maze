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
player = p.Player(WINDOW, SCREEN_X / 2, SCREEN_Y / 2)

def init():
    maze.build(WINDOW)
    print(len(maze.current_maze))

def update():
    player.update()

def draw():
    player.draw()
    maze.draw()


def main():
    global inPlay
    init()

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