# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Read pygame window with open cv2
# https://stackoverflow.com/questions/68841168/read-pygame-window-with-open-cv/68842883#68842883
#
# Pygame surface to opencv image object (not file saving)
# https://stackoverflow.com/questions/72756330/pygame-surface-to-opencv-image-object-not-file-saving/72756521#72756521
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load OpenCV (cv2) image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import os
import pygame
import cv2
import numpy

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def pygameSurfaceToCv2Image(mysurface, x, y, w, h):
    selected_area =  mysurface.subsurface((x, y, w, h))
    img_array = numpy.array(pygame.surfarray.pixels3d(selected_area))
    image_object = numpy.transpose(img_array, (1, 0, 2))
    #image_object[:, :, [0, 2]] = image_object[:, :, [2, 0]]
    image_object = cv2.cvtColor(image_object, cv2.COLOR_RGB2BGR)
    return image_object

image = pygame.image.load('icon/Apple1-256.png')
apple_surf = pygame.Surface(image.get_size())
apple_surf.blit(image, (0, 0))
image_object = pygameSurfaceToCv2Image(apple_surf, 20, 20, 200, 120)
gray = cv2.cvtColor(image_object, cv2.COLOR_BGR2GRAY)
cv2.imshow("apple subsurface", image_object)
cv2.imshow("gray apple subsurface", gray)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill(0)
    window.blit(image, image.get_rect(center = window.get_rect().center))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()