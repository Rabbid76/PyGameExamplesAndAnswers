# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# Making a clickable grid using Pygame
# https://stackoverflow.com/questions/73835007/making-a-clickable-grid-using-pygame/73835336#73835336
#
# GitHub - Grid
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_grid.md

import pygame

class Cell:
    def __init__(self):
        self.clicked = False

grid_size, cell_size = 10, 20
board = [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:    
            if event.button == 1:
                row = event.pos[1] // cell_size
                col = event.pos[0] // cell_size
                board[row][col].clicked = True

    window.fill('black')
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            color = (64, 64, 64) if cell.clicked else (164, 164, 164)
            cell_rect = pygame.Rect(ix*cell_size+1, iy*cell_size+1, cell_size-2, cell_size-2)
            pygame.draw.rect(window, color, cell_rect)
    pygame.display.flip()

pygame.quit()
exit()