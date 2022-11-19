# pygame.image module
# https://www.pygame.org/docs/ref/image.html
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How do I blit a PNG with some transparency onto a surface in Pygame?
# https://stackoverflow.com/questions/1634208/how-do-i-blit-a-png-with-some-transparency-onto-a-surface-in-pygame/64630678#64630678
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md
#
# https://replit.com/@Rabbid76/PyGame-LoadTransparentImage

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

pygameSurface = pygame.image.load('icon/Porthole_256.png').convert_alpha()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (160, 160, 160), (192, 192, 192)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    window.blit(pygameSurface, pygameSurface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()