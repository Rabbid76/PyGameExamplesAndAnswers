# pynanosvg 
# 
# pip install svglib
#
#    - https://pypi.org/project/svglib/
#    - https://github.com/deeplook/svglib
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# SVG rendering in a PyGame application. Prior to Pygame 2.0, Pygame did not support SVG. Then how did you load it?
# https://stackoverflow.com/questions/120584/svg-rendering-in-a-pygame-application-prior-to-pygame-2-0-pygame-did-not-suppo/64598021#64598021
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Surface and image, load SVG
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image_svg.md

import os
import pygame
from svglib.svglib import svg2rlg
import io

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def identity_color_converter(c):
    return c

def load_svg(filename):
    drawing = svg2rlg(filename, color_converter=identity_color_converter)
    str = drawing.asString("png")
    byte_io = io.BytesIO(str)
    return pygame.image.load(byte_io)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

pygame_surface = load_svg('clipart/Ice-001.svg')
size = pygame_surface.get_size()
scale = min(window.get_width() / size[0], window.get_width() / size[1]) * 0.8
pygame_surface = pygame.transform.scale(pygame_surface, (round(size[0] * scale), round(size[1] * scale)))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((127, 127, 127))
    window.blit(pygame_surface, pygame_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()