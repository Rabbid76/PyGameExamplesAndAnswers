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

pygame.init()
window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()

#svg_string = ""
#with open('clipart/Ice-001.svg', "rt") as f:
#    svg_string = f.read()

svg_string = '<svg height="100" width="500"><ellipse cx="240" cy="50" rx="220" ry="30" style="fill:yellow" /><ellipse cx="220" cy="50" rx="190" ry="20" style="fill:white" /></svg>'
svg_string = '<svg height="200" width="200"><ellipse cx="100" cy="100" rx="100" ry="100" style="fill:yellow"/></svg>'
pygame_surface = pygame.image.load(io.BytesIO(svg_string.encode()))
#pygame_surface = pygame.image.load(io.BytesIO(svg_string.encode(encoding="utf-8")))

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
