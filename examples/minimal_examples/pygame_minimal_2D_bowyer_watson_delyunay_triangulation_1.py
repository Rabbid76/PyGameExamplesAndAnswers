# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Bowyer–Watson algorithm
# https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm 
#
# A Bowyer-Watson Delaunay Triangulation I implemented doesn't remove the triangles that contain points of the super-triangle
# https://stackoverflow.com/questions/58116412/a-bowyer-watson-delaunay-triangulation-i-implemented-doesnt-remove-the-triangle/58122991#58122991
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Mathematics
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame
import math
import random

def circumcenter(a, b, c):
    ad = a[0] * a[0] + a[1] * a[1]
    bd = b[0] * b[0] + b[1] * b[1]
    cd = c[0] * c[0] + c[1] * c[1]
    D = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    return pygame.Vector2((1 / D * (ad * (b[1] - c[1]) + bd * (c[1] - a[1]) + cd * (a[1] - b[1])),
                           1 / D * (ad * (c[0] - b[0]) + bd * (a[0] - c[0]) + cd * (b[0] - a[0]))))

def LineIsEqual(line1,line2):
    if (line1[0] == line2[0] and line1[1] == line2[1]) or (line1[0] == line2[1] and line1[1] == line2[0]):
        return True
    return False

def distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.edges = [[self.a,self.b], [self.b,self.c], [self.c,self.a]]
        self.circumcenter = circumcenter(a, b, c)
    def IsPointInCircumcircle(self,point):
        return self.a.distance_to(self.circumcenter) > point.distance_to(self.circumcenter)
    def HasVertex(self,point):
        """
        if ((self.a[0] == point[0] and self.a[1] == point[1]) or
            (self.b[0] == point[0] and self.b[1] == point[1]) or
            (self.c[0] == point[0] and self.c[1] == point[1])):
        """
        return self.a == point or self.b == point or self.c == point
    def Show(self,screen,colour):
        for edge in self.edges:
            pygame.draw.aaline(screen, colour, edge[0], edge[1])


def DelaunayTriangulation(points, width, height):

    triangulation = []
    superTriangleA = pygame.Vector2(-100, -100)
    superTriangleB = pygame.Vector2(2*width+100, -100)
    superTriangleC = pygame.Vector2(-100, 2*height+100)
    superTriangle = Triangle(superTriangleA, superTriangleB, superTriangleC)
    triangulation.append(superTriangle)

    for point in points:

        badTriangles = []
        for triangle in triangulation:
            if triangle.IsPointInCircumcircle(point):
                badTriangles.append(triangle)

        polygon = []
        for triangle in badTriangles:
            for triangleEdge in triangle.edges:
                isShared = False
                for other in badTriangles:
                    if triangle == other:
                        continue
                    for otherEdge in other.edges:
                        if LineIsEqual(triangleEdge, otherEdge):
                            isShared = True
                if isShared == False:
                    polygon.append(triangleEdge)
 
        for badTriangle in badTriangles:
            triangulation.remove(badTriangle)

        for edge in polygon:
            newTriangle = Triangle(edge[0],edge[1],point)
            triangulation.append(newTriangle)

    onSuper = lambda triangle : triangle.HasVertex(superTriangleA) or triangle.HasVertex(superTriangleB) or triangle.HasVertex(superTriangleC)

    """
    for triangle in triangulation[:]:
        if onSuper(triangle):
            triangulation.remove(triangle)
    """ 
    
    """
    to_be_removed = []
    for triangle in triangulation:
        if onSuper(triangle):
            to_be_removed.append(triangle)
    for triangle in to_be_removed:
        triangulation.remove(triangle)
    """
  
    triangulation = [triangle for triangle in triangulation if not onSuper(triangle)]

    return triangulation

pygame.init()
window = pygame.display.set_mode((500, 500))

background = 20, 40, 100
white = 255, 255, 255

points = []
for i in range(100):
    x = random.randint(20, window.get_width()-40)
    y = random.randint(20, window.get_height()-40)
    points.append(pygame.Vector2(x, y))

delaunay = DelaunayTriangulation(points, *window.get_size())

run = True
while run:
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
    
    window.fill(background)
    for triangle in delaunay:
        triangle.Show(window, white)
    pygame.display.flip()

pygame.quit()
exit()