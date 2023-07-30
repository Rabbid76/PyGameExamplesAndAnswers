# Pygame + PyOpenGL Resolution Downscaling
# https://stackoverflow.com/questions/76795854/pygame-pyopengl-resolution-downscaling/76796567#76796567

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
window = pygame.display.set_mode((320, 320), pygame.OPENGL | pygame.DOUBLEBUF | pygame.OPENGLBLIT)
clock = pygame.time.Clock()

surf = pygame.image.load('icon/sunglasses.png').convert_alpha()
surf_rect = surf.get_rect()
surf_tecture = surfaceToTexture(surf)

scale = 16
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    width = window.get_width() // scale
    height = window.get_height() // scale

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClearColor(0.5, 0.5, 0.5, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glDisable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    surf_rect.center = (width // 2, height // 2)
    drawTextrue(surf_tecture, surf_rect)

    pygame.display.flip()
    clock.tick(100)

size = window.get_size()
buffer = glReadPixels(0, 0, *size, GL_RGBA, GL_UNSIGNED_BYTE)
pygame.display.flip()
screen_surf = pygame.image.fromstring(buffer, size, "RGBA")
#pygame.image.save(screen_surf, "pygame_opengl_surface_to_texture_scaled.png")

pygame.quit()
exit()