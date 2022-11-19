# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#
# How to know if two ellipses are colliding - Pygame
# https://stackoverflow.com/questions/65323156/how-to-know-if-two-ellipses-are-colliding-pygame
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

# TODO
# [Intersection of two ellipses](https://math.stackexchange.com/questions/1688449/intersection-of-two-ellipses)
# [Detect if two ellipses intersect](https://math.stackexchange.com/questions/1114879/detect-if-two-ellipses-intersect)
# [Ellipse–circle and ellipse–ellipse collision detection](http://yehar.com/blog/?p=2926)
# [How to detect if an ellipse intersects(collides with) a circle](https://stackoverflow.com/questions/2945337/how-to-detect-if-an-ellipse-intersectscollides-with-a-circle)
# [The closest point from ellipse](https://math.stackexchange.com/questions/315283/the-closest-point-from-ellipse)

import math
import pygame

class Ellipse:
    def __init__(self, center, vertex):
        self.center = center
        self.vertex = vertex
    def draw(self, surface):
        bounding_rect = pygame.Rect(0, 0, self.vertex[0] * 2, self.vertex[1] * 2)
        bounding_rect.center = round(self.center[0]), round(self.center[1])
        pygame.draw.ellipse(surface, (0, 255, 0), bounding_rect, 3)
    
def planeFromEllipse(ellipse):
    a, b = ellipse.vertex
    if a > b:
        y = math.sqrt(a*a - b*b)
        nv = pygame.math.Vector3(0, y, b)
    else:
        x = math.sqrt(b*b - a*a)
        nv = pygame.math.Vector3(x, 0, a)
    nv.normalize_ip()
    return pygame.math.Vector3(*ellipse.center, 0), nv 

def rayPlaneIntersection(R0, D, P0, NV):
    return R0 + D * (P0 - R0).dot(NV) / D.dot(NV)

def planePlaneIntersection(P1, NV1, P2, NV2):
    D = NV1.cross(NV2)
    #PX = rayPlaneIntersection(P1, NV1.cross(D), P2, NV2)
    PX = rayPlaneIntersection(P2, NV2.cross(D), P1, NV1)
    return PX, D

def lineCircleIntersection(P1, P2, CPT, r):
    sign = lambda x: math.copysign(1, x)
    X1 = P1 - CPT
    X2 = P2 - CPT
    DV = X2 - X1
    dr = DV.length()
    d = X1.x*X2.y - X2.x*X1.y
    di = r*r*dr*dr - d*d
    if di < 0.0: return [] 
    t = math.sqrt(di)
    ip = [pygame.math.Vector2(d*DV.y + sign(DV.y)*DV.x*t, -d*DV.x + abs(DV.y)*t) / (dr*dr) + CPT]
    if di > 0:
       ip += [pygame.math.Vector2(d*DV.y - sign(DV.y)*DV.x*t, -d*DV.x - abs(DV.y)*t) / (dr*dr) + CPT] 
    return ip

def intersect_circle_ellipse(ellipse1, ellipse2):
    P1, NV1 = planeFromEllipse(ellipse1)
    P2, NV2 = planeFromEllipse(ellipse2)
    #NV2 = pygame.math.Vector3(-NV2.x, -NV2.y, NV2.z)
    I0, D = planePlaneIntersection(P1, NV1, P2, NV2)
    D.normalize_ip()
    s1 = ellipse1.vertex[0] / ellipse1.vertex[1]
    s2 = ellipse2.vertex[0] / ellipse2.vertex[1]
    v2 = pygame.math.Vector2
    isect1 = lineCircleIntersection(v2(I0.x, I0.y*s1), v2(I0.x+D.x, (I0.y+D.y)*s1), v2(P1.x, P1.y*s1), ellipse1.vertex[0])
    isect2 = lineCircleIntersection(v2(I0.x, I0.y*s2), v2(I0.x+D.x, (I0.y+D.y)*s2), v2(P2.x, P2.y*s2), ellipse2.vertex[0])
    return isect1 and isect2, I0, D

pygame.init()
window = pygame.display.set_mode((500, 500))
    
ellipse1 = Ellipse(window.get_rect().center, (100, 50)) 
ellipse2 = Ellipse(window.get_rect().center, (50, 100))

run = True
while run:
    events = pygame.event.get()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            
    ellipse1.center = mousePos
    isect = intersect_circle_ellipse(ellipse1, ellipse2)

    window.fill((255, 255, 255))
    ellipse1.draw(window)
    ellipse2.draw(window) 
    
    color = (255, 0, 255) if isect[0] else (127, 127, 127)
    ix, iy = round(isect[1][0]), round(isect[1][1])
    len = 500
    lx1, ly1 = round(isect[1][0] + isect[2][0] * len), round(isect[1][1] + isect[2][1] * len)
    lx2, ly2 = round(isect[1][0] - isect[2][0] * len), round(isect[1][1] - isect[2][1] * len)
    pygame.draw.circle(window, color, (ix, iy), 5)
    pygame.draw.line(window, color, (lx1, ly1), (lx2, ly2), 3)

    pygame.display.flip()

pygame.quit()
exit()