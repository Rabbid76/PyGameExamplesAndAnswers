# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How to free transform image in pygame?
# https://stackoverflow.com/questions/77714070/trianglular-picture-in-pygame/77714179#77714179
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Clipping with masks
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def clip_surface(surf, mask):
    return mask.to_surface(setsurface = surf.convert_alpha(), unsetcolor = (0, 0, 0, 0))

def checker_image(ts, w, h, c1, c2):
    surf = pygame.Surface((w, h))
    [pygame.draw.rect(surf, c1 if (x+y) % 2 == 0 else c2, (x*ts, y*ts, ts, ts)) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
    return surf

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

try:
    image = pygame.image.load('icon/Apple1-256.png')
except:
    image = checker_image(20, 200, 200, (255, 128, 128), (255, 64, 64))
image = pygame.transform.scale(image, (200, 200))

background = checker_image(40, *window.get_size(), (129, 128, 128), (96, 96, 96))
mask_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
pygame.draw.polygon(mask_image, (255, 255, 255), [(100, 200), (0, 0), (200, 0)])
mask = pygame.mask.from_surface(mask_image)

clipped_image = clip_surface(image, mask)
image.set_alpha(127)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.blit(background, (0, 0))
    image_rect = clipped_image.get_rect(center = window.get_rect().center)
    window.blit(image, image_rect)
    window.blit(clipped_image, image_rect)
    pygame.draw.rect(window, (0, 0, 0), image_rect, 3)
    pygame.draw.polygon(window, (255, 0, 0), [(150, 250), (50, 50), (250, 50)], 1)
    pygame.display.flip()

pygame.image.save(window, 'c:/temp/ss.png')
pygame.quit()
exit()