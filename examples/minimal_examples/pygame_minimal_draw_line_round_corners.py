# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# draw lines with round edges in pygame
# https://stackoverflow.com/questions/70051590/draw-lines-with-round-edges-in-pygame/70053349#70053349
#
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Lines with round corners
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md
#
# https://replit.com/@Rabbid76/PyGame-DashedLine

import pygame
import cv2, numpy

def draw_line_round_corners(surf, p1, p2, c, w):
    pygame.draw.line(surf, c, p1, p2, w)
    pygame.draw.circle(surf, c, p1, w // 2)
    pygame.draw.circle(surf, c, p2, w // 2)

def draw_line_round_corners_polygon(surf, p1, p2, c, w):
    p1v = pygame.math.Vector2(p1)
    p2v = pygame.math.Vector2(p2)
    lv = (p2v - p1v).normalize()
    lnv = pygame.math.Vector2(-lv.y, lv.x) * w // 2
    pts = [p1v + lnv, p2v + lnv, p2v - lnv, p1v - lnv]
    pygame.draw.polygon(surf, c, pts)
    pygame.draw.circle(surf, c, p1, round(w / 2))
    pygame.draw.circle(surf, c, p2, round(w / 2))

def draw_line_round_corners_cv(surf, p1, p2, color, w):
    rect = pygame.Rect(*p1, p2[0]-p1[0], p2[1]-p1[1])
    rect.normalize()
    rect.inflate_ip(w, w)
    line_image = numpy.zeros((rect.height, rect.width, 4), dtype = numpy.uint8)
    c = pygame.Color(color)
    line_image = cv2.line(line_image, (w//2, w//2), (p2[0]-p1[0]+w//2, p2[1]-p1[1]+w//2), (c.r, c.g, c.b, c.a), thickness=w)
    line_surface = pygame.image.frombuffer(line_image.flatten(), rect.size, 'RGBA')
    surf.blit(line_surface, line_surface.get_rect(center = rect.center))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill(0)
    draw_line_round_corners(window, (50, 50), (300, 300), "red", 20)
    draw_line_round_corners_polygon(window, (50, 100), (250, 350), "orange", 20)
    draw_line_round_corners_cv(window, (100, 50), (350, 250), "yellow", 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
