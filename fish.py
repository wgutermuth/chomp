import pygame
from settings import *

class Fish(pygame.sprite.Sprite):
    def __init__(self, x=200, y=200):
        self.image = pygame.image.load("assets/images/fish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.x = x
        self.y = y

        print("I am a brand new fish :D")

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))


    def update(self):
        if self.moving_left:
            self.x -= 1
        elif self.moving_right:
            self.x += 1
        elif self.moving_up:
            self.y -= 1
        elif self.moving_down:
            self.y += 1
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > SCREEN_WIDTH-TILE_SIZE:
            self.x = SCREEN_WIDTH-TILE_SIZE
        if self.y > SCREEN_HEIGHT-3*TILE_SIZE:
            self.y = SCREEN_HEIGHT-3*TILE_SIZE

