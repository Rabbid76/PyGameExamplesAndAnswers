# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html
#
# How to detect when a sprite is clicked
# https://stackoverflow.com/questions/58917346/how-to-detect-when-a-sprite-is-clicked/58935218#58935218
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Click on rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_rectangle.md

import pygame

pygame.init()

def drawRectHighlight(surface, rect, color, highlightColor, point):
    pygame.draw.rect(
        surface,
        highlightColor if rect.collidepoint(point) else color,
        rect)

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    w, h = window.get_size()
    rectangles = [pygame.Rect(0, 0, w // 3, h // 3) for _ in range(4)]
    for i in range(4): 
        rectangles[i].center = w // 4 + (i // 2) * w // 2, h // 4 + (i % 2) * h // 2 
    colors = [(64, 0, 0), (0, 64, 0), (0, 0, 64), (64, 64, 0)]
    hightlightColors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

    point = pygame.mouse.get_pos()

    window.fill('black')
    for r, c, h in zip(rectangles, colors, hightlightColors):
        drawRectHighlight(window, r, c, h, point)
    pygame.display.flip()

pygame.quit()
exit()