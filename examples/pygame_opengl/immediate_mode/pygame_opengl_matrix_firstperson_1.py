# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Stackoverflow question: how to modify the view of the camera with pygame and openGL
# https://stackoverflow.com/questions/47169618/how-to-modify-the-view-of-the-camera-with-pygame-and-opengl/47173089#47173089
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Camera - First person 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md#first-person

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

class Cube:
  
    def __init__(self):
        self.v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        self.edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
        self.surfaces = [(0,1,2,3), (5,4,7,6), (4,0,3,7),(1,5,6,2), (4,5,1,0), (3,2,6,7)]
        self.colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (1,0.5,0)]

    def draw(self):
        glEnable(GL_DEPTH_TEST)

        glLineWidth(5)
        glColor3fv((0, 0, 0))
        glBegin(GL_LINES)
        for e in self.edges:
            glVertex3fv(self.v[e[0]])
            glVertex3fv(self.v[e[1]])
        glEnd()

        glEnable( GL_POLYGON_OFFSET_FILL )
        glPolygonOffset( 1.0, 1.0 )

        glBegin(GL_QUADS)
        for i, quad in enumerate(self.surfaces):
            glColor3fv(self.colors[i])
            for iv in quad:
                glVertex3fv(self.v[iv])
        glEnd()

        glDisable( GL_POLYGON_OFFSET_FILL )

def identity_matrix44(): return numpy.matrix(numpy.identity(4), copy=False, dtype='float32')

def set_projection(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

pygame.init()
window = pygame.display.set_mode((400, 300), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
clock = pygame.time.Clock()

set_projection(*window.get_size())
cube = Cube()
tx, ty, tz = 0, 0, 0
rx, ry, rz = 0, 0, 0

view_mat = identity_matrix44()
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0, 0, -5)
glGetFloatv(GL_MODELVIEW_MATRIX, view_mat)
glLoadIdentity()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            set_projection(event.w, event.h)

    keys = pygame.key.get_pressed()
    tx = (keys[pygame.K_d] - keys[pygame.K_a]) * -0.1
    tz = (keys[pygame.K_w] - keys[pygame.K_s]) * 0.1
    ry = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 1.0

    glClearColor(0.5, 0.5, 0.5, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glLoadIdentity()
    glTranslatef(tx, ty, tz)
    glRotatef(ry, 0, 1, 0)
    glMultMatrixf(view_mat)

    glGetFloatv(GL_MODELVIEW_MATRIX, view_mat)
    
    cube.draw()
    glPopMatrix()    

    size = window.get_size()
    buffer = glReadPixels(0, 0, *size, GL_RGBA, GL_UNSIGNED_BYTE)
    pygame.display.flip()

    #screen_surf = pygame.image.fromstring(buffer, size, "RGBA")
    #pygame.image.save(screen_surf, "d:/temp/screenshot.jpg")
    
pygame.quit()
exit()