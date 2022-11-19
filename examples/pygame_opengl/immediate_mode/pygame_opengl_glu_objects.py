# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def set_projection(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

pygame.init()
pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

set_projection(*pygame.display.get_surface().get_size())
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.1, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])
glLightfv(GL_LIGHT0, GL_POSITION, [0, -1, 0, 0])

sphere = gluNewQuadric() 

run = True
while run:
    clock.tick(100)
    take_screenshot = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    
    glTranslatef(-1.5, 0, 0)
    glColor4f(0.5, 0.2, 0.2, 1)
    gluSphere(sphere, 1.0, 32, 16) 

    glTranslatef(3, 0, 0)
    glColor4f(0.2, 0.2, 0.5, 1)
    gluSphere(sphere, 1.0, 32, 16) 

    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
exit()
