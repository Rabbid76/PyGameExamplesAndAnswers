# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How to use a dictionary of images with sprite?
# https://stackoverflow.com/questions/66467383/how-to-use-a-dictionary-of-images-with-sprite/66514748#66514748
#
# GitHub - Grid - Chess board, checker texture
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_grid.md
#
# GitHub - Sprite, Group and Sprite mask - Drag Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-MouseDrag

import pygame

class DragOperator:
    def __init__(self, sprite):
        self.sprite = sprite
        self.dragging = False
        self.rel_pos = (0, 0)
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = self.sprite.rect.collidepoint(event.pos)
                self.rel_pos = event.pos[0] - self.sprite.rect.x, event.pos[1] - self.sprite.rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            if event.type == pygame.MOUSEMOTION and self.dragging:
                self.sprite.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]

class ChessSprite(pygame.sprite.Sprite):
    def __init__(self, board_rect, i, j, image):
        super().__init__() 
        self.board = board_rect
        self.image = image 
        self.set_pos(i, j)
        self.drag = DragOperator(self)
    def set_pos(self, i, j):
        x = self.board.left + self.board.width // 8 * i + self.board.width // 16
        y = self.board.left + self.board.height // 8 * (7 - j) + self.board.height // 16
        self.rect = self.image.get_rect(center = (x, y))
    def update(self, event_list):
        self.drag.update(event_list)
        if not self.drag.dragging:
            i = max(0, min(7, (self.rect.centerx - self.board.left) // (self.board.width // 8)))
            j = 7 - max(0, min(7, (self.rect.centery - self.board.top) // (self.board.height // 8)))
            self.set_pos(i, j)
        
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

board = pygame.Surface(window.get_size())
board.fill((255, 255, 255))
size = (min(window.get_size()) - 20) // 8
start = (window.get_width() - size * 8) // 2, (window.get_height() - size * 8) // 2
board_rect = pygame.Rect(*start, size*8, size*8)
ts, w, h, c1, c2 = 50, *window.get_size(), (128, 128, 128), (64, 64, 64)
for y in range(8):
    for x in range(8):
        color = (192, 192, 164) if (x+y) % 2 == 0 else (96, 64, 32)
        pygame.draw.rect(board, color, (start[0]+ x*size, start[1] + y*size, size, size))

# https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode
white_figures = { 'king': '♔', 'queen': '♕', 'rook': '♖', 'bishop': '♗', 'knight': '♘', 'pawn': '♙'}
black_figures = { 'king': '♚', 'queen': '♛', 'rook': '♜', 'bishop': '♝', 'knight': '♞', 'pawn': '♟'}

seguisy = pygame.font.SysFont("segoeuisymbol", size-4)
white_images = { k : seguisy.render(c, True, (255, 255, 255)) for k, c in white_figures.items() }
black_images = { k : seguisy.render(c, True, (0, 0, 0)) for k, c in black_figures.items() } 

group = pygame.sprite.Group()
figures = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
for i, figure in enumerate(figures):
    group.add(ChessSprite(board_rect, i, 0, white_images[figure]))
    group.add(ChessSprite(board_rect, i, 1, white_images['pawn']))
    group.add(ChessSprite(board_rect, i, 7, black_images[figure]))
    group.add(ChessSprite(board_rect, i, 6, black_images['pawn']))
   
run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    group.update(event_list)

    window.blit(board, (0, 0))
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
