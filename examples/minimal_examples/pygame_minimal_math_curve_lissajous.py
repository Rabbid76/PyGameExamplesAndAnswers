# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Lissajous curve
# https://en.wikipedia.org/wiki/Lissajous_curve
#
# How to Get the X and Y Positions of All Curves in a Lissajous Curve Table?
# https://stackoverflow.com/questions/55076531/how-to-get-the-x-and-y-positions-of-all-curves-in-a-lissajous-curve-table/55076619#55076619
#
# GitHub - PyGameExamplesAndAnswers - Math and Vector- Curve - Lissajous curve
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_math_vector_and_reflection.md
#
# https://replit.com/@Rabbid76/PyGame-LissajousCurve

import math
import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

angle = 0
tile_size = window.get_width() // 10
columns = window.get_width() // tile_size - 1
rows = window.get_height() // tile_size - 1
radius = (tile_size - 10) // 2

surf = pygame.Surface((tile_size, tile_size))
surf.fill((32, 0, 32))
grid = [[surf.copy() for i in range(columns)] for j in range(rows)]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    lx = [(c-1, c*tile_size + tile_size//2, round(radius * math.cos(angle*c)), round(radius * math.sin(angle*c))) for c in range(1, columns+1)]
    ly = [(r-1, r*tile_size + tile_size//2, round(radius * math.cos(angle*r)), round(radius * math.sin(angle*r))) for r in range(1, rows+1)]
    angle += 0.01

    for column, cx, x, y_ in lx:
        for row, cy, x_, y in ly:
            grid[column][row].set_at((x + tile_size // 2, y + tile_size // 2), (255, 255, 255))


    window.fill((0, 0, 0))

    for column, grid_row in enumerate(grid):
        for row, cell_surf in enumerate(grid_row):
            cx = (column + 1) * tile_size
            cy = (row + 1) * tile_size
            window.blit(cell_surf, (cx, cy))

    cy = tile_size // 2
    for column, cx, x, y in lx:
        pygame.draw.circle(window, (127, 127, 127), (cx, cy), radius, 1)
        pygame.draw.circle(window, (127, 127, 127), (x + cx, y + cy), 5)
        pygame.draw.line(window, (127, 127, 127), (cx + x, cy + y), (cx + x, window.get_height()), 1)
        
    cx = tile_size // 2   
    for row, cy, x, y in ly:
        pygame.draw.circle(window, (127, 127, 127), (cx, cy), radius, 1)
        pygame.draw.circle(window, (127, 127, 127), (x + cx, y + cy), 5)
        pygame.draw.line(window, (127, 127, 127), (cx + x, cy + y), (window.get_width(), cy + y), 1)
    
    for pos in [(x[1] + x[2], y[1] + y[3]) for x in lx for y in ly]:
        pygame.draw.circle(window, (255, 0, 0), pos, 3)

    pygame.display.flip()

pygame.quit()
exit()