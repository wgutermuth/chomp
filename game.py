import pygame
import time
import sys
import random
import fish
from settings import *

print(f" the quit event is type {pygame.QUIT}")
pygame.init()

# Font Settings
game_font = pygame.font.Font("assets/fonts/hogfish.otf", 128)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0,0,0))

# Fish
fish_graphic = pygame.image.load("assets/images/fish.png").convert()
fish_graphic.set_colorkey((0,0,0))
my_fish = fish.Fish() # create a new fish


seagrass_long = pygame.image.load("assets/images/seagrass_long.png").convert()
seagrass_long.set_colorkey((0,0,0))
seagrass_short = pygame.image.load("assets/images/seagrass_short.png").convert()
seagrass_short.set_colorkey((0,0,0))

background = screen.copy()
def draw_background():
    background.fill(WATER_COLOR)
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        background.blit(sand, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE, TILE_SIZE, TILE_SIZE))
        background.blit(sand_top, (i * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    for i in range(15):
        x = random.randint(0,SCREEN_WIDTH)
        y = random.randint(SCREEN_HEIGHT-2*TILE_SIZE,SCREEN_HEIGHT)-(0.5*TILE_SIZE)
        grass_assets = [seagrass_long, seagrass_short]
        grass = random.choice(grass_assets)
        background.blit(grass, (x, y))
    text = game_font.render("CHOMP!", True, (17, 3, 64))
    background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
draw_background()

#pygame.draw.rect(screen, (0,255,0), (200,200, 50,50))
#pygame.display.flip()

fish_x = 200
fish_y = 200

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(f'The {event.key} is pressed!')
            if event.key == pygame.K_LEFT:
                my_fish.move_left()
            if event.key == pygame.K_RIGHT:
                my_fish.move_right()
    screen.blit(background, (0,0))
    my_fish.draw(screen)
    pygame.display.flip()
