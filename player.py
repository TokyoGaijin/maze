import pygame
import colorswatch as cs

class Player(object):
    def __init__(self, surface):
        self.surface = surface
        self.posX = 0
        self.posY = 0
        self.color = cs.red["pygame"]
        self.size = 10
        self.speed = 5
        self.player_rect = pygame.Rect(self.posX, self.posY, self.size, self.size)


    def move(self, direction):
        if direction == "left":
            self.posX -= self.speed
        if direction == "right":
            self.posX += self.speed
        if direction == "up":
            self.posY -= self.speed
        if direction == "down":
            self.posY += self.speed

        self.player_rect.x = self.posX
        self.player_rect.y = self.posY


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move("up")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move("down")
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move("left")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move("right")


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.player_rect)