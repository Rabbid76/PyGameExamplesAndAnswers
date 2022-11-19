# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Bowyer–Watson algorithm
# https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm 
#
# Bowyer-Watson triangulates incorrectly when trying to implement circumcircle calculation for vertices at infinity
# https://stackoverflow.com/questions/58203812/bowyer-watson-triangulates-incorrectly-when-trying-to-implement-circumcircle-cal/58205019#58205019
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Mathematics
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame
import math
import random

def Sign(value):
    return -1 if value < 0 else 1 if value > 0 else 0

def SideOfLineOfPoint(x1, y1, x2, y2, posX, posY):
   return Sign((posX-x1) * (y2-y1) - (posY-y1) * (x2-x1))

def LineIsEqual(line1,line2): 
    return (line1[0] == line2[0] and line1[1] == line2[1]) or (line1[0] == line2[1] and line1[1] == line2[0])
    #return ((line1[0].x == line2[0].x and line1[0].y == line2[0].y and line1[1].x == line2[1].x and line1[1].y == line2[1].y) or 
    #    (line1[0].x == line2[1].x and line1[0].y == line2[1].y and line1[1].x == line2[0].x and line1[1].y == line2[0].y))


class Point:
    def __init__(self,x,y,isInfinite):
        self.x = x
        self.y = y
        self.isInfinite = isInfinite
    def distanceTo(self,other):
        return math.sqrt( (self.x-other.x)**2 + (self.y-other.y)**2 )
    def distanceToSquare(self,other):
        dx, dy = self.x-other.x, self.y-other.y
        return dx*dx + dy*dy

class Triangle:

    def __init__(self,a,b,c):
        self.vertices = [a, b, c]
        self.edges = [[a,b], [b,c], [c,a]]
        self.CalculateCircumcenter()
        self.infiniteVertices = []
        self.finiteVertices = []
        for vertex in self.vertices:
            if vertex.isInfinite:
                self.infiniteVertices.append(vertex)
            else:
                self.finiteVertices.append(vertex)

    def CalculateCircumcenter(self):
        a = [self.vertices[0].x , self.vertices[0].y]
        b = [self.vertices[1].x , self.vertices[1].y]
        c = [self.vertices[2].x , self.vertices[2].y]
        ad = a[0] * a[0] + a[1] * a[1]
        bd = b[0] * b[0] + b[1] * b[1]
        cd = c[0] * c[0] + c[1] * c[1]
        D = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
        self.circumcenter = Point(1 / D * (ad * (b[1] - c[1]) + bd * (c[1] - a[1]) + cd * (a[1] - b[1])),
                                  1 / D * (ad * (c[0] - b[0]) + bd * (a[0] - c[0]) + cd * (b[0] - a[0])),
                                  False)

    def IsPointInCircumcircle(self,point):
       
        #verify_result = self.vertices[0].distanceToSquare(self.circumcenter) > point.distanceToSquare(self.circumcenter)
        #return verify_result

        result = True 
        
        if len(self.infiniteVertices) == 0: 
            result = self.vertices[0].distanceTo(self.circumcenter) > point.distanceTo(self.circumcenter)
    
        elif len(self.infiniteVertices) == 1:
            x1 = self.finiteVertices[0].x
            y1 = self.finiteVertices[0].y
            x2 = self.finiteVertices[1].x
            y2 = self.finiteVertices[1].y
            sideOfLineOfVertex = SideOfLineOfPoint(x1, y1, x2, y2, point.x,point.y)
            sideOfLineOfPoint = SideOfLineOfPoint(x1, y1, x2, y2, self.infiniteVertices[0].x, self.infiniteVertices[0].y)
            result = sideOfLineOfVertex == sideOfLineOfPoint

        elif len(self.infiniteVertices) == 2:
            x1 = self.finiteVertices[0].x
            y1 = self.finiteVertices[0].y
            x2 = self.infiniteVertices[0].x - self.infiniteVertices[1].x + x1
            y2 = self.infiniteVertices[0].y - self.infiniteVertices[1].y + y1
            sideOfLineOfVertex = SideOfLineOfPoint(x1, y1, x2, y2, point.x, point.y)
            sideOfLineOfPoint = SideOfLineOfPoint(x1, y1, x2, y2, self.infiniteVertices[0].x, self.infiniteVertices[0].y)
            result = sideOfLineOfVertex == sideOfLineOfPoint
            
        return result
    
    def HasVertex(self,point):
        if point in self.vertices:
            return True
        return False

    def Show(self,screen,colour):
        for edge in self.edges:
            pygame.draw.aaline(screen,colour,(edge[0].x,edge[0].y),(edge[1].x,edge[1].y))

class DelaunayTriangulation:

    def __init__(self,points,width,height):

        self.triangulation = [] # Create empty list

        self.superTriangleA = Point(-100,-100,True)
        self.superTriangleB = Point(2*width+100,-100,True)
        self.superTriangleC = Point(-100,2*height+100,True)
        superTriangle = Triangle(self.superTriangleA,self.superTriangleB,self.superTriangleC)
        self.triangulation.append(superTriangle) # Create super-triangle

        for point in points: # For every single point to be triangulated
            self.addPoint(point)

    def addPoint(self,point):

        invalidTriangles = [] # Invalid triangle list
        for triangle in self.triangulation: # For every existing triangle
            if triangle.IsPointInCircumcircle(point): # If new point is in the circumcenter of triangle
                invalidTriangles.append(triangle) # Triangle is invalid and added to invalid triangle list

        polygon = [] # List for remaining edges after removal of invalid triangles
        for triangle in invalidTriangles: # For every invalid triangle
            for triangleEdge in triangle.edges: # For each invalid triangle's edges
                isShared = False # Assume no edges are shared
                for other in invalidTriangles: # For every other invalid triangle
                    if triangle == other: # If both are the same triangle
                        continue
                    for otherEdge in other.edges: # For every edge in other triangle
                        if LineIsEqual(triangleEdge,otherEdge):
                            isShared = True # Congruent edges are shared
                if isShared == False: # Only append edges not shared by invalid triangles to polygon hole
                    polygon.append(triangleEdge)

        for triangle in invalidTriangles: # Remove invalid triangles
            self.triangulation.remove(triangle)
        for edge in polygon:
            newTriangle = Triangle(edge[0], edge[1], point)
            self.triangulation.append(newTriangle)

    def Show(self,screen,colour):

        self.shownTriangulation = self.triangulation

        superTriangles = []
        for triangle in self.triangulation:
            if (triangle.HasVertex(self.superTriangleA) or triangle.HasVertex(self.superTriangleB) or triangle.HasVertex(self.superTriangleC)) and (triangle in self.triangulation):
                superTriangles.append(triangle)
        for triangle in superTriangles:
            self.triangulation.remove(triangle)

        for triangle in self.shownTriangulation:
            triangle.Show(screen,colour)


pygame.init()
window = pygame.display.set_mode((500, 500))

background = 20, 40, 100
white = 255, 255, 255

min_dist = 40
points = []
while len(points) < 50:
    x = random.randint(20, window.get_width()-40)
    y = random.randint(20, window.get_height()-40)
    if not any([p for p in points if (p.x-x)*(p.x-x)+(p.y-y)*(p.y-y) < min_dist*min_dist]):
        points.append(Point(x,y,False))

delaunay = DelaunayTriangulation(points, *window.get_size())

run = True
while run:
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
    
    window.fill(background)
    delaunay.Show(window, white)
    pygame.display.flip()

pygame.quit()
exit()