# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# how to make circular surface in pygame
# https://stackoverflow.com/questions/64075338/how-to-make-circular-surface-in-pygame/64075812#64075812
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Circular clipping region
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md
#
# https://replit.com/@Rabbid76/PyGame-ClipCircularRegion-1

import pygame
pygame.init()
window = pygame.display.set_mode((250, 250))

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (255, 255, 255), (255, 0, 0)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

size = background.get_size()
cropped_background = pygame.Surface(size, pygame.SRCALPHA)
pygame.draw.ellipse(cropped_background, (255, 255, 255, 255), (0, 0, *size))
cropped_background.blit(background, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    window.fill(0)
    window.blit(cropped_background, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()