import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))
import pygame
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

pygame.init()
window = pygame.display.set_mode((300, 300), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

surf = pygame.image.load('icon/Ice64.png').convert_alpha()
surf_rect = surf.get_rect(center = window.get_rect().center)
rot_surf = pygame.transform.rotate(surf, -90)

run = True
while run:
    clock.tick(100)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_LINE_LOOP)
    glVertex3f(-0.5, 0.5, 0)
    glVertex3f(-0.5, -0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(0.5, 0.5, 0)
    glEnd()

    glWindowPos2i(*surf_rect.topleft)
    glDrawPixels(*surf_rect.size, GL_RGB, GL_UNSIGNED_BYTE, pygame.surfarray.pixels3d(rot_surf))

    pygame.display.flip()

pygame.quit()
exit()