# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# SVG rendering in a PyGame application. Prior to Pygame 2.0, Pygame did not support SVG. Then how did you load it?
# https://stackoverflow.com/questions/120584/svg-rendering-in-a-pygame-application-prior-to-pygame-2-0-pygame-did-not-suppo/64598021#64598021
#
# Display SVG (as string) on Python Pygame
# https://stackoverflow.com/questions/65649933/display-svg-as-string-on-python-pygame/65651155#65651155  
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Surface and image, load SVG
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image_svg.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
import pygame
import io

def load_and_scale_svg(filename, scale):
    svg_string = open(filename, "rt").read()
    start = svg_string.find('<svg')    
    if start > 0:
        svg_string = svg_string[:start+4] + f' transform="scale({scale})"' + svg_string[start+4:]
    return pygame.image.load(io.BytesIO(svg_string.encode()))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

pygame_surface = load_and_scale_svg('clipart/Ice-001.svg', 0.4)

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