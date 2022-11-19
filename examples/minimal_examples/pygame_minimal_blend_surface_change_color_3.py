# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Changing ememy's color to show that it is aking damage?
# https://stackoverflow.com/questions/63734429/changing-ememys-color-to-show-that-it-is-aking-damage/63745242#63745242
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Change color of an image - Change the color of a surface area (mask)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md
#
# https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-3

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def changColor(image, maskImage, newColor):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(newColor)
    
    masked = maskImage.copy()
    masked.set_colorkey((0, 0, 0))
    masked.blit(colouredImage, (0, 0), None, pygame.BLEND_RGBA_MULT)

    finalImage = image.copy()
    finalImage.blit(masked, (0, 0), None)

    return finalImage

pygame.init()
window = pygame.display.set_mode((404, 84))

image = pygame.image.load('icon/avatar64.png').convert_alpha()
maskImage = pygame.image.load('icon/avatar64mask.png').convert_alpha()

colors = []
for hue in range (0, 360, 60):
    colors.append(pygame.Color(0))
    colors[-1].hsla = (hue, 100, 50, 100)

images = [changColor(image, maskImage, c) for c in colors]

clock = pygame.time.Clock()
nextColorTime = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    for i, image in enumerate(images):
        window.blit(image, (10 + i * 64, 10))
    pygame.display.flip()

pygame.quit()
exit()