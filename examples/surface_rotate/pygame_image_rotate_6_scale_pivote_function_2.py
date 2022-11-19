# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Rotating and scaling an image around a pivot, while scaling width and height separately in Pygame
# https://stackoverflow.com/questions/70819750/rotating-and-scaling-an-image-around-a-pivot-while-scaling-width-and-height-sep/70820034#70820034
#
# How to rotate an image around its center while its scale is getting larger(in Pygame)
# https://stackoverflow.com/questions/54462645/how-to-rotate-an-image-around-its-center-while-its-scale-is-getting-largerin-py/54713639#54713639
#
# How to set the pivot point (center of rotation) for pygame.transform.rotate()?
# https://stackoverflow.com/questions/15098900/how-to-set-the-pivot-point-center-of-rotation-for-pygame-transform-rotate/69312319#69312319
#
# https://replit.com/@Rabbid76/PyGame-RotateZoomPivot#main.py
#
# https://replit.com/@Rabbid76/PyGame-RotateZoomPivot-Example#main.py

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

def blitRotateZoomXY(surf, original_image, origin, pivot, angle, scale_x, scale_y):

    image_rect = original_image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(origin) - image_rect.center
    offset_center_to_pivot.x *= scale_x
    offset_center_to_pivot.y *= scale_y
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)
    scaled_image = pygame.transform.smoothscale(original_image, (image_rect.width * scale_x, image_rect.height * scale_y))
    rotozoom_image = pygame.transform.rotate(scaled_image, angle)
    rect = rotozoom_image.get_rect(center = rotated_image_center)

    surf.blit(rotozoom_image, rect)

cannon = pygame.image.load('icon/cannon.png')
cannon_mount = pygame.image.load('icon/cannon_mount.png')

angle, zoom_x, zoom_y = -90, 1, 1
stage = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/3, screen.get_height()*3/4)
    
    screen.fill((192, 192, 192))
    blitRotateZoomXY(screen, cannon, pos, (33.5, 120), angle, zoom_x, zoom_y)
    screen.blit(cannon_mount, (pos[0]-43, pos[1]-16))
    pygame.display.flip()

    if stage == 0:
        angle += 1
        if angle >= -30:
            stage += 1
    elif stage == 1:
        zoom_y -= 0.05
        if zoom_y <= 0.7:
           stage += 1
    elif stage == 2: 
        zoom_y += 0.05
        if zoom_y >= 1:
           stage += 1
    elif stage == 3:
        angle -= 1
        if angle <= -90:
            stage = 0
    
pygame.quit()
exit()
