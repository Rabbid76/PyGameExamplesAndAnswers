# How to make a “while mouse down” loop in pygame
# https://stackoverflow.com/questions/54666587/how-to-make-a-while-mouse-down-loop-in-pygame/54667247#54667247 
#
# GitHub - Paint
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_paint.md

import pygame
import random
pygame.init()

window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def airbrush(surf, color, brushSize):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        pos = cur[0] + random.randrange(brushSize), cur[1] + random.randrange(brushSize)
        radius = random.randrange(1, 5)
        pygame.draw.circle(surf, color, pos, radius)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    airbrush(window, (255, 0, 0), 20)
    pygame.display.flip()

pygame.quit()
exit()