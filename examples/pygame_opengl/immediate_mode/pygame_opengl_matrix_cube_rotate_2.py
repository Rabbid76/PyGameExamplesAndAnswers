# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# how to drag camera with the mouse like in blender
# https://stackoverflow.com/questions/70398671/how-to-drag-camera-with-the-mouse-like-in-blender/70398950#70398950
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Scale, Rotate, Translate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
        glColor3f(1, 0, 0)    
        glVertex3f(0, -2, 0)  
        glVertex3f(0, 2, 0)    
        glEnd()

pygame.init()
size = (400, 300)
pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, size[0] / size[1], 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)  

cube = Cube()
rot_x, rot_y, transalte_z = 0, 0, -6

run = True
while run:
    mouse_buttons = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            if  mouse_buttons[0]:
                rot_x += event.rel[1]
                rot_y += event.rel[0]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                transalte_z = min(-2.5, transalte_z + 0.2)
            if event.button == 5:
                transalte_z = max(-20, transalte_z - 0.2)
            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(0, 0, transalte_z)
    glRotatef(rot_x, 1, 0, 0)    
    glRotatef(rot_y, 0, 1, 0)    
    cube.draw()
    glPopMatrix()
    
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
