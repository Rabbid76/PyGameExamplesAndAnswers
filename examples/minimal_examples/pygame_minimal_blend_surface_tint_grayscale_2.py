# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Changing ememy's color to show that it is aking damage?
# https://stackoverflow.com/questions/56209634/is-it-possible-to-change-sprite-colours-in-pygame/56210460?noredirect=1
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Change color of an image - Tint a grayscale image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md
#
# https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-4

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def changColor(image, color):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

pygame.init()
window = pygame.display.set_mode((300, 160))

image = pygame.image.load('icon/CarWhiteDragon256.png').convert_alpha()
hue = 0

clock = pygame.time.Clock()
nextColorTime = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    color = pygame.Color(0)
    color.hsla = (hue, 100, 50, 100)
    hue = hue + 1 if hue < 360 else 0 

    color_image = changColor(image, color)

    window.fill((96, 96, 64))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()