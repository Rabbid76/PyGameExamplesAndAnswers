# My pygame/pyopengl code seems to apply a texture to every surface
# https://stackoverflow.com/questions/68902541/my-pygame-pyopengl-code-seems-to-apply-a-texture-to-every-surface/68902623#68902623

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))
import pygame
from OpenGL.GL import *

def surfaceToTexture(pygame_surface):
    texture_oj = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_oj)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    rgba_surface = pygame.image.tostring(pygame_surface, 'RGBA')
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, *pygame_surface.get_size(), 0, GL_RGBA, GL_UNSIGNED_BYTE, rgba_surface)
    glBindTexture(GL_TEXTURE_2D, 0)
    return texture_oj

def drawTextrue(texture_obj, rect):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_obj)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(rect.left, rect.bottom)
    glTexCoord2f(0, 1); glVertex2f(rect.left, rect.top)
    glTexCoord2f(1, 1); glVertex2f(rect.right, rect.top)
    glTexCoord2f(1, 0); glVertex2f(rect.right, rect.bottom)
    glEnd()
    glDisable(GL_TEXTURE_2D)


pygame.init()
window = pygame.display.set_mode((300, 300), pygame.OPENGL | pygame.DOUBLEBUF | pygame.OPENGLBLIT)
clock = pygame.time.Clock()

surf = pygame.image.load('icon/Ice64.png').convert_alpha()
surf_rect = surf.get_rect()
surf_tecture = surfaceToTexture(surf)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, window.get_width(), 0, window.get_height(), -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT)

    glDisable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    surf_rect.center = window.get_rect().center
    drawTextrue(surf_tecture, surf_rect)

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()