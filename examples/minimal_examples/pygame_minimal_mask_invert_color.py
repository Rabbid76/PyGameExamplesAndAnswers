# How can i optimize the code of inversion mask in Pygame
# https://stackoverflow.com/questions/78532738/how-can-i-optimize-the-code-of-inversion-mask-in-pygame/78534477#78534477
#
# GitHub - Sprite, Group and Sprite mask - Sprite mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 683))
clock = pygame.time.Clock()

image = pygame.image.load('image/parrot1.png').convert_alpha()

inversionMaskImage = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(inversionMaskImage, (255, 255, 255), inversionMaskImage.get_rect().center, inversionMaskImage.get_width()//2)
mask = pygame.mask.from_surface(inversionMaskImage)
inversionMask = mask.to_surface(setcolor=(255, 255, 255, 255), unsetcolor=(0, 0, 0, 0))

def invert_surface(surface, mask, sx, sy):
    areaRect = pygame.Rect((sx, sy), mask.get_size())
    clipRect = areaRect.clip(surface.get_rect())
    subSurface = surface.subsurface(clipRect)
    finalImage = mask.copy()
    finalImage.blit(subSurface, (clipRect.x - areaRect.x, clipRect.y - areaRect.y), special_flags = pygame.BLEND_SUB)
    return finalImage

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    areaRect = pygame.Rect(pygame.mouse.get_pos(), (0, 0)).inflate(inversionMask.get_size())
    invertedArea = invert_surface(image, inversionMask, areaRect.x, areaRect.y)

    screen.fill('black')
    screen.blit(image, (0, 0))
    screen.blit(invertedArea, areaRect)
    pygame.display.flip()

pygame.quit()
exit()