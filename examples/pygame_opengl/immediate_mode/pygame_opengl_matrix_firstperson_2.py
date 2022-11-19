# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Stackoverflow question: how to modify the view of the camera with pygame and openGL
# https://stackoverflow.com/questions/47169618/how-to-modify-the-view-of-the-camera-with-pygame-and-opengl/47173089#47173089
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Camera - First person 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md#first-person


import pygame
from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]

def Cube(tX, tY, tZ):
    glPushMatrix()
    glTranslate(tX, tY, tZ)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    glPopMatrix()

pygame.init()
pygame.display.set_mode((600, 400), DOUBLEBUF|OPENGL)
clock = pygame.time.Clock()

sum_rot_updown = 0
current_mv_mat = (GLfloat * 16)()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, 600 / 400, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    sum_rot_updown += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 1.5

    glLoadIdentity()
    glRotatef((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 1.5, 0, 1, 0)
    glTranslate((keys[pygame.K_a] - keys[pygame.K_d]) * 0.5, 0, (keys[pygame.K_w] - keys[pygame.K_s]) * 0.5)
    glMultMatrixf(current_mv_mat)
    glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
    
    glLoadIdentity()
    glRotatef(sum_rot_updown, 1, 0, 0)
    glMultMatrixf(current_mv_mat)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    for i in range(8):
        for j in range(8):
            Cube(i*2.5 - 8.75, -4, -j*2.5)
    pygame.display.flip()

pygame.quit()
exit()
