import pygame
import colorswatch as cs

class WallBlock(object):
    def __init__(self, surface):
        self.surface = surface
        self.posX = 0
        self.posY = 0
        self.color = cs.cornflower_blue["pygame"]
        self.size = 20
        self.wall_rect = pygame.Rect(self.posX, self.posY, self.size, self.size)

        self.current_maze = []

        self.maze_pattern = [ "--------------------------------",
                              "--------------------------------",
                              "--------------------------------",
                              "--------------------------------",
                              "--111S-1111111111111111111111---",
                              "--1--------11--------11-----1---",
                              "--1--111---11--1111--11-----1---",
                              "--1--1---1111-----1--11--1111---",
                              "--1--1-----11111--1--11--1--1---",
                              "--1--11111--------1--11-----1---",
                              "--1------1-----1111---11-1--1---",
                              "--11111--1---1111---1----1--1---",
                              "--1------1---1--11111--111--1---",
                              "--1--11111---1------1--1---11---",
                              "--1----------11111--1-----111---",
                              "--1----1------------1111----1---",
                              "--1----1-----1---1----11----1---",
                              "--11111111111111111111111--11---",
                              "--------------------------------",
                              "--------------------------------",
                              "--------------------------------",
                              "--------------------------------",
                              "--------------------------------",
                              "--------------------------------"]


    def build_level(self):
        for row in self.maze_pattern:
            for col in row:
                if col == "1":
                    self.current_maze.append(pygame.Rect(self.posX, self.posY, self.size, self.size))

                self.posX += self.size

            self.posY += self.size
            self.posX = 0


    def draw(self):
        for block in self.current_maze:
            pygame.draw.rect(self.surface, self.color, block)
