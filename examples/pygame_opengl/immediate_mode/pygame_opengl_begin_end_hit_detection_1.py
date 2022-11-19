# How to find PyGame Window Coordinates of an OpenGL Vertice?
# https://stackoverflow.com/questions/46801701/how-to-find-pygame-window-coordinates-of-an-opengl-vertice/46815050#46815050
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Mouse position and Unproject
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md#mouse-position-and-unproject

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

rect1 = [(-10, -3, -30), (-4, -3, -30), (-4, 3, -30), (-10, 3, -30)]
rect2 = [(  4, -3, -30), (10, -3, -30), (10, 3, -30), (  4, 3, -30)]
fov_y, width,height  = 45, 320, 200

def draw():
    mpos = pygame.mouse.get_pos()
    ndc = [ 2.0 * mpos[0]/width - 1.0, 1.0 - 2.0 * mpos[1]/height ]
    tan_fov = math.tan(fov_y * 0.5 * math.pi / 180)
    aspect = width / height 
    
    for rect in (rect1, rect2):
        z = abs(rect[0][2])
        view_pos = [z * ndc[0] * aspect * tan_fov, z * ndc[1] * tan_fov]
        in_rect = 1 if rect[0][0] <= view_pos[0] <= rect[1][0] and rect[0][1] <= view_pos[1] <= rect[2][1] else 0

        glColor3f(1, 1-in_rect, 1-in_rect)
        glBegin(GL_LINE_LOOP)
        for vertex in rect:
            glVertex3fv(vertex)
        glEnd()

pygame.init()
pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(fov_y, width / height, 0.1, 100)
glMatrixMode(GL_MODELVIEW)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)      
    draw()
    pygame.display.flip() 

pygame.quit()
exit()