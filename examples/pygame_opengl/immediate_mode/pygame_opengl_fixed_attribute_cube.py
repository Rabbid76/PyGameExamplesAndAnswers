# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Pygame OpenGL 3D Cube Lag
# https://stackoverflow.com/questions/50312760/pygame-opengl-3d-cube-lag/50314047#50314047
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh - Fixed attribute
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import ctypes

class Cube:
  
    def __init__(self):
        v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
        surfaces = [(0,1,2,3), (5,4,7,6), (4,0,3,7),(1,5,6,2), (4,5,1,0), (3,2,6,7)]
        colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (1,0.5,0)]
        self.line_color = [0, 0, 0]

        edge_attributes = []
        for e in edges:
            edge_attributes += v[e[0]]
            edge_attributes += v[e[1]]
        self.edge_array = (GLfloat * len(edge_attributes))(*edge_attributes)

        face_vertices = []
        face_colors = []
        for i, quad in enumerate(surfaces):
            for iv in quad:
                face_vertices += v[iv]
                face_colors += colors[i]
        self.vertex_array = (GLfloat * len(face_vertices))(*face_vertices)
        self.color_array = (GLfloat * len(face_colors))(*face_colors)

    def draw(self):
        glEnable(GL_DEPTH_TEST)

        glLineWidth(5)

        glColor3fv(self.line_color)
        glVertexPointer(3, GL_FLOAT, 0, self.edge_array) 
        glEnableClientState(GL_VERTEX_ARRAY) 
        glDrawArrays(GL_LINES, 0, 12*2)
        glDisableClientState(GL_VERTEX_ARRAY)

        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset( 1.0, 1.0 )

        glVertexPointer(3, GL_FLOAT, 0, self.vertex_array)
        glColorPointer(3, GL_FLOAT, 0, self.color_array) 
        glEnableClientState(GL_VERTEX_ARRAY)  
        glEnableClientState(GL_COLOR_ARRAY) 
        glDrawArrays(GL_QUADS, 0, 6*4)
        glDisableClientState(GL_VERTEX_ARRAY)  
        glDisableClientState(GL_COLOR_ARRAY) 
        
        glDisable(GL_POLYGON_OFFSET_FILL)

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
angle_x, angle_y = 0, 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            set_projection(event.w, event.h)

    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_x, 1, 0, 0)
    angle_x += 1
    angle_y += 0.4

    glClearColor(0.5, 0.5, 0.5, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.draw()    
    pygame.display.flip()

pygame.quit()
exit()