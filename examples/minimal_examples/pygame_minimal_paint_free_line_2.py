# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Cells are skipped when I move the mouse quickly
# https://stackoverflow.com/questions/68566210/cells-are-skipped-when-i-move-the-mouse-quickly/68566665#68566665
#
# GitHub - PyGameExamplesAndAnswers - Paint
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_paint.md

import pygame, math

cellsize = (5, 5)
mapSize = (int(600 / cellsize[0]), int(600 / cellsize[1]))
cells = [False for _ in range(mapSize[0] * mapSize[1])]

def cellAtPos(pos):
    c = (round(pos[0] / cellsize[0]), round(pos[1] / cellsize[1]))
    return c[1] * mapSize[0] + c[0]

pygame.init()
window = pygame.display.set_mode((600, 600))
mousePreviousFrame = pygame.mouse.get_pos()

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
  
    mouse = pygame.mouse.get_pressed()
    mousepos = pygame.mouse.get_pos()
    
    if mouse[0]:
        cells[cellAtPos(mousepos)] = True
    if mouse[0] and mousePreviousFrame[0]:
        direction = (mousepos[0] - mousePosPreviousFrame[0], mousepos[1] - mousePosPreviousFrame[1])
        mag = math.hypot(*direction)
        if mag != 0:
            norm_dir = (direction[0] / mag, direction[1] / mag)
            p = mousePosPreviousFrame
            for i in range(int(mag)):
                cells[cellAtPos((p[0] + norm_dir[0] * i, p[1] + norm_dir[1] * i))] = True

    mousePreviousFrame = mouse
    mousePosPreviousFrame = mousepos

    window.fill((255, 255, 255))
    for x in range(mapSize[0]):
        for y in range(mapSize[1]):
            if (cells[y * mapSize[0] + x]):
                pygame.draw.rect(window, (0, 0, 0), (x * cellsize[0], y * cellsize[1], cellsize[0], cellsize[1]))

    pygame.display.flip()

pygame.quit()
exit()