# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# GitHub - PyGameExamplesAndAnswers -  Primitive and Mesh - PyGame and OpenGL immediate mode (Legacy OpenGL)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md
#
# https://replit.com/@Rabbid76/pygame-opengl-1#main.py

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

window = pygame.display.set_mode((400, 300), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
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
    glVertex2f(-0.5, -0.5)
    glVertex2f( 0.5, -0.5)
    glVertex2f( 0.0,  0.5)
    glEnd()
    
    pygame.display.flip()

pygame.quit()
exit()