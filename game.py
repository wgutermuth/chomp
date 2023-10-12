import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Chomp!')

pygame.draw.rect(screen,(100, 25, 0), (0, 380, 400, 400))

while True:
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == 1024:
            print('Cursor!')
