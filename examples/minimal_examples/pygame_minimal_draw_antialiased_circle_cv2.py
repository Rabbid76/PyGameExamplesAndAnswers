# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How do you draw an antialiased circular line of a certain thickness? How to set width on pygame.gfx.aacircle()?
# https://stackoverflow.com/questions/64816341/how-do-you-draw-an-antialiased-circular-line-of-a-certain-thickness-how-to-set/65353318#65353318
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw arc
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame
import cv2
import numpy

def drawAACircle(surf, color, center, radius, width):
    circle_image = numpy.zeros((radius*2+4, radius*2+4, 4), dtype = numpy.uint8)
    circle_image = cv2.circle(circle_image, (radius+2, radius+2), radius-width//2, (*color, 255), width, lineType=cv2.LINE_AA)  
    circle_surface = pygame.image.frombuffer(circle_image.flatten(), (radius*2+4, radius*2+4), 'RGBA')
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
    drawAACircle(window, (255, 0, 0), window.get_rect().center, 100, 20)
    pygame.display.flip()