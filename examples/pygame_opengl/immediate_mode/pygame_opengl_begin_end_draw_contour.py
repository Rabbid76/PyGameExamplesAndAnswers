# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# Draw variable number of lines - PyOpenGL
# https://stackoverflow.com/questions/64079973/draw-variable-number-of-lines-pyopengl/64080275#64080275
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Draw lines and polygons
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line(vertices):
    glBegin(GL_LINE_STRIP)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

def set_projection(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, h, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)

pygame.init()
display_size = (640, 480)
pygame.display.set_mode(display_size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
clock = pygame.time.Clock()

set_projection(*pygame.display.get_surface().get_size())
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

lines = [[]]

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            set_projection(event.w, event.h)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                lines[-1].append(event.pos)
            if event.button == 3:
                lines.append([])

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    for line in lines[:-1]:
       draw_line(line)  
    draw_line(lines[-1] + [pygame.mouse.get_pos()])  
    pygame.display.flip()
    
pygame.quit()
exit()