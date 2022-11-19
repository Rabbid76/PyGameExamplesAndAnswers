# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How do you draw an antialiased circular line of a certain thickness? How to set width on pygame.gfx.aacircle()?
# https://stackoverflow.com/questions/64816341/how-do-you-draw-an-antialiased-circular-line-of-a-certain-thickness-how-to-set/65353318#65353318
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw arc
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame
import pygame.gfxdraw

def drawAACircle(surf, color, center, radius, width):
    pygame.gfxdraw.aacircle(surf, *center, 100, color)  
    pygame.gfxdraw.aacircle(surf, *center, 100-width, color)  
    pygame.draw.circle(surf, color, center, radius, width)   

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    drawAACircle(window, (255, 0, 0), window.get_rect().center, 100, 20)
    pygame.display.flip()