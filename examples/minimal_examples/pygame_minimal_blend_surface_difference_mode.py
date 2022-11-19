# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How to get the Difference blending mode?
# https://stackoverflow.com/questions/67737854/how-to-get-the-difference-blending-mode/67737939#67737939
#
# GitHub - PyGameExamplesAndAnswers - vBlending and transparency - Blending
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

image1 = pygame.transform.scale(pygame.image.load('texture/ObjectSheet.png').convert(), (256, 256))
image2 = pygame.image.load('texture/woodtiles.jpg')
temp_image = image1.copy() 
temp_image.blit(image2, (0, 0), special_flags = pygame.BLEND_RGBA_SUB)
final_image = image2.copy() 
final_image.blit(image1, (0, 0), special_flags = pygame.BLEND_RGBA_SUB)
final_image.blit(temp_image, (0, 0), special_flags = pygame.BLEND_RGBA_MAX)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.fill((255, 255, 255))
    window.blit(final_image, (20, 20))
    pygame.display.flip()

pygame.quit()
exit()