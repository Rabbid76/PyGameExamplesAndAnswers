# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Rotation of a sprite on a circle
# https://stackoverflow.com/questions/26517579/rotation-of-a-sprite-on-a-circle/65332120#65332120
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import os
import math
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class RotatingSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)     
        self.original_image = pygame.image.load('icon/arrow_up.png').convert_alpha()
        self.image = self.original_image        
        self.rect = self.image.get_rect()  
        self.angle = 0

    def initLoc(self, pos, radius):
        self.pos = pos
        self.radius = radius

    def update(self):
        center = pygame.math.Vector2(self.pos) + pygame.math.Vector2(0, -self.radius).rotate(-self.angle) 
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = (round(center.x), round(center.y)))            

    def turnLeft(self):
        self.angle += 1
   

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

my_sprite = RotatingSprite()
my_sprite.initLoc(window.get_rect().center, 100)
all_sprites = pygame.sprite.Group(my_sprite)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    my_sprite.turnLeft()
    all_sprites.update()

    window.fill(0)
    pygame.draw.circle(window, (127, 127, 127), window.get_rect().center, 100, 1)
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()