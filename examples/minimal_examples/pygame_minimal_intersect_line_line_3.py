# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# I'm having a problem with determining the intersection of two lines in this python code
# https://stackoverflow.com/questions/69353309/im-having-a-problem-with-determining-the-intersection-of-two-lines-in-this-pyth/69357134#69357134
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Line and line
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

pygame.init()
window = pygame.display.set_mode((500,500))

def add(a, b):
    return a[0]+b[0], a[1]+b[1]
def sub(a, b):
    return a[0]-b[0], a[1]-b[1]
def rot90(v):
    return -v[1], v[0]
def mul(v, s):
    return v[0]*s, v[1]*s
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

lines = []
start = None

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start = event.pos
        elif event.type == pygame.MOUSEBUTTONUP: 
            lines.append(([start, event.pos]))
            start = None

    intersections = []
    for i, line1 in enumerate(lines):
        for line2 in lines[i+1:]:
            #line 1
            point1_line1, point2_line1 = line1
            line1_vector = sub(point2_line1, point1_line1)
            line1_norml  = rot90(line1_vector)

            #line2
            point1_line2, point2_line2 = line2
            line2_vector = sub(point2_line2, point1_line2)
            line2_norml  = rot90(line2_vector)

            # vector from start point of line 2 to start point of line 1
            l2p1_l1p1 = sub(point1_line1, point1_line2)

            # intersection
            d = dot(line2_vector, line1_norml)
            if d != 0: # prallel lines
                t = dot(l2p1_l1p1, line1_norml) / d
                u = dot(l2p1_l1p1, line2_norml) / d
                if 0 <= t <= 1 and 0 <= u <= 1: # intersection on line segments
                    xi, yi = add(point1_line2, mul(line2_vector, t))
                    intersections.append((xi, yi))

    window.fill((255,255,255))
    if start:
        pygame.draw.line(window, (0,0,0), start, pygame.mouse.get_pos(), 4)
    for line in lines:
        pygame.draw.line(window, (0,0,0), *line, 4)
    for p in intersections:
        pygame.draw.circle(window, (0,200,0), (round(p[0]), round(p[1])), 10)
    pygame.display.flip()

pygame.quit()
exit()