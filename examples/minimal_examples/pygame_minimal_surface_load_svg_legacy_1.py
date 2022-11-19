# pynanosvg 
# 
# pip install Cython
# pip install pynanosvg
#
#    - https://github.com/ethanhs/pynanosvg
#    - https://pypi.org/project/pynanosvg/
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
from svg import Parser, Rasterizer
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def load_svg(filename, scale=None, size=None, clip_from=None, fit_to=None, foramt='RGBA'):
    svg = Parser.parse_file(filename)
    scale = min((fit_to[0] / svg.width, fit_to[1] / svg.height)
                if fit_to else ([scale if scale else 1] * 2))
    width, height = size if size else (svg.width, svg.height)
    surf_size = round(width * scale), round(height * scale)
    buffer = Rasterizer().rasterize(svg, *surf_size, scale, *(clip_from if clip_from else 0, 0))
    return  pygame.image.frombuffer(buffer, surf_size, foramt)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

pygameSurface = load_svg('clipart/Ice-001.svg', fit_to = (window.get_width()*3//4, window.get_height()))

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