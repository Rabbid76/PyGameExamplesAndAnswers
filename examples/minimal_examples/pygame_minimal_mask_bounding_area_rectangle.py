# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How to get the correct dimensions for a pygame rectangle created from an image
# https://stackoverflow.com/questions/65361582/how-to-get-the-correct-dimensions-for-a-pygame-rectangle-created-from-an-image/65361896#65361896
#
# GitHub - Sprite, Group and Sprite mask - Mask bounding area rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-ImageHitbox

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

try:
    my_image = pygame.image.load('icon/Bomb-256.png')
except:
    my_image = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.circle(my_image, (0, 128, 0), (60, 60), 40)
    pygame.draw.circle(my_image, (0, 0, 128), (100, 150), 40)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos = window.get_rect().center
    my_image_rect = my_image.get_rect(center = pos)
    bounding_rect = my_image.get_bounding_rect()
    bounding_rect.move_ip(my_image_rect.topleft)
    
    window.fill((255, 255, 255))
    window.blit(my_image, my_image_rect)
    pygame.draw.rect(window, (0, 0, 0), my_image_rect, 3)
    pygame.draw.rect(window, (255, 0, 0), bounding_rect, 3)
    pygame.display.flip()

pygame.quit()
exit()