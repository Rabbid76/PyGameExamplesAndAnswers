# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# GitHub - PyGameExamplesAndAnswers -  Primitive and Mesh - PyGame and OpenGL immediate mode (Legacy OpenGL)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

window = pygame.display.set_mode((400, 300), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-1, 1, 1, -1, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

glEnable(GL_DEPTH_TEST)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor4f(1, 0, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.4)
    glVertex2f( 0.5, -0.4)
    glVertex2f( 0.0,  0.6)
    glEnd()

    glEnable(GL_POLYGON_OFFSET_FILL)
    glPolygonOffset(-1.0, -1.0)

    glColor4f(0, 1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5,  0.4)
    glVertex2f( 0.5,  0.4)
    glVertex2f( 0.0, -0.6)
    glEnd()

    glDisable(GL_POLYGON_OFFSET_FILL)
    
    pygame.display.flip()

pygame.quit()
exit()