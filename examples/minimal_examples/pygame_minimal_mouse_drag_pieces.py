# pygame.event.nt module
# https://www.pygame.org/docs/ref/event.nt.html
#
# Drawing square colour stored in a list of tuples?
# https://stackoverflow.com/questions/69828786/drawing-square-colour-stored-in-a-list-of-tuples/69828913#69828913 
#
# GitHub - Grid - Chess board, checker texture
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_grid.md
#
# GitHub - Mouse - Mouse Drag
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_event.nts.md

import pygame


BOARD_COLOURS = (34, 139, 34), (245, 211, 79)
PIECE_COLOUR = (128, 0, 0), (255, 239, 213)
ROWS, COLS = 8, 8
DIMS = 600
SQUARE = 600 // 8
RADIUS = SQUARE // 2 - 8

class Board:
    def __init__(self):
        self.board = [[(r + c) % 2 for c in range(COLS)] for r in range(ROWS)]
        for row in range(2):
            for col in range(8):
                if self.board[row][col] == 0:
                    self.board[row][col] = 2
                elif self.board[7 - row][col] == 0:
                    self.board[7 - row][col] = 3

    def draw(self, surf):
        for r in range(ROWS):
            for c in range(COLS):
                colour = BOARD_COLOURS[((r+c) % 2)]
                pygame.draw.rect(surf, colour, pygame.Rect(c*SQUARE, r*SQUARE, SQUARE, SQUARE))
                if self.board[r][c] >= 2:
                    colour = PIECE_COLOUR[((self.board[r][c])-2)]
                    x = SQUARE * c + SQUARE // 2
                    y = SQUARE * r + SQUARE // 2
                    pygame.draw.circle(surf, colour, (x, y), RADIUS)

pygame.init()
window = pygame.display.set_mode((DIMS, DIMS))
clock = pygame.time.Clock()

board = Board()
dragitem = None

run = True
while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] * COLS // DIMS
            row = event.pos[1] * ROWS // DIMS
            if board.board[row][col] > 1:
                dragitem = (row, col, board.board[row][col])
                board.board[row][col] = (row + col) % 2 == 0
                dragpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP and dragitem and dragpos:
            new_col = event.pos[0] * COLS // DIMS
            new_row = event.pos[1] * ROWS // DIMS
            if board.board[new_row][new_col] < 1:
                board.board[dragitem[0]][dragitem[1]] = (dragitem[0] + dragitem[1]) % 2
                board.board[new_row][new_col] = dragitem[2]
            else:
                board.board[dragitem[0]][dragitem[1]] = dragitem[2]
            dragpos = None
            dragitem = None
        if event.type == pygame.MOUSEMOTION and dragitem:
            dragpos = event.pos

    window.fill(0)
    board.draw(window)
    if dragitem:
        pygame.draw.circle(window, PIECE_COLOUR[dragitem[2]-2], dragpos, RADIUS)
    pygame.display.flip()

pygame.quit()
exit()