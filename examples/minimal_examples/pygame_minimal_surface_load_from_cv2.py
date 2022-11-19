# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How do I convert an OpenCV (cv2) image (BGR and BGRA) to a pygame.Surface object
# https://stackoverflow.com/questions/64183409/how-do-i-convert-an-opencv-cv2-image-bgr-and-bgra-to-a-pygame-surface-object/64183410#64183410
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load OpenCV (cv2) image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import os
import pygame
import cv2
import numpy as np

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def cv2ImageToSurface(cv2Image):
    if cv2Image.dtype.name == 'uint16':
        cv2Image = (cv2Image / 256).astype('uint8')
    size = cv2Image.shape[1::-1]
    if len(cv2Image.shape) == 2:
        cv2Image = np.repeat(cv2Image.reshape(size[1], size[0], 1), 3, axis = 2)
        format = 'RGB'
    else:
        format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
        cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]    
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

cv2Image1 = cv2.imread('texture/woodtiles.jpg', cv2.IMREAD_GRAYSCALE)
cv2Image2 = cv2.imread('image/parrot1.png', cv2.IMREAD_UNCHANGED)
cv2Image3 = cv2.imread('icon/Apple1-256.png', cv2.IMREAD_UNCHANGED)
pygameSurface1 = cv2ImageToSurface(cv2Image1)
pygameSurface2 = cv2ImageToSurface(cv2Image2)
pygameSurface3 = cv2ImageToSurface(cv2Image3)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(pygameSurface1, pygameSurface1.get_rect(topleft = window.get_rect().inflate(-10, -10).topleft))
    window.blit(pygameSurface2, pygameSurface2.get_rect(center = window.get_rect().center))
    window.blit(pygameSurface3, pygameSurface3.get_rect(bottomright = window.get_rect().inflate(-10, -10).bottomright))
    pygame.display.flip()

#pygame.image.save(window, r'c:\temp\so_pygame__minimum_cv2_to_surface.png')

pygame.quit()
exit()