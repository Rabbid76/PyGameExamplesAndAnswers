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

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def blitRotateZoom(surf, original_image, origin, pivot, angle, scale):

    image_rect = original_image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = (pygame.math.Vector2(origin) - image_rect.center) * scale
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)
    rotozoom_image = pygame.transform.rotozoom(original_image, angle, scale)
    rect = rotozoom_image.get_rect(center = rotated_image_center)

    surf.blit(rotozoom_image, rect)
    pygame.draw.rect (surf, (255, 0, 0), rect, 2)

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
    pygame.draw.rect (surf, (255, 0, 0), rect, 2)

try:
    image = pygame.image.load('icon/AirPlaneFront1-128.png')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
    image = pygame.Surface((text.get_width()+1, text.get_height()+1))
    pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
    image.blit(text, (1, 1))
w, h = image.get_size()

start = False
angle, zoom = 0, 1
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            start = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.fill(0)
    blitRotateZoom(screen, image, pos, (w/4, h/2), angle, zoom)
    #blitRotateZoomXY(screen, image, pos, (w/4, h/2), angle, zoom, zoom*2)
    if start:
        angle += 1
        zoom += 0.005
        if zoom > 3:
            zoom = 1

    pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

    pygame.display.flip()
    
pygame.quit()
exit()

