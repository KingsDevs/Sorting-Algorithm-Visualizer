import pygame
import os
import time
import random

class sorting_algo:

    def __init__(self,screen,backcolor,color,num_bars,bar_width,space,width,delay):
        self.screen = screen
        self.backcolor = backcolor
        self.color = color
        self.num_bars = num_bars
        self.bar_width = bar_width
        self.space = space
        self.width = width
        self.delay = delay
        self.clock = pygame.time.Clock()

    def x_bar(self,i):
        x = (i * self.bar_width) + (i + self.space) + (self.width - (self.num_bars * self.bar_width + self.num_bars * self.space)) / 2
        return x

    def random_items(self):
        arr = []
        for i in range(self.num_bars):
            height = random.randint(-100, -1)
            arr.append(height)
            x = self.x_bar(i)
            self.draw_bar(height,x)
        return arr

    def drawbars(self,arr):
        for i in range(len(arr)):
            x = self.x_bar(i)
            self.draw_bar(arr[i],x)

    def draw_bar(self,height,x):
        pygame.draw.rect(self.screen, self.color, (x, 200, self.bar_width, height), 0)

    def selection_sort(self,a):
        elapsed = self.clock.tick(30)
        counter = 0
        minimum_index = counter
        traversing_index = counter + 1
        while(counter < len(a)):

            for traversing_index in range(counter, len(a)):
                if a[traversing_index] < a[minimum_index]:
                    minimum_index = traversing_index
                traversing_index += 1
            for i in range(len(a)):
                x = self.x_bar(i)
                height = a[i]
                self.draw_bar(height,x)
                time.sleep(self.delay)
                pygame.display.update()
            self.screen.fill(self.backcolor)
            a[counter], a[minimum_index] = a[minimum_index], a[counter]
            counter += 1
            minimum_index = counter
            traversing_index = counter + 1
        for i in range(len(a)):
            x = self.x_bar(i)
            height = a[i]
            self.draw_bar(height, x)
            time.sleep(self.delay)
            pygame.display.update()
        return a

    def bubble_sort(self,a):
        swapped_values = True
        traversing_index = 0

        while(swapped_values):
            swapped_values = False
            traversing_index = 0
            for i in range(len(a)):
                x = self.x_bar(i)
                height = a[i]
                self.draw_bar(height,x)
                time.sleep(self.delay)
                pygame.display.update()
            for traversing_index in range(len(a)-1):
                if a[traversing_index] > a[traversing_index + 1]:
                    a[traversing_index], a[traversing_index + 1] = a[traversing_index + 1], a[traversing_index]
                    swapped_values = True

        return a


    def cocktail_shaker_sort(self,a):
        swapped_values = True
        traversing_index = 0

        while(swapped_values):
            swapped_values = False
            traversing_index = 0
            for i in range(0,len(a)-1):
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swapped_values = True
                traversing_index += 1

            if swapped_values:
                for i in range(traversing_index, (len(a)-len(a)+1), -1):
                    if a[i] < a[i - 1]:
                        a[i], a[i - 1] = a[i - 1], a[i]
                        swapped_values = True
                    traversing_index -= 1

        return a

    def odd_even_sort(self,a):
        is_sorted = False
        while(is_sorted == False):
            is_sorted = True
            #Odd Face
            for i in range(1,len(a)-1,2):
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
                    is_sorted = False
            #Even Face
            for i in range(0, len(a)-1,2):
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
                    is_sorted = False

        return a

#a = [30,2,4,8,23,1,6,9,2,45,2,34]
#print(odd_even_sort(a))

