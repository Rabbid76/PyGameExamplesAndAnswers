# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Video and Camera
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md#mouse-position-and-unproject
#
# Draw a background video behind a 3D model in OpenGL
# https://stackoverflow.com/questions/68533162/draw-a-background-video-behind-a-3d-model-in-opengl/68533213#68533213

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame_opengl_begin_end_objloader import *
import cv2
from PIL import Image

class ImageLoader:
    def __init__(self):
        self.width, self.height, self.img_data = 0, 0, None
        self.texture_obj = glGenTextures(1)

    def load(self, image):
        tx_image = cv2.flip(image, 0)
        tx_image = Image.fromarray(tx_image)
        width = tx_image.size[0]
        height = tx_image.size[1]
        self.img_data = tx_image.tobytes('raw', 'BGRX', 0, -1)
        glBindTexture(GL_TEXTURE_2D, self.texture_obj)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        if self.width != width or self.height != height:
            self.width = width
            self.height = height
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.img_data)
        else:
            glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, self.width, self.height, GL_RGBA, GL_UNSIGNED_BYTE, self.img_data)
        glBindTexture(GL_TEXTURE_2D, 0)

    def draw(self):
        glColor4f(1, 1, 1, 1)
        glEnable(GL_TEXTURE_2D)  
        glBindTexture(GL_TEXTURE_2D, self.texture_obj)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(0, 0)
        glTexCoord2f(1, 0)
        glVertex2f(self.width, 0)
        glTexCoord2f(1, 1)
        glVertex2f(self.width, self.height)
        glTexCoord2f(0, 1)
        glVertex2f(0, self.height)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, 0)


cap = cv2.VideoCapture(0)
width, height = int(cap.get(3)), int(cap.get(4))
pygame.init()
pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

image_loader = ImageLoader()
model = OBJ('model/wavefront/bunny.obj')
box = model.box()
center = [(box[0][i] + box[1][i])/2 for i in range(3)]
size = [box[1][i] - box[0][i] for i in range(3)]
max_size = max(size)
distance = 10
scale = distance / max_size
angle = 0

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, height, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glDisable(GL_DEPTH_TEST)
    success, image = cap.read()
    if success:
        image_loader.load(image)
    image_loader.draw()
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (width/height), 0.1, distance*2)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0, -distance)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnable(GL_DEPTH_TEST)
    glColor4f(1, 0.5, 0.2, 1)
    glPushMatrix()
    glRotate(angle, 0, 1, 0)
    glScale(scale, scale, scale)
    glTranslate(-center[0], -center[1], -center[2])
    model.render()
    glPopMatrix()
    angle += 1

    pygame.display.flip()

pygame.quit()
quit()