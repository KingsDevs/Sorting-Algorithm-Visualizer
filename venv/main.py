from sorting_algo import sorting_algo
import pygame
import sys
import time
import random

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (53,45,49)
BLACK = (0,0,0)
WHITE = (255,255,255)

num_bars = 40
bar_width = 20
space = 5
delay = .01


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((BACKGROUND_COLOR))
font = pygame.font.SysFont("Arial", 30)
pygame.display.update()

running = True


def draw_button(title,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    sorting = False
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h),0)
        if click[0] == 1:
            sorting = True
    else:
        pygame.draw.rect(screen, ac, (x, y, w, h), 0)

    text = font.render(title,True,WHITE)
    screen.blit(text, (x+10, y+10))
    return sorting

so = sorting_algo(screen,BACKGROUND_COLOR,BLACK,WHITE,num_bars,bar_width,space,WIDTH,delay)
arr = so.random_items()
while True:
    sorting = draw_button("Sort", 200 - 75 / 2, 200 - 25, 75, 50, (230, 230, 230), (200, 200, 200))
    if sorting:
        arr = so.odd_even_sort(arr)
        so.drawbars(arr,BLACK)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



