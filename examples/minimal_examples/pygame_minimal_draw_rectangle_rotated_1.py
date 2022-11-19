# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Getting rotated rect of rotated image in Pygame
# https://stackoverflow.com/questions/66984521/getting-rotated-rect-of-rotated-image-in-pygame/66984713#66984713
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md
#
# https://replit.com/@Rabbid76/PyGame-RotatedRectangle

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

orig_image = font.render("rotated rectangle", True, (255, 0, 0))
angle = 30
rotated_image = pygame.transform.rotate(orig_image, angle)

def draw_rect_angle(surf, rect, pivot, angle, width=0):
    pts = [rect.topleft, rect.topright, rect.bottomright, rect.bottomleft]
    pts = [(pygame.math.Vector2(p) - pivot).rotate(-angle) + pivot for p in pts]
    pygame.draw.polygon(surf, (255, 255, 0), pts, width)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    

    window.fill(0)
    window_center = window.get_rect().center
    window.blit(rotated_image, rotated_image.get_rect(center = window_center))
    rect = orig_image.get_rect(center = window_center)
    draw_rect_angle(window, rect, window_center, angle, 3)
    pygame.display.flip()

pygame.quit()
exit()