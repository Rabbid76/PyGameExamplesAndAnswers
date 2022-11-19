# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# How to scale images to screen size in Pygame
# https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame/73384976#73384976
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Scale background
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

background = pygame.image.load('image/sky1.png').convert()
background = pygame.transform.smoothscale(background, window.get_size())

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()