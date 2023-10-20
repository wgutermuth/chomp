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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False

    # Clear the screen
    screen.blit(background, (0, 0))
    # Update fish movement
    my_fish.update()
    # Draw the fish
    my_fish.draw(screen)
    # Update the display
    pygame.display.flip()