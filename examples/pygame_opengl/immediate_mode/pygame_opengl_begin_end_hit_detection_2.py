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

def transform_vec3(vec_a, mat44):
    vec_b = [0, 0, 0, 0]
    for i0 in range(0, 4):
        vec_b[i0] = vec_a[0] * mat44[0*4+i0] + vec_a[1] * mat44[1*4+i0] + vec_a[2] * mat44[2*4+i0] + mat44[3*4+i0]
    return [vec_b[0]/vec_b[3], vec_b[1]/vec_b[3], vec_b[2]/vec_b[3]]

def test_rec(prj_mat, mpos, ll, tr):
    ll_ndc = transform_vec3(ll, prj_mat)
    tr_ndc = transform_vec3(tr, prj_mat)
    ndc = [2.0 * mpos[0]/width - 1.0, 1.0 - 2.0 * mpos[1]/height ]
    in_rect = 1 if ll_ndc[0] <= ndc[0] <= tr_ndc[0] and ll_ndc[1] <= ndc[1] <= tr_ndc[1] else 0
    return in_rect

def draw():
    prj_mat = (GLfloat * 16)()
    glGetFloatv(GL_PROJECTION_MATRIX, prj_mat)
    mpos = pygame.mouse.get_pos()
    
    for rect in (rect1, rect2):
        in_rect = test_rec(prj_mat, mpos, rect[0], rect[2])
        
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