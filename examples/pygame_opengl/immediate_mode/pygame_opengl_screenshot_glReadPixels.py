# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# How to save pygame scene as jpeg?
# https://stackoverflow.com/questions/66209365/how-to-save-pygame-scene-as-jpeg/66209486#66209486
#
# Screenshots in OpenGL using python
# https://stackoverflow.com/questions/71661677/screenshots-in-opengl-using-python/71663843#71663843
#
# GitHub - PyGameExamplesAndAnswers - PyGame window and OpenGL context - Save rendering (Screenshot)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_window_and_context.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def screenshot(filename):
    viewport = glGetIntegerv(GL_VIEWPORT)
    size = viewport[2:]
    buffer = glReadPixels(0, 0, *size, GL_RGBA, GL_UNSIGNED_BYTE)
    screen_surf = pygame.image.fromstring(buffer, size, "RGBA")
    pygame.image.save(screen_surf, filename)

class Cube:
    def __init__(self):
        self.v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        self.surfaces = [(0,1,2,3), (5,4,7,6), (4,0,3,7),(1,5,6,2), (4,5,1,0), (3,2,6,7)]
        self.colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (1,0.5,0)]

    def draw(self):
        glEnable(GL_DEPTH_TEST)
        glBegin(GL_QUADS)
        for i, quad in enumerate(self.surfaces):
            glColor3fv(self.colors[i])
            for iv in quad:
                glVertex3fv(self.v[iv])
        glEnd()

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
    take_screenshot = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            set_projection(event.w, event.h)
        elif event.type == pygame.KEYDOWN:
            take_screenshot = True

    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_x, 1, 0, 0)
    angle_x += 1
    angle_y += 0.4

    glClearColor(0.5, 0.5, 0.5, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.draw()   
    if take_screenshot: 
        screenshot("cube.png")
    pygame.display.flip()
    
pygame.quit()
exit()