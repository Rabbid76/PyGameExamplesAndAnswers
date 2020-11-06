# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How do I rotate an image around its center using PyGame?
# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
#
# How can you rotate an image around an off center pivot in Pygame
# https://stackoverflow.com/questions/59909942/how-can-you-rotate-an-image-around-an-off-center-pivot-in-pygame/59909946#59909946
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_rotate.md
#
# GitHub - Sprite, Group and Sprite mask - Drag Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import os
import math
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class SpriteRotate(pygame.sprite.Sprite):

    def __init__(self, imageName, pos, pivot):
        super().__init__() 
        self.image = pygame.image.load(imageName)
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft = (pos[0]-pivot[0], pos[1]-pivot[1]))
        self.pos   = pos
        self.pivot = pivot
        self.angle = 0

    def update(self):
        
        # calcaulate the axis aligned bounding box of the rotated image
        w, h         = self.original_image.get_size()
        sin_a, cos_a = math.sin(math.radians(self.angle)), math.cos(math.radians(self.angle)) 
        min_x, min_y = min([0, sin_a*h, cos_a*w, sin_a*h + cos_a*w]), max([0, sin_a*w, -cos_a*h, sin_a*w - cos_a*h])

        # calculate the translation of the pivot 
        pivot        = pygame.math.Vector2(self.pivot[0], -self.pivot[1])
        pivot_rotate = pivot.rotate(self.angle)
        pivot_move   = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (self.pos[0] - self.pivot[0] + min_x - pivot_move[0], self.pos[1] - self.pivot[1] - min_y + pivot_move[1])

        # get a rotated image
        self.image  = pygame.transform.rotate(self.original_image, self.angle)
        self.rect   = self.image.get_rect(topleft = (round(origin[0]), round(origin[1])))
        self.angle += 10
  
pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

boomerang = SpriteRotate('icon/Boomerang64.png', (200, 200), (48, 21))
all_sprites = pygame.sprite.Group(boomerang)

frame = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pos = (200 + math.cos(frame * 0.05)*100, 200 + math.sin(frame * 0.05)*50)
    boomerang.pos = pos
    all_sprites.update()

    screen.fill(0)
    
    all_sprites.draw(screen)
    #pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    #pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    #pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

    pygame.display.flip()
    frame += 1
    
pygame.quit()
exit()

