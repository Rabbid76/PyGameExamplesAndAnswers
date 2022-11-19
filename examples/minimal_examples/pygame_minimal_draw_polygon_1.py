# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How to translate and rotate the coordinate axis about a point in pygame screen?
# https://stackoverflow.com/questions/68835224/how-can-i-make-my-code-more-optimised-by-not-drawing-a-rect-on-each-pixel/68835795#68835795 
#
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw lines and polygons
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame, math, pygame.gfxdraw

def drawDDA(p1, p2, color=[0, 0, 0]):
    x0, y0, x1, y1 = p1[0], p1[1], p2[0], p2[1]
    steps = abs(x0-x1) if abs(x0-x1) > abs(y0-y1) else abs(y0-y1)
    dx = (x1-x0) / steps
    dy = (y1-y0) / steps
    pygame.gfxdraw.pixel(screen, round(x0), round(y0), color)
    for i in range(int(steps)):
        pygame.gfxdraw.pixel(screen, round(x0 + i*dx), round(y0 + i*dy), color)

def drawPoly(center, n, s, color=[0, 0, 0]):
    x0, y0 = center[0], center[1]
    a =  math.radians(360 / n)
    d = s / 2 / math.sin(a / 2)
    pts = []
    for i in range(n+1):
        sideAngle = math.radians(360 * i / n)
        x = x0 + d * math.cos(sideAngle)
        y = y0 + d * math.sin(sideAngle)
        pts.append([x, y])

    for i in range(n):
        drawDDA(pts[i], pts[i+1], color)

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
colors = [(192, 0, 0), (0, 192, 0), (0, 0, 192), (192, 192, 0), (0, 192, 192), (192, 0, 192), (0, 0, 0)]

run = True
while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    for i, color in enumerate(colors):
        drawPoly((150, 150), i+3, 100, color)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()