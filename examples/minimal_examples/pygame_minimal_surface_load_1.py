# pygame.image module
# https://www.pygame.org/docs/ref/image.html
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# What is a good way to draw images using pygame?
# https://stackoverflow.com/questions/8873219/what-is-a-good-way-to-draw-images-using-pygame
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

pygameSurface = pygame.image.load('icon/Apple1-256.png').convert_alpha()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((127, 127, 127))
    window.blit(pygameSurface, pygameSurface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()