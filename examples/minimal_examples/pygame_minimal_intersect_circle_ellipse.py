# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#
# Collision detection between an ellipse and a circle
# https://stackoverflow.com/questions/64107897/collision-detection-between-an-ellipse-and-a-circle/64108816#64108816
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-IntersectCircleEllipse

import math
import pygame

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center = center_x, center_y
        self.radius = radius
    def update(self, center_x, center_y):
        self.center = center_x, center_y
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (round(self.center[0]), round(self.center[1])), self.radius, 3)

class Ellipse:
    def __init__(self, center, vertex):
        self.center = center
        self.collided = False
        self.vertex = vertex
    def draw(self, surface):
        bounding_rect = pygame.Rect(0, 0, self.vertex[0] * 2, self.vertex[1] * 2)
        bounding_rect.center = round(self.center[0]), round(self.center[1])
        pygame.draw.ellipse(surface, (0, 255, 0), bounding_rect, 3)
    def pointFromAngle(self, a):
        c = math.cos(a)
        s = math.sin(a)
        ta = s / c  ## tan(a)
        tt = ta * self.vertex[0] / self.vertex[1]  ## tan(t)
        d = 1. / math.sqrt(1. + tt * tt)
        x = self.center[0] + math.copysign(self.vertex[0] * d, c)
        y = self.center[1] - math.copysign(self.vertex[1] * tt * d, s)
        return x, y

def intersect_circle_ellipse(circle, ellipse):
    dx = circle.center[0] - ellipse.center[0]
    dy = circle.center[1] - ellipse.center[1]
    angle = math.atan2(-dy, dx)
    x, y = ellipse.pointFromAngle(angle)
    distance = math.hypot(x - circle.center[0], y-circle.center[1])
    return distance <= circle.radius, (x, y) 

pygame.init()
window = pygame.display.set_mode((500, 300))
circle = Circle(0, 0, 30)      
ellipse = Ellipse(window.get_rect().center, (150, 100))
run = True
while run:
    events = pygame.event.get()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            
    circle.update(*mousePos)
    isect = intersect_circle_ellipse(circle, ellipse)

    window.fill((255, 255, 255))
    circle.draw(window)
    ellipse.draw(window) 
    color = (255, 0, 255) if isect[0] else (0, 0, 255)
    pygame.draw.circle(window, color, (round(isect[1][0]), round(isect[1][1])), 5)
    pygame.display.flip()

pygame.quit()
exit()