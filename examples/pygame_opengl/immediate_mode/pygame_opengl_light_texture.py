# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# How do I add an image as texture of my 3D cube in pyopengl
# https://stackoverflow.com/questions/67367424/how-do-i-add-an-image-as-texture-of-my-3d-cube-in-pyopengl/67367851#67367851 
#
# I've been trying to texture this cube, it is textured with the image but not in the right way
# https://stackoverflow.com/questions/57540156/ive-been-trying-to-texture-this-cube-it-is-textured-with-the-image-but-not-in/57542230#57542230
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Primitive and Mesh 
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Cube:
  
    def __init__(self):
        self.v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        self.nv = [(0,0,-1), (0,0,1), (-1,0,0), (1,0,0), (0,-1,0), (0,1,0)]
        self.uv = [(0, 0), (0, 1), (1, 1), (1, 0)]
        self.surfaces = [(0,1,2,3), (5,4,7,6), (4,0,3,7),(1,5,6,2), (4,5,1,0), (3,2,6,7)]

    def draw(self):
        glEnable(GL_DEPTH_TEST)
        glBegin(GL_QUADS)
        for i, quad in enumerate(self.surfaces):
            glNormal3fv(self.nv[i])
            for ti, iv in enumerate(quad):
                glTexCoord2fv(self.uv[ti])
                glVertex3fv(self.v[iv])
        glEnd()

        glDisable( GL_POLYGON_OFFSET_FILL )

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

image = pygame.image.load('texture/ObjectSheet.png')
datas = pygame.image.tostring(image, 'RGBA')
texID = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texID)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

glEnable(GL_TEXTURE_2D)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1))

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

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.draw()    

    if take_screenshot: 
        screenshot(window, "cube.png")
    pygame.display.flip()

pygame.quit()
exit()