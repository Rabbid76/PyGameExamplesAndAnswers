# pygame.image module
# https://www.pygame.org/docs/ref/image.html
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Adjust image of rect
# https://stackoverflow.com/questions/66443304/adjust-image-of-rect/66443370#66443370 
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Transformation - Scroll
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

# https://replit.com/@Rabbid76/PyGame-Scroll

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def scroll_y(surf, dy):
    scroll_surf = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
    scroll_surf.blit(surf, (0, dy))
    if dy > 0:
        scroll_surf.blit(surf, (0, dy-surf.get_height()))
    else:
        scroll_surf.blit(surf, (0, surf.get_height()+dy))
    return scroll_surf

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (64, 64, 64), (96, 96, 96)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

rain_surf = pygame.image.load('icon/Raindrops256.png').convert_alpha()
rain_surf = pygame.transform.smoothscale(rain_surf, window.get_size())
dy = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window_center = window.get_rect().center
    scroll_surf = scroll_y(rain_surf, dy)
    dy = (dy + 1) % rain_surf.get_height()

    window.blit(background, (0, 0))
    window.blit(scroll_surf, scroll_surf.get_rect(center = window_center))
    pygame.display.flip()

pygame.quit()
exit()