# PyOpenGL
# http://pyopengl.sourceforge.net/
#
# PyOpenGL texture isn't displaying correctly
# https://stackoverflow.com/questions/68468091/pyopengl-texture-isnt-displaying-correctly/68489022#68489022
#
# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Texture
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def loadTexture(filename):
    image = pygame.image.load(filename)
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    return texID

def drawQuad(textureID):
    verts = ((1, 1), (1,-1), (-1,-1), (-1,1))
    uvs = ((1, 0), (1, 1), (0, 1), (0, 0))
    glBindTexture(GL_TEXTURE_2D, textureID)
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    for v, uv in zip(verts, uvs):
        glTexCoord2fv(uv)
        glVertex2fv(v)
    glEnd()
    glDisable(GL_TEXTURE_2D)

pygame.init()
pygame.display.set_mode((200, 200), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, 1, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -5)
textID = loadTexture("icon/Bird64.png")

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawQuad(textID)
    pygame.display.flip()
    pygame.time.wait(10)
        
pygame.quit()        
exit()