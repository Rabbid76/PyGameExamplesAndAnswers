# pygame.image module
# https://www.pygame.org/docs/ref/image.html
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How do you load all images at a time in pygame?
# https://stackoverflow.com/questions/67141356/how-do-you-load-all-images-at-a-time-in-pygame/67141422#67141422
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/Load multiple images.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

path = 'icon'
filenames = [f for f in os.listdir(path) if f.endswith('.png')]

images = {}
for name in filenames:
    imagename = os.path.splitext(name)[0] 
    images[imagename] = pygame.image.load(os.path.join(path, name)).convert_alpha()

for name in filenames:
    imagename = os.path.splitext(name)[0] 
    globals()[imagename] =  pygame.image.load(os.path.join(path, name)).convert_alpha()

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
    window.blit(images['Watermelon64'], images['Watermelon64'].get_rect(center = (100, 100)))
    window.blit(Plums64, Plums64.get_rect(center = (200, 100)))
    window.blit(images['Apple64'], images['Apple64'].get_rect(center = (100, 200)))
    window.blit(Pear64, Pear64.get_rect(center = (200, 200)))
    pygame.display.flip()

pygame.quit()
exit()
