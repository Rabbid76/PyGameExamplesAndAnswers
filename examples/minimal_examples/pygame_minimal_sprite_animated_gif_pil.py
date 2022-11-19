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
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Animated sprite from few images
# https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images/64668964#64668964
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load animated GIF
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md
#
# GitHub - Sprite, Group and Sprite mask - Animation, timing and Sprite sheet
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SpriteAnimation

import os
import pygame
from PIL import Image, ImageSequence
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames
 
class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0
    def update(self):
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = pygame.display.get_surface().get_width()

pygame.init()
window = pygame.display.set_mode((300, 200))
clock = pygame.time.Clock()
ground = window.get_height() * 3 // 4

gifFrameList = loadGIF('animated_clipart/stone_age_1.gif')
animated_sprite = AnimatedSpriteObject(window.get_width() // 2, ground, gifFrameList)    
all_sprites = pygame.sprite.Group(animated_sprite)

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()

    window.fill((127, 192, 255), (0, 0, window.get_width(), ground))
    window.fill((255, 127, 64), (0, ground, window.get_width(), window.get_height() - ground))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()