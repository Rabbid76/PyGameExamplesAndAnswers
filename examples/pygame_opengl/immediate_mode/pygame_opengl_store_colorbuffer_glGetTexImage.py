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

def store_texture(tex_obj, size, filename):
    glBindTexture(GL_TEXTURE_2D, tex_obj)
    image_buffer = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_UNSIGNED_BYTE)
    screen_surf = pygame.image.fromstring(image_buffer, size, "RGBA")
    pygame.image.save(screen_surf, filename)

def create_framebuffer(fb_size):
    depth_buffer_obj = glGenRenderbuffers(1)
    glBindRenderbuffer(GL_RENDERBUFFER, depth_buffer_obj)
    glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT24, fb_size[0], fb_size[1])
    color_tex_obj = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, color_tex_obj)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, fb_size[0], fb_size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, None)
    glBindTexture(GL_TEXTURE_2D, 0)
    fb_obj = glGenFramebuffers(1)
    glBindFramebuffer(GL_FRAMEBUFFER, fb_obj)
    glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, depth_buffer_obj)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, color_tex_obj, 0)
    if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
        print("incomplete framebuffer object")
    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    return fb_obj, color_tex_obj

pygame.init() 
window = pygame.display.set_mode((500, 500), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

fb_size = (50, 50)
fb_obj, color_tex_obj = create_framebuffer(fb_size)

gluPerspective(70, window.get_width() / window.get_height(), 0.1, 50.0)
glTranslatef(0, 0, -5)

run = True
while run:
    clock.tick(60)
    store_colorbuffer = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            store_colorbuffer = True

    glBindFramebuffer(GL_FRAMEBUFFER, fb_obj)
    glViewport (0, 0, fb_size[0], fb_size[1])
    glClearColor(0.1, 0.1, 0.1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotatef(1, 3, 1, 1)
    gluSphere(gluNewQuadric( ), 2.0, 32, 32)

    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glViewport(0, 0, 500, 500)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, color_tex_obj)
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0,0)
    glVertex2f(-1,-1)
    glTexCoord2f(1,0)
    glVertex2f(1,-1)
    glTexCoord2f(1,1)
    glVertex2f(1,1)
    glTexCoord2f(0,1)
    glVertex2f(-1,1)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

    if store_colorbuffer:

        store_texture(color_tex_obj, fb_size, "coorbuffer.png")
    pygame.display.flip()

pygame.quit() 
exit()