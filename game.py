import pygame
import time
import sys

# DIMENSIONS
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64  # square, height = width

# COLORS
WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)

print(f" the quit event is type {pygame.QUIT}")
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (200 - 32, 200 - 32))
#pygame.draw.rect(screen, (0,255,0), (200,200, 50,50))
pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
