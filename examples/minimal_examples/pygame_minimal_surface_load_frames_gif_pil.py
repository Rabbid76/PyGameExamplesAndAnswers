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
from PIL import Image, ImageSequence
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../screenshot'))

# GIF decoder does not correctly handle images with different palettes
# https://github.com/python-pillow/Pillow/issues/1717
def _convert_mode(im, initial_call=False):
    # convert on the fly (EXPERIMENTAL -- I'm not sure PIL
    # should automatically convert images on save...)
    if Image.getmodebase(im.mode) == "RGB":
        if initial_call:
            palette_size = 256
            if im.palette:
                palette_size = len(im.palette.getdata()[1]) // 3
            return im.convert("P", palette=1, colors=palette_size)
        else:
            return im.convert("P", dither=None)
    return im.convert("L")

def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    if pilImage.format == 'GIF' and pilImage.is_animated:
        for frame in ImageSequence.Iterator(pilImage):
            pygameImage = pilImageToSurface(frame.convert('RGBA'))
            frames.append(pygameImage)
    else:
        frames.append(pilImageToSurface(pilImage))
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