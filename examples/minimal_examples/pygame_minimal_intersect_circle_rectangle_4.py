# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# How can I know if a circle and a rect is touched in Pygame?
# https://stackoverflow.com/questions/54840710/how-can-i-know-if-a-circle-and-a-rect-is-touched-in-pygame/54841116#54841116
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Rectangle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame
import pygame.font
pygame.init()

def isectRectCircle(rect_tl, rect_size, circle_cpt, circle_rad):
    
    rect = pygame.Rect(*rect_tl, *rect_size)
    if rect.collidepoint(*circle_cpt):
        return True

    centerPt = pygame.math.Vector2(*circle_cpt)
    cornerPts = [rect.bottomleft, rect.bottomright, rect.topleft, rect.topright]
    if any(p for p in cornerPts if pygame.math.Vector2(*p).distance_to(centerPt) <= circle_rad):
        return True

    return False


window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

circle_cpt, circle_rad = window.get_rect().center, 50
rect_object = pygame.Rect(window.get_width() // 5, window.get_height() // 5, 50, 50)
speed = 1

run = False
while not run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    keys = pygame.key.get_pressed()
    rect_object.centerx = (rect_object.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed) % window.get_width()
    rect_object.centery = (rect_object.centery + (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed) % window.get_height()
    
    rect_color = (128, 128, 128)
    if isectRectCircle(rect_object.topleft, rect_object.size, circle_cpt, circle_rad):
        rect_color = (255, 0, 0)

    window.fill((0, 0, 128))
    pygame.draw.circle(window, (0, 196, 0), circle_cpt, circle_rad)
    pygame.draw.rect(window, rect_color, rect_object)
    
    pygame.display.flip()

pygame.quit()
exit()