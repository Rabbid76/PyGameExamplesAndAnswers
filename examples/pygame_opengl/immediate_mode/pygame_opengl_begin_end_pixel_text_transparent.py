# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# pygame + opengl = display text
# https://stackoverflow.com/questions/67608968/pygame-opengl-display-text/67639147#67639147
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md
#
# https://replit.com/@Rabbid76/pygame-opengl-text#main.py

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
             (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0,1), (0,3), (0,4), (2,1),(2,3), (2,7), (6,3), (6,4),(6,7), (5,1), (5,4), (5,7))

def drawCube():
    global edges
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def drawText(x, y, text):                                                
    textSurface = font.render(text, True, (255, 255, 66, 255)).convert_alpha()
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

pygame.init()
clock = pygame.time.Clock()

display = (400, 300)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
font = pygame.font.SysFont('arial', 64)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    drawCube()
    drawText(140, 120, "cube")
    pygame.display.flip()

pygame.quit()
exit()
