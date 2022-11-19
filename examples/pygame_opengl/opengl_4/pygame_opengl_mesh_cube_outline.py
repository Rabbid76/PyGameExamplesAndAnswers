# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Pygame OpenGL 3D Cube Lag
# https://stackoverflow.com/questions/50312760/pygame-opengl-3d-cube-lag/50314047#50314047
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL 4 - Mesh
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/moderngl_library/pygame_opengl_4.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
import ctypes
import glm

glsl_vert = """
#version 330 core

layout (location = 0) in vec3 a_pos;
layout (location = 1) in vec4 a_col;

out vec4 v_color;

uniform mat4 u_proj; 
uniform mat4 u_view; 
uniform mat4 u_model; 

void main()
{
    v_color     = a_col;
    gl_Position = u_proj * u_view * u_model * vec4(a_pos.xyz, 1.0);
}
"""

glsl_frag = """
#version 330 core

out vec4 frag_color;
in  vec4 v_color;

void main()
{
    frag_color = v_color;
}
"""

class Cube:
  
    def __init__(self):
        v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
        surfaces = [(0,1,2,3), (5,4,7,6), (4,0,3,7),(1,5,6,2), (4,5,1,0), (3,2,6,7)]
        colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (1,0.5,0)]
        line_color = [0, 0, 0]

        edge_attributes = []
        for e in edges:
            edge_attributes += v[e[0]]
            edge_attributes += line_color
            edge_attributes += v[e[1]]
            edge_attributes += line_color

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
        glVertexAttribPointer(0, 3, GL_FLOAT, False, 6*ctypes.sizeof(GLfloat), ctypes.c_void_p(0)) 
        glEnableVertexAttribArray(0) 
        glVertexAttribPointer(1, 3, GL_FLOAT, False, 6*ctypes.sizeof(GLfloat), ctypes.c_void_p(3*ctypes.sizeof(GLfloat))) 
        glEnableVertexAttribArray(1) 

        self.face_vbos = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.face_vbos)
        glBufferData(GL_ARRAY_BUFFER, (GLfloat * len(face_attributes))(*face_attributes), GL_STATIC_DRAW)
        self.face_vao = glGenVertexArrays(1)
        glBindVertexArray(self.face_vao)
        glVertexAttribPointer(0, 3, GL_FLOAT, False, 6*ctypes.sizeof(GLfloat), ctypes.c_void_p(0)) 
        glEnableVertexAttribArray(0) 
        glVertexAttribPointer(1, 3, GL_FLOAT, False, 6*ctypes.sizeof(GLfloat), ctypes.c_void_p(3*ctypes.sizeof(GLfloat))) 
        glEnableVertexAttribArray(1) 

    def draw(self):
        glEnable(GL_DEPTH_TEST)

        glLineWidth(5)

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
    return glm.perspective(glm.radians(45), w / h, 0.1, 50.0)

pygame.init()
window = pygame.display.set_mode((400, 300), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
clock = pygame.time.Clock()

proj = set_projection(*window.get_size())
view = glm.lookAt(glm.vec3(0, 0, 5), glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))
model = glm.mat4(1)
cube = Cube()
angle_x, angle_y = 0, 0

program = compileProgram( 
    compileShader(glsl_vert, GL_VERTEX_SHADER),
    compileShader(glsl_frag, GL_FRAGMENT_SHADER))
attrib = { a : glGetAttribLocation(program, a) for a in ['a_pos', 'a_col'] }
print(attrib)
uniform = { u : glGetUniformLocation(program, u) for u in ['u_model', 'u_view', 'u_proj'] }
print(uniform)
glUseProgram(program)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            proj = set_projection(event.w, event.h)

    model = glm.mat4(1)
    model = glm.rotate(model, glm.radians(angle_y), glm.vec3(0, 1, 0))
    model = glm.rotate(model, glm.radians(angle_x), glm.vec3(1, 0, 0))
   
    glUniformMatrix4fv(uniform['u_proj'], 1, GL_FALSE, glm.value_ptr(proj))
    glUniformMatrix4fv(uniform['u_view'], 1, GL_FALSE, glm.value_ptr(view))
    glUniformMatrix4fv(uniform['u_model'], 1, GL_FALSE, glm.value_ptr(model))

    angle_x += 1
    angle_y += 0.4

    glClearColor(0.5, 0.5, 0.5, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.draw()    
    pygame.display.flip()

pygame.quit()
exit()