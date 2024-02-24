# PIL GIF:
# 
#    - Extracting The Frames Of An Animated GIF Using Pillow
#      https://pythontic.com/image-processing/pillow/extract%20frames%20from%20animated%20gif
#
#    - How to: Extract frames from an animated gif
#    - https://www.kite.com/python/examples/4892/pil-extract-frames-from-an-animated-gif
#
# PIL PyGame:
#
#    - PIL and pygame.image
#    - https://stackoverflow.com/questions/25202092/pil-and-pygame-image
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How do I make a sprite as a gif in pygame?
# https://stackoverflow.com/questions/64179680/how-do-i-make-a-sprite-as-a-gif-in-pygame/64182074#64182074
#
# How can I load an animated GIF and get all of the individual frames in PyGame?
# https://stackoverflow.com/questions/29571399/how-can-i-load-an-animated-gif-and-get-all-of-the-individual-frames-in-pygame
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load animated GIF
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import os
import pygame
import cv2
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../screenshot'))

def cv2ImageToSurface(cv2Image):
    size = cv2Image.shape[1::-1]
    format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
    cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()

def loadGIF(filename):
    gif = cv2.VideoCapture(filename)
    frames = []
    while True:
        ret, cv2Image = gif.read()
        if not ret:
            break
        pygameImage = cv2ImageToSurface(cv2Image)
        frames.append(pygameImage)
    return frames
 
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

gifFrameList = loadGIF('rubber_ball.gif')
currentFrame = 0

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill('black')

    rect = gifFrameList[currentFrame].get_rect(center = (250, 250))
    window.blit(gifFrameList[currentFrame], rect)
    currentFrame = (currentFrame + 1) % len(gifFrameList)
    
    pygame.display.flip()

pygame.quit()
exit()