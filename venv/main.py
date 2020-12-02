from sorting_algo import sorting_algo as so
import pygame
import sys
import time

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (75,71,88)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((BACKGROUND_COLOR))
pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()

