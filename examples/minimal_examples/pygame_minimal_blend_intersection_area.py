# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Fill the area of intersection of two Circles in Pygame
# https://stackoverflow.com/questions/63058731/fill-the-area-of-intersection-of-two-circles-in-pygame/63060020#63060020
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Intersection area
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md
#
# https://replit.com/@Rabbid76/PyGame-CircleIntersection

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

pos1, rad1 = (window.get_width() // 2, window.get_height() // 2 - 20), 100
pos2, rad2 = (window.get_width() // 2, window.get_height() // 2 + 30), 80

surf1 = pygame.Surface(window.get_size(), pygame.SRCALPHA)
surf2 = pygame.Surface(window.get_size(), pygame.SRCALPHA)

pygame.draw.circle(surf1, (255, 0, 0, 255), pos1, rad1)
pygame.draw.circle(surf2, (255, 0, 0, 255), pos2, rad2)

surf1.blit(surf2, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
surf2.blit(surf1, (0, 0), special_flags = pygame.BLEND_RGBA_SUB)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
 
    window.fill((255, 255, 255))

    window.blit(surf2, (0, 0))     
    pygame.draw.circle(window, (128, 128, 128), pos1, rad1+1, 3)
    pygame.draw.circle(window, (128, 128, 128), pos2, rad2+1, 3)

    pygame.display.flip()

pygame.quit()
exit()