from sorting_algo import sorting_algo as so
import pygame
import sys
import time
import random

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (75,71,88)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((BACKGROUND_COLOR))
pygame.display.update()
running = True
sorting = False

def draw_button(title,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global sorting

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h),0)

        if click[0] == 1:
            sorting = True
    else:
        pygame.draw.rect(screen, ac, (x, y, w, h), 0)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()
