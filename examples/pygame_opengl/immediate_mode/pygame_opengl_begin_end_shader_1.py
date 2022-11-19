# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Vertex/fragment shaders for a OpenGL firsrt-person shooter view?
# https://stackoverflow.com/questions/59896103/vertex-fragment-shaders-for-a-opengl-firsrt-person-shooter-view/59898241#59898241
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL.shaders as shaders

verticies = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
             (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0,1), (0,3), (0,4), (2,1),(2,3), (2,7), (6,3), (6,4),(6,7), (5,1), (5,4), (5,7))

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

pygame.init()
size = (400, 300)
pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, size[0] / size[1], 3.0, 7.0)
glMatrixMode(GL_MODELVIEW)  
glTranslatef(0.0, 0.0, -5)

vertes_shader = """
#version 120

void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
"""

fragment_shader = """
#version 120
void main()
{
    vec3 color = vec3(1.0 - gl_FragDepth);
    gl_FragColor = vec4(color, 1.0);
}
"""

shader = shaders.compileProgram(
    shaders.compileShader(vertes_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)
    glRotatef(1, 3, 1, 1)
    cube()
    pygame.display.flip()

pygame.quit()
exit()
