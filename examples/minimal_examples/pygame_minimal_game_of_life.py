# Conway's Game of Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
# Conway's Game of life pygame implementation not working with a copy of the grid, not using numpy
# https://stackoverflow.com/questions/62221456/conways-game-of-life-pygame-implementation-not-working-with-a-copy-of-the-grid/62221553#62221553
#
# GitHub - PyGameExamplesAndAnswers - Game of life
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_game_of_life.md

import pygame
import random

pygame.init()
window = pygame.display.set_mode((500, 500)) 
clock = pygame.time.Clock()

tile_size = 20
rows = window.get_width() // tile_size
cols = window.get_height() // tile_size

grid = [[0 for j in range(cols)] for i in range(rows)]

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

        copy_of_grid = []
        for row in grid:
            copy_of_grid.append(row[:])

        for y in range(rows):
            for x in range(cols):
                bl = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
                neighbors = sum(copy_of_grid[(y + i) % rows][(x + j) % cols] for i, j in bl)
                value = copy_of_grid[y][x]
                if value == 1 and (neighbors == 2 or neighbors == 3):
                    grid[y][x] = 1
                elif value == 0 and neighbors == 3:
                    grid[y][x] = 1
                else:
                    grid[y][x] = 0

    window.fill(0)
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 1:
                pygame.draw.rect(window, (255, 255, 255), (tile_size * x, tile_size * y, tile_size, tile_size))
    pygame.display.flip()

pygame.quit()
exit()
