# Diagonal lines of squares in grids
# https://stackoverflow.com/questions/16499848/diagonal-lines-of-squares-in-grids/74072623#74072623 
#
# GitHub - Grid
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_grid.md

import pygame

pygame.init()
window = pygame.display.set_mode((350, 350))
clock = pygame.time.Clock()

grid_x, grid_y = 25, 25
tile_size, rows, columns = 20, 15, 15

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
    mx, my = pygame.mouse.get_pos()
    column, row = (mx - grid_x) // tile_size, (my - grid_y)  // tile_size
    cells_on_diagonals = []
    if 0 <= column < columns and 0 <= row < rows:
        cells_on_diagonals.append((row, column))
        for dir in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            rn, cn = row + dir[1], column + dir[0]
            while 0 <= cn < columns and 0 <= rn < rows:
                cells_on_diagonals.append((rn, cn))
                rn += dir[1]
                cn += dir[0]

    window.fill('black')
    for row in range(rows):
        for column in range(columns):
            if (row, column) in cells_on_diagonals:
                rect = (grid_x + column*tile_size, grid_y + row*tile_size, tile_size, tile_size)
                pygame.draw.rect(window, "red", rect)
    for column in range(columns+1):
        x = grid_x + column*tile_size
        pygame.draw.line(window, "white", (x, grid_y), (x, grid_x + rows*tile_size))
    for row in range(rows+1):
        y = grid_y + row*tile_size
        pygame.draw.line(window, "white", (grid_x, y), (grid_x + columns*tile_size, y))
    pygame.display.flip()

pygame.quit()
exit()
