# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# PyOpenGl Pygame window freezes when run
# https://stackoverflow.com/questions/54683378/pyopengl-pygame-window-freezes-when-run/54696233#54696233
#
# Drawing a cube with Pygame and OpenGL in Python environment
# https://stackoverflow.com/questions/66623528/drawing-a-cube-with-pygame-and-opengl-in-python-environment/66623589#66623589
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

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
gluPerspective(45, size[0] / size[1], 0.1, 10.0)
glMatrixMode(GL_MODELVIEW)  
glTranslatef(0.0, 0.0, -5)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 3, 1, 1)
    cube()
    pygame.display.flip()

pygame.quit()
exit()
