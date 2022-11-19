# Tetris generating coloured shapes from blocks
# https://stackoverflow.com/questions/66765536/tetris-generating-coloured-shapes-from-blocks/66767879#66767879
#   
# GitHub - PyGameExamplesAndAnswers - Tetris
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_tetris.md

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

tile_size = 20
red_tile = pygame.Surface((tile_size, tile_size))
red_tile.fill("red")
blue_tile = pygame.Surface((tile_size, tile_size))
blue_tile.fill("blue")
green_tile = pygame.Surface((tile_size, tile_size))
green_tile.fill("green")
yellow_tile = pygame.Surface((tile_size, tile_size))
yellow_tile.fill("yellow")

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    # [...] add more
]

def draw_shape(x, y, tile_index, surf):
    w, h = surf.get_size()
    for pos in shapes[tile_index]:
        window.blit(surf, (x + pos[0]*w, y + pos[1]*h))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.fill(0)
    draw_shape(70, 70, 0, red_tile)
    draw_shape(170, 70, 1, blue_tile)
    draw_shape(70, 170, 2, green_tile)
    draw_shape(170, 170, 3, yellow_tile)
    pygame.display.flip()

pygame.quit()
exit()