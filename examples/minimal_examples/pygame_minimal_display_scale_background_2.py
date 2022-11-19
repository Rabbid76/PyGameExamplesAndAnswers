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

def transformScaleKeepRatio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    #scale = max(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size) 
    image_rect = scaled_image.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaled_image, image_rect

pygame.init()
window = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
clock = pygame.time.Clock()

background = pygame.image.load('image/sky1.png').convert_alpha()
scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())

run = True
while run == True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())

    window.fill((127, 127, 127))
    window.blit(scaled_bg, bg_rect)
    pygame.display.flip()

pygame.quit()
exit()