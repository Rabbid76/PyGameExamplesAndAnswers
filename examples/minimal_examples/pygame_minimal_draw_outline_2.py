# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Why am I not getting appropriate values for the outline I am creating - mask with pygame
# https://stackoverflow.com/questions/73716557/why-am-i-not-getting-appropriate-values-for-the-outline-i-am-creating-mask-wit/74172766#74172766
#
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Outline
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

surface = pygame.image.load('icon/Apple1-256.png')
mask = pygame.mask.from_surface(surface)
outline = mask.outline(3)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window_center = window.get_rect().center
    rect = surface.get_rect(center = window_center)
    window_points = [(p[0] + rect.x, p[1] + rect.y) for p in outline]

    window.fill('black')
    window.blit(surface, rect)
    pygame.draw.lines(window, "white", True, window_points, 5)
    pygame.display.flip()

#pygame.image.save(window, 'otl.png')
pygame.quit()
exit()