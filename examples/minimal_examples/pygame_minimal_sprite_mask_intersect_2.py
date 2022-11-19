# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Can't figure out how to check mask collision between two spritese
# https://stackoverflow.com/questions/71535185/cant-figure-out-how-to-check-mask-collision-between-two-sprites/71536155#71536155
#
# GitHub - Sprite, Group and Sprite mask - Sprite mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SpriteMask

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image )

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((400, 400))
size = window.get_size()

object_surf = pygame.image.load('icon/AirPlaneFront1-128.png').convert_alpha()
obstacle_surf = pygame.image.load('icon/Rocket64.png').convert_alpha()

moving_object = SpriteObject(0, 0, object_surf)
obstacle = SpriteObject(size[0] // 2, size[1] // 2, obstacle_surf)
all_sprites = pygame.sprite.Group([moving_object, obstacle])

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    moving_object.rect.center = pygame.mouse.get_pos()
    collide = pygame.sprite.collide_mask(moving_object, obstacle)
    
    window.fill((255, 0, 0) if collide else (0, 0, 64))
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()
exit()