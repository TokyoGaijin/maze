import pygame
import colorswatch as cs

class WallBlock(object):
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = cs.cornflower_blue["pygame"]
        self.size = 20
        self.wall_rect = pygame.Rect(self.posX, self.posY, self.size, self.size)


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.wall_rect)


current_maze = []

maze_pattern = [["--------------------------------"],
                ["--------------------------------"],
                ["--------------------------------"],
                ["--------------------------------"],
                ["--111111111111111111111111111---"],
                ["--1--------11--------11-----1---"],
                ["--1--111---11--1111--11-----1---"],
                ["--1--1--11111-----1--11--1111---"],
                ["--1--1-----11111--1--11--1--1---"],
                ["--1--11111-----1--1--11-----1---"],
                ["--1------1-----1111---11-1--1---"],
                ["--11111--1---1111---1----1--1---"],
                ["--1------1---1--11111--111--1---"],
                ["--1--11111---1------1--1---11---"],
                ["--1----------11111--1-----111---"],
                ["--1----1------------1111----1---"],
                ["--1----1-----1---1----11----1---"],
                ["--111111111111111111111111111---"],
                ["--------------------------------"],
                ["--------------------------------"],
                ["--------------------------------"],
                ["--------------------------------"],
                ["--------------------------------"],
                ["--------------------------------"]]


def build(surface):
    global current_maze
    x, y = 0, 0
    for row in maze_pattern:
        for col in row:
            if col == "1":
                current_maze.append(WallBlock(surface, x, y))
            x += 20
        y += 20
        x = 0

def draw():
    for block in current_maze:
        block.draw()