# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# wondering about pixel perfect mousepointer collision in the case of a button
# https://stackoverflow.com/questions/70338690/pygame-wondering-about-pixel-perfect-mousepointer-collision-in-the-case-of-a-b/70338984#70338984
#
# GitHub - PyGameExamplesAndAnswers - Mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mask.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

image = pygame.image.load('icon/Banana64.png')
image_rect = image.get_rect(center = window.get_rect().center)
image_mask = pygame.mask.from_surface(image)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    color = (0, 0, 0)
    mouse_pos = pygame.mouse.get_pos()
    if image_rect.collidepoint(mouse_pos):
        mask_x = mouse_pos[0] - image_rect.left
        mask_y = mouse_pos[1] - image_rect.top
        if image_mask.get_at((mask_x, mask_y)):
            color = (255, 0, 0)

    window.fill(color)
    window.blit(image, image_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
