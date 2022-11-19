# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Changing ememy's color to show that it is aking damage?
# https://stackoverflow.com/questions/63734429/changing-ememys-color-to-show-that-it-is-aking-damage/63745242#63745242
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Change color of an image - Change the color of a surface area (mask)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md
# 
# https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-2

import pygame
import random
#import os
#os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c:/temp'))

pygame.init()
window = pygame.display.set_mode((200, 200))

image = pygame.Surface((128, 128), pygame.SRCALPHA)
image.fill((0, 0, 0, 0))
pygame.draw.rect(image, (255, 128, 64), (8, 8, 112, 112))
for cpt in [(64, 64), (32, 32), (96, 32), (32, 96), (96, 96)]:
    pygame.draw.circle(image, (0, 0, 0), cpt, 8)
#pygame.image.save(image, 'TestImage1.jpg')

maskImage = pygame.Surface((128, 128))
for cpt in [(64, 64), (32, 32), (96, 32), (32, 96), (96, 96)]:
    pygame.draw.circle(maskImage, (255, 255, 255), cpt, 8)
#pygame.image.save(maskImage, 'TestImageMask1.bmp')

def changColor(image, maskImage, newColor):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(newColor)
    
    masked = maskImage.copy()
    masked.set_colorkey((0, 0, 0))
    masked.blit(colouredImage, (0, 0), None, pygame.BLEND_RGBA_MULT)

    finalImage = image.copy()
    finalImage.blit(masked, (0, 0), None)

    return finalImage

clock = pygame.time.Clock()
nextColorTime = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    currentTime = pygame.time.get_ticks()
    if nextColorTime <= currentTime:
        nextColorTime = currentTime + 1000
        newColor = [random.randrange(255) for _ in range(3)]
        coloredImage = changColor(image, maskImage, newColor)

    window.fill((255, 255, 255))
    window.blit(coloredImage, (36, 36))
    pygame.display.flip()

pygame.quit()
exit()