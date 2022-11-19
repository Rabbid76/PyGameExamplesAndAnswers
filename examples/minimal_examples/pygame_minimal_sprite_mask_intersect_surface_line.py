# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Make a line as a sprite with its own collision in Pygame
# https://stackoverflow.com/questions/34456195/make-a-line-as-a-sprite-with-its-own-collision-in-pygame/65324946#65324946
#
# GitHub - Sprite, Group and Sprite mask - Sprite mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import os
import math
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Line(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center = (x, y))
        self.angle = 0
    def update(self):
        vec = round(math.cos(self.angle * math.pi / 180) * 100), round(math.sin(self.angle * math.pi / 180) * 100)
        self.angle = (self.angle + 1) % 360
        self.image.fill(0)
        pygame.draw.line(self.image, (255, 255, 0), (100 - vec[0], 100 - vec[1]), (100 + vec[0], 100 + vec[1]), 5)
        self.mask = pygame.mask.from_surface(self.image)
        
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

sprite_image = pygame.image.load('icon/AirPlaneFront1-128.png').convert_alpha()
moving_object = SpriteObject(0, 0, sprite_image)
line_object = Line(*window.get_rect().center)
all_sprites = pygame.sprite.Group([moving_object, line_object])
red = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
    all_sprites.update()

    if pygame.sprite.collide_mask(moving_object, line_object):
        red = min(255, red+4)
    else: 
        red = 0

    window.fill((red, 0, 0))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()