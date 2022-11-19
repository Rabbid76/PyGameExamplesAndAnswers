# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Cube:
    def __init__(self):
        self.v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        self.surfaces = [(0,1,2,3), (5,4,7,6), (4,0,3,7),(1,5,6,2), (4,5,1,0), (3,2,6,7)]
        self.colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (1,0.5,0)]
        self.normals = [(0,0,-1), (0,0,1), (-1,0,0), (1,0,0), (0,-1,0), (0,1,0)]

    def render(self):
        glBegin(GL_QUADS)
        for i, quad in enumerate(self.surfaces):
            #glColor3fv(self.colors[i])
            glColor3f(.5, .5, .7)
            glNormal3fv(self.normals[i])
            for iv in quad:
                glVertex3fv(self.v[iv])
        glEnd()

pygame.init()
pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
size = pygame.display.get_surface().get_size()
gluPerspective(45, size[0] / size[1], 0.001, 10.0)
#gluPerspective(45, size[0] / size[1], 0.1, 10.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(0.0, 1.0, -5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glShadeModel(GL_SMOOTH)
glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 1.0))

lighting = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
cube = Cube()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == timer_event:
            lighting = not lighting
            if lighting:
                glEnable(GL_LIGHTING)
            else:
                glDisable(GL_LIGHTING)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotate(-30, 1, 0, 0)
    glRotate(60, 0, 1, 0)
    glScale(1, 0.25, 0.5)
    cube.render()
    glPopMatrix()
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
quit()
