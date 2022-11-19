# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# How can I visualize the overlapping area of 2 masks in pygame?
# https://stackoverflow.com/questions/70485132/how-can-i-visualize-the-overlapping-area-of-2-masks-in-pygame/70485262#70485262
#
# GitHub - PyGameExamplesAndAnswers - Mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SurfaceLineMaskIntersect-2

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

import pygame, math

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

image1 = pygame.image.load("icon/Banana64.png")
image2 = pygame.image.load("icon/Bird64.png")
rect1 = image1.get_rect(center = (165, 150))
rect2 = image1.get_rect(center = (135, 150))
mask1 = pygame.mask.from_surface(image1)
mask2 = pygame.mask.from_surface(image2)

angle = 0
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    angle += 0.01
    rect1.centery = 150 + round(60 * math.sin(angle))        

    offset_x = rect2.x - rect1.x
    offset_y = rect2.y - rect1.y
    overlap_mask = mask1.overlap_mask(mask2, (offset_x, offset_y))
    overlap_surf = overlap_mask.to_surface(setcolor = (255, 0, 0))
    overlap_surf.set_colorkey((0, 0, 0))

    window.fill(0)
    window.blit(image1, rect1)
    window.blit(image2, rect2)
    window.blit(overlap_surf, rect1)
    pygame.display.flip()

pygame.quit()
exit()