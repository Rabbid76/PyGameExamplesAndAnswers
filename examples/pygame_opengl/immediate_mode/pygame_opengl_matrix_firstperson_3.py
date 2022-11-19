# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# How create a camera on PyOpenGL that can do “perspective rotations” on mouse movements?
# https://stackoverflow.com/questions/56609044/how-create-a-camera-on-pyopengl-that-can-do-perspective-rotations-on-mouse-mov/56609894#56609894 
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Camera - First person 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md#first-person


import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def set_projection(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

pygame.init()
pygame.display.set_mode((400, 300), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
set_projection(*pygame.display.get_surface().get_size())
pygame.mouse.set_pos(pygame.display.get_surface().get_rect().center)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()
up_down_angle = 0
sphere = gluNewQuadric() 

paused = False
run = True
while run:
    mouse_move = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            set_projection(event.w, event.h)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
        if event.type == pygame.MOUSEMOTION:
            if not paused: 
                mouse_move = event.rel
                up_down_angle += mouse_move[1]*0.1
                pygame.mouse.set_pos(pygame.display.get_surface().get_rect().center) 
                pygame.mouse.set_visible(paused)
            
    if not paused:
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_d] - keys[pygame.K_a]) * 0.1
        dy = (keys[pygame.K_s] - keys[pygame.K_w]) * 0.1
        
        glLoadIdentity()
        glTranslatef(-dx, 0, -dy)
        glRotatef(mouse_move[0]*0.1, 0, 1, 0)
        glMultMatrixf(view_matrix)
        view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glLoadIdentity()
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)
        glMultMatrixf(view_matrix)

    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

    glPushMatrix()

    glColor4f(0.5, 0.5, 0.5, 1)
    glBegin(GL_QUADS)
    glVertex3f(-10, -10, -2)
    glVertex3f(10, -10, -2)
    glVertex3f(10, 10, -2)
    glVertex3f(-10, 10, -2)
    glEnd()

    glTranslatef(-1.5, 0, 0)
    glColor4f(0.5, 0.2, 0.2, 1)
    gluSphere(sphere, 1.0, 32, 16) 

    glTranslatef(3, 0, 0)
    glColor4f(0.2, 0.2, 0.5, 1)
    gluSphere(sphere, 1.0, 32, 16) 

    glPopMatrix()

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()