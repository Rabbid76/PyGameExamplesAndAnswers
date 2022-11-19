# PIL PyGame:
#
#    - PIL and pygame.image
#    - https://stackoverflow.com/questions/25202092/pil-and-pygame-image
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# PIL and pygame.image
# https://stackoverflow.com/questions/25202092/pil-and-pygame-image/64182629#64182629
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load Pillow image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import os
import pygame
from PIL import Image
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

pilImage = Image.open('icon/Ball1-256.png')
pygameSurface = pilImageToSurface(pilImage)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(pygameSurface, pygameSurface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()