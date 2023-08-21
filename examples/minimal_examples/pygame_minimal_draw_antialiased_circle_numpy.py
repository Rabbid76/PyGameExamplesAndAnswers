# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How do you draw an antialiased circular line of a certain thickness? How to set width on pygame.gfx.aacircle()?
# https://stackoverflow.com/questions/64816341/how-do-you-draw-an-antialiased-circular-line-of-a-certain-thickness-how-to-set/65353318#65353318
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw arc
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame
import numpy

def drawAACircle(surf, color, center, radius):
    f_circle = lambda i, j: numpy.clip(radius - numpy.hypot(i-radius-1, j-radius-1), 0, 1) * 255
    shape = (radius*2+4, radius*2+4)
    circle_rgb = numpy.full((*shape, len(color)), color, dtype = numpy.uint8)
    circle_alpha = numpy.fromfunction(f_circle, shape).astype(numpy.uint8).reshape((*shape, 1))
    circle_array = numpy.concatenate((circle_rgb, circle_alpha), 2)
    circle_surface = pygame.image.frombuffer(circle_array.flatten(), shape, 'RGBA')
    surf.blit(circle_surface, circle_surface.get_rect(center = center))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((32, 32, 32))
    drawAACircle(window, (255, 0, 0), window.get_rect().center, 100)
    pygame.display.flip()

pygame.quit()
exit()