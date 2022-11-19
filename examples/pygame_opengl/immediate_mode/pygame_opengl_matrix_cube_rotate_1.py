# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# How to rotate a cube using mouse in pyopengl
# https://stackoverflow.com/questions/59823131/how-to-rotate-a-cube-using-mouse-in-pyopengl/59823600#59823600
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Scale, Rotate, Translate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class Cube:
    def __init__(self):
        self.v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        self.edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]

    def draw(self):
        glLineWidth(3)
        glColor3fv((1, 1, 1))
        glBegin(GL_LINES)
        for e in self.edges:
            glVertex3fv(self.v[e[0]])
            glVertex3fv(self.v[e[1]])   
        glEnd()

pygame.init()
size = (400, 300)
pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, size[0] / size[1], 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)  
model_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glEnable(GL_DEPTH_TEST)

cube = Cube()

run = True
while run:
    mouse_buttons = pygame.mouse.get_pressed()
    rotate = (0, 0, 0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            if  mouse_buttons[0]:
                rotate = math.hypot(event.rel[0], event.rel[1]), event.rel[1], event.rel[0], 0
        
    glPushMatrix()
    glLoadIdentity()
    glRotatef(*rotate)
    glMultMatrixf(model_matrix)
    model_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glPopMatrix()

    glLoadIdentity()
    glTranslatef(0, 0, -6)
    glMultMatrixf(model_matrix)
            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.draw()
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
