# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# How do I create an extendable bar sprite in PyGame?
# https://stackoverflow.com/questions/75561432/how-do-i-create-an-extendable-bar-sprite-in-pygame/75561623#75561623
#
# GitHub - PyGameExamplesAndAnswers - Scale and zoom - Transform scale and zoom surface
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_scale_and_zoom.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((200, 100))
clock = pygame.time.Clock()

bar = pygame.image.load('icon/ScrollBar.png').convert_alpha()c

def scale_bar(image, width):
    size = image.get_size()
    margin = 4
    middel_parat = image.subsurface(pygame.Rect(margin, 0, size[0]-margin*2, size[1]))
    scaled_image = pygame.Surface((width, size[1]))
    scaled_image.blit(image, (0, 0), (0, 0, margin, size[1]))
    scaled_image.blit(pygame.transform.smoothscale(middel_parat, (width-margin*2, size[1])), (margin, 0))
    scaled_image.blit(image, (width-margin, 0), (size[0]-margin, 0, margin, size[1]) )
    return scaled_image

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    scaled_image = scale_bar(bar, 100)

    window.fill(0)
    window.blit(scaled_image, scaled_image.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()