# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Drawing points on a surface of a sphere?
# https://stackoverflow.com/questions/50307431/drawing-points-on-a-surface-of-a-sphere 
#
# GitHub - PyGameExamplesAndAnswers -  Primitive and Mesh - PyGame and OpenGL immediate mode (Legacy OpenGL)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import math
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def DrawSphere():
    glBegin(GL_POINTS)
    glVertex3d(0, -1, 0)          # south pole
    for i in range(-90+10,90,10): # -90 to 90 south pole to north pole
        alt = math.radians(i)
        c_alt = math.cos(alt)
        s_alt = math.sin(alt)
        for j in range(0,360,10): # 360 degree (around the sphere)
            azi = math.radians(j)
            c_azi = math.cos(azi)
            s_azi = math.sin(azi)
            glVertex3d(c_azi*c_alt, s_alt, s_azi*c_alt)
    glVertex3d(0, 1, 0)           # north pole
    glEnd()

def set_projection(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, w/h, 0.1, 20)
    glMatrixMode(GL_MODELVIEW)

window = pygame.display.set_mode((400, 300), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
clock = pygame.time.Clock()

set_projection(*window.get_size())
angle = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            set_projection(event.w, event.h)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -2)
    glRotate(25, 1, 0, -1)
    glRotate(angle, 0, 1, 0)
    angle += 1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    DrawSphere()
    pygame.display.flip()

pygame.quit()
exit()