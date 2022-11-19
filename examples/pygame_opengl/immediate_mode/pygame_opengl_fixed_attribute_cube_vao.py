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

        face_attributes = []
        for i, quad in enumerate(surfaces):
            for iv in quad:
                face_attributes += v[iv]
                face_attributes += colors[i]

        self.edge_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.edge_vbo)
        glBufferData(GL_ARRAY_BUFFER, (GLfloat * len(edge_attributes))(*edge_attributes), GL_STATIC_DRAW)
        self.edge_vao = glGenVertexArrays(1)
        glBindVertexArray(self.edge_vao)
        glVertexPointer(3, GL_FLOAT, 0, None) 
        glEnableClientState(GL_VERTEX_ARRAY) 
        glBindBuffer(GL_ARRAY_BUFFER, 0) 

        self.face_vbos = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.face_vbos)
        glBufferData(GL_ARRAY_BUFFER, (GLfloat * len(face_attributes))(*face_attributes), GL_STATIC_DRAW)
        self.face_vao = glGenVertexArrays(1)
        glBindVertexArray(self.face_vao)
        glVertexPointer(3, GL_FLOAT, 6*ctypes.sizeof(GLfloat), None)
        glEnableClientState(GL_VERTEX_ARRAY)  
        glColorPointer(3, GL_FLOAT, 6*ctypes.sizeof(GLfloat), ctypes.cast(3*ctypes.sizeof(GLfloat), ctypes.c_void_p)) 
        glEnableClientState(GL_COLOR_ARRAY) 
        
        glBindBuffer(GL_ARRAY_BUFFER, 0) 
        glBindVertexArray(0)


    def draw(self):
        glEnable(GL_DEPTH_TEST)

        glLineWidth(5)

        glColor3fv(self.line_color)
        glBindVertexArray(self.edge_vao)
        glDrawArrays(GL_LINES, 0, 12*2)
        glBindVertexArray(0)

        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset( 1.0, 1.0 )

        glBindVertexArray(self.face_vao)
        glDrawArrays(GL_QUADS, 0, 6*4)
        glBindVertexArray(0)
        
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