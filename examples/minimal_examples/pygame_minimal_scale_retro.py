# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Pygame + PyOpenGL Resolution Downscaling
# https://stackoverflow.com/questions/76795854/pygame-pyopengl-resolution-downscaling/76796567#76796567
#
# GitHub - PyGameExamplesAndAnswers - Scale and zoom - Transform scale and zoom surface
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_scale_and_zoom.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
import pygame

pygame.init()
window = pygame.display.set_mode((320, 320))
clock = pygame.time.Clock()

scale = 16
display = pygame.Surface((window.get_width() // scale, window.get_height() // scale))

surf = pygame.image.load('icon/sunglasses.png').convert_alpha()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill('gray')
    display.blit(surf, surf.get_rect(center = display.get_rect().center))
    
    scaled_disaply = pygame.transform.scale_by(display, scale)
    window.blit(scaled_disaply, (0, 0))
    pygame.display.flip()

#pygame.image.save(window, "pygame_opengl_surface_to_texture_scaled.png")

pygame.quit()
exit()