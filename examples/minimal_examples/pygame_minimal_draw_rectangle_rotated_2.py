# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Getting rotated rect of rotated image in Pygame
# https://stackoverflow.com/questions/66984521/getting-rotated-rect-of-rotated-image-in-pygame/66984713#66984713
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md
#
# https://replit.com/@Rabbid76/PyGame-AnalogClock#main.py

import pygame, datetime
  
pygame.init()
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
  
hour = pygame.Surface((60, 10), pygame.SRCALPHA)
hour.fill((255, 255, 255))
minute = pygame.Surface((80, 6), pygame.SRCALPHA)
minute.fill((255, 255, 0))
second = pygame.Surface((100, 2), pygame.SRCALPHA)
second.fill((255, 0, 0))

def blitRotate(surf, image, origin, pivot, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(origin) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

start_time = pygame.time.get_ticks()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    now = datetime.datetime.now()
    angle_hour = 90 - 360 * (now.hour + now.minute/60) / 12
    angle_minute = 90 - 360 * now.minute / 60
    angle_second = 90 - 360 * now.second / 60
    center = window.get_rect().center
    
    window.fill(0)
    blitRotate(window, hour, center, (5, 5), angle_hour) 
    blitRotate(window, minute, center, (5, 4), angle_minute)  
    blitRotate(window, second, center, (5, 2), angle_second) 
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()