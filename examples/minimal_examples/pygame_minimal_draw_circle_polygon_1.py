# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How do you create a polygon that fills the area between 2 circles?
# https://stackoverflow.com/questions/75105181/how-do-you-create-a-polygon-that-fills-the-area-between-2-circles/75109072#75109072
#
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw lines and polygons
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

cpt1 = (100, 200)
cpt2 = (300, 200)
radius = 40

def create_polygon(center1, radius1, center2, radius2):
    cp1 = pygame.math.Vector2(center1)
    cp2 = pygame.math.Vector2(center2)
    cv = cp1 - cp2
    nv = pygame.math.Vector2(-cv.y, cv.x).normalize() * (radius1 - radius2)
    tnv1 = pygame.math.Vector2(-(cv.y + nv.y), cv.x + nv.x).normalize() 
    tnv2 = pygame.math.Vector2(cv.y - nv.y, -(cv.x - nv.x)).normalize()
    pts = [cp1 + tnv1 * radius1, cp2 + tnv1 * radius2, cp2 + tnv2 * radius2, cp1 + tnv2 * radius1]
    return [(p.x, p.y) for p in pts] 

def draw_line_round_corners_polygon(surf, point_1, point_2, color, circle_radius):
    points = create_polygon(point_1, circle_radius*2, point_2, circle_radius)
    pygame.draw.polygon(surf, color, points)
    pygame.draw.circle(surf, color, point_1, round(circle_radius*2))
    pygame.draw.circle(surf, color, point_2, round(circle_radius))

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill("gray")
    draw_line_round_corners_polygon(window, cpt1, cpt2, "red", radius)
    pygame.display.flip()

pygame.quit()
exit()
