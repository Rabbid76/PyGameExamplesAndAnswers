# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# GL_LINES not showing up on top of cube?
# https://stackoverflow.com/questions/56624147/gl-lines-not-showing-up-on-top-of-cube/56624975#56624975
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

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

        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset( 1.0, 1.0 )

        glBegin(GL_QUADS)
        for i, quad in enumerate(self.surfaces):
            glColor3fv(self.colors[i])
            for iv in quad:
                glVertex3fv(self.v[iv])
        glEnd()

        glDisable(GL_POLYGON_OFFSET_FILL)

def set_projection(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def screenshot(display_surface, filename):
    size = display_surface.get_size()
    buffer = glReadPixels(0, 0, *size, GL_RGBA, GL_UNSIGNED_BYTE)
    screen_surf = pygame.image.fromstring(buffer, size, "RGBA")
    pygame.image.save(screen_surf, filename)

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
        screenshot(window, "cube.png")
    pygame.display.flip()
    
pygame.quit()
exit()