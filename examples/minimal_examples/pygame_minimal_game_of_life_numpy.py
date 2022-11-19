# Conway's Game of Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
# Pygame is running game of life very slowly
# https://stackoverflow.com/questions/69056318/pygame-is-running-game-of-life-very-slowly/69056448#69056448
#
# GitHub - PyGameExamplesAndAnswers - Game of life
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_game_of_life.md

import pygame
import numpy
from scipy.ndimage import convolve

pygame.init()
window = pygame.display.set_mode((500, 400)) 
clock = pygame.time.Clock()

tile_size = 20
cols = window.get_width() // tile_size
rows = window.get_height() // tile_size

kernel = numpy.array([[1,1,1], [1,0,1], [1,1,1]])
lookup = numpy.array([0,0,0,1,0,0,0,0,0, 0,0,1,1,0,0,0,0,0])
grid = numpy.zeros((rows, cols), dtype=int)

# Toad
grid[4][5] = 1
grid[5][5] = 1
grid[5][6] = 1
grid[6][5] = 1
grid[6][6] = 1
grid[7][6] = 1

# Blinker
grid[15][10] = 1
grid[15][11] = 1
grid[15][12] = 1

run_game_of_life = True
run = True
while run:
    clock.tick(10)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            run_game_of_life = not run_game_of_life
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            print(posX, posY)
            posX, posY = int(posX / tile_size), int(posY / tile_size)
            grid[posY][posX] = 1 - grid[posY][posX]

    if run_game_of_life:
        adjacent = convolve(grid, kernel, mode='constant')
        new_grid = lookup[grid * 9 + adjacent]
        grid = new_grid

    color_grid = numpy.repeat((grid * 255).astype('uint8').reshape(rows, cols, 1), 3, axis = 2)
    grid_surf = pygame.image.frombuffer(color_grid.flatten(), (cols, rows), 'RGB')
    grid_surf = pygame.transform.scale(grid_surf, (cols*tile_size, rows*tile_size))

    window.fill(0)
    window.blit(grid_surf, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()
