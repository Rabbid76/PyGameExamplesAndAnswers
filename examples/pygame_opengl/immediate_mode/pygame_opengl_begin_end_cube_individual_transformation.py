# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Cube:
    vertices = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
    edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
    
    def __init__(self, position, axis):
        self.position = position
        self.axis = axis
        self.angle = 0

    def animate(self):
        self.angle += 1

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glRotatef(self.angle, *self.axis)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        glPopMatrix()

def main():
    pygame.init()
    size = (800, 600)
    pygame.display.set_mode(size, DOUBLEBUF| OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    aspect = size[0] / size[1]
    #gluPerspective(45, aspect, 0.1, 50)
    glFrustum(-0.1 * aspect, 0.1 * aspect, -0.1, 0.1, 0.2, 50)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -10)
    glEnable(GL_DEPTH_TEST)

    cubes = [Cube((-3, 0, 0), (0, 0, 1)), Cube((3, 0, 0), (0, 1, 0))]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for cube in cubes:
            cube.draw()
            cube.animate()
        
        pygame.display.flip()
        clock.tick(100)

main()
pygame.quit()
exit()