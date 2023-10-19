import pygame
import time
import sys
import random

from settings import *

print(f" the quit event is type {pygame.QUIT}")
pygame.init()

# Font Settings
game_font = pygame.font.Font("assets/fonts/hogfish.otf", 128)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0,0,0))
for i in range(SCREEN_WIDTH//TILE_SIZE):
    screen.blit(sand, (i*TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE, TILE_SIZE,TILE_SIZE))
    screen.blit(sand_top, (i*TILE_SIZE, SCREEN_HEIGHT-2*TILE_SIZE, TILE_SIZE,TILE_SIZE))


# draw CHOMP!
text = game_font.render("CHOMP!",True,(17,3,64))
screen.blit(text,(SCREEN_WIDTH//2-text.get_width()//2, SCREEN_HEIGHT//2-text.get_height()//2))

# randomly place 4 pieces of grass along the bottom of the screen

seagrass_long = pygame.image.load("assets/images/seagrass_long.png").convert()
seagrass_long.set_colorkey((0,0,0))
seagrass_short = pygame.image.load("assets/images/seagrass_short.png").convert()
seagrass_short.set_colorkey((0,0,0))
for i in range(15):
    random_grass = random.randint(1,2)
    x = random.randint(0,SCREEN_WIDTH)
    y = random.randint(SCREEN_HEIGHT-2*TILE_SIZE,SCREEN_HEIGHT)-(0.5*TILE_SIZE
    grass_assets = ['seagrass_long', 'seagrass_short']
    grass = random.choice(grass_assets)
    screen.blit(grass, (x, y))

#pygame.draw.rect(screen, (0,255,0), (200,200, 50,50))
pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
