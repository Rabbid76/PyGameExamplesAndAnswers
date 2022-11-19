# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How to draw a dashed curved line with pygame?
# https://stackoverflow.com/questions/66943011/how-to-draw-a-dashed-curved-line-with-pygame/66944050#66944050
#
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw lines and polygons
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md
#
# https://replit.com/@Rabbid76/PyGame-DashedLine

import pygame
import math

def draw_dashed_line(surf, color, p1, p2, prev_line_len, dash_length=8):
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    if dx == 0 and dy == 0:
        return 
    dist = math.hypot(dx, dy)
    dx /= dist
    dy /= dist

    step = dash_length*2
    start = (int(prev_line_len) // step) * step
    end = (int(prev_line_len + dist) // step + 1) * step
    for i in range(start, end, dash_length*2):
        s = max(0, start - prev_line_len)
        e = min(start - prev_line_len + dash_length, dist)
        if s < e:
            ps = p1[0] + dx * s, p1[1] + dy * s 
            pe = p1[0] + dx * e, p1[1] + dy * e 
            pygame.draw.line(surf, color, pe, ps)

def draw_dashed_lines(surf, color, points, dash_length=8):
    line_len = 0
    for i in range(1, len(points)):
        p1, p2 = points[i-1], points[i]
        dist = math.hypot(p2[0]-p1[0], p2[1]-p1[1])
        draw_dashed_line(surf, color, p1, p2, line_len, dash_length)
        line_len += dist

pygame.init()
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

line = [(i, 150 + math.sin(math.radians(i*2)) * 100) for i in range(400)]

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_dashed_lines(window, (255, 255, 255), line)
    pygame.display.flip()