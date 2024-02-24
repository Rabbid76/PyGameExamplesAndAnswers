# How to correctly update the grid in falling sand simulation?
# https://stackoverflow.com/questions/71257560/how-to-correctly-update-the-grid-in-falling-sand-simulation/71257698#71257698
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Gravity
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame
import random

pygame.init()

class Grid:

    def __init__(self, width, height, tile_size):
        self.tile_size = tile_size
        self.rows = height // self.tile_size
        self.columns = width // self.tile_size
        self.current_grid =  [[0 for _ in range(self.columns)] for _ in range(self.rows)]
    def add_cell(self, x, y):
        row = y // self.tile_size
        col = x // self.tile_size
        self.current_grid[row][col] = 1
    def update_grid(self):
        previous_grid = self.current_grid
        self.current_grid = [[0 for i in range(self.columns)] for j in range(self.rows)]
        self.current_grid[self.rows-1] = previous_grid[self.rows-1][:]        
        for i in range(self.rows-1):
            for j in range(self.columns):
                if previous_grid[i][j] == 1:
                    if previous_grid[i+1][j] == 0:
                        self.current_grid[i+1][j] = 1
                        continue
                    left_side = j > 0 and previous_grid[i+1][j-1] == 0
                    right_side = j < self.columns-1 and previous_grid[i+1][j+1] == 0
                    if left_side and right_side:
                        self.current_grid[i+1][j+random.choice([-1, 1])] = 1
                    elif left_side:
                        self.current_grid[i+1][j-1] = 1
                    elif right_side:
                        self.current_grid[i+1][j+1] = 1
                    else:
                        self.current_grid[i][j] = 1

    def draw_grid(self, surf):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.current_grid[row][col] == 1:
                    rect = (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(surf, (164, 104, 32), rect)


window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

grid = Grid(*window.get_size(), 5)
timer_event = pygame.USEREVENT
pygame.time.set_timer(timer_event, 20)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == timer_event: 
            grid.update_grid()
            if pygame.mouse.get_pressed()[0]:
                grid.add_cell(*pygame.mouse.get_pos())

    window.fill('black')  
    grid.draw_grid(window)
    pygame.display.update()

pygame.quit()
exit()