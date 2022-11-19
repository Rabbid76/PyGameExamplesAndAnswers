# Recursive Fractal Pygame - Not Displaying Shapes
# https://stackoverflow.com/questions/30140671/recursive-fractal-pygame-not-displaying-shapes/69036894#69036894
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Fractal
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md
#
# https://replit.com/@Rabbid76/PyGame-BarnsleysFern

import pygame

def recursiveSquare(surf, x, y, side, color, level):
    global done
    if level and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        rect = pygame.Rect(x - side/2, y - side/2, side, side)
        pygame.draw.rect(surf, color, rect)
        pygame.display.flip()
        clock.tick(FPS)

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    recursiveSquare(surf, x + side*i, y + side*j, side/3, color, level - 1)

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sierpinski Carpet")
clock = pygame.time.Clock()
FPS = 0
level = 5

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    window.fill((255, 255, 255))
    recursiveSquare(window, *window.get_rect().center, window.get_width()/3, (0, 0, 0), level)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
quit()