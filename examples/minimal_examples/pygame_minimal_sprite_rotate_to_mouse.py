# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How do I rotate a sprite towards the mouse and move it?
# https://stackoverflow.com/questions/64805267/in-the-pygame-module-no-matter-what-i-change-the-coordinates-of-player-to-it-w/64806308#64806308
#
# GitHub - Sprite, Group and Sprite mask - Rotate Sprite - Follow mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SpriteRotateToMouse

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load('icon/arrow_up.png')
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (x, y))
        self.velocity = 5

    def point_at(self, x, y):
        direction = pygame.math.Vector2(x, y) - self.rect.center
        angle = direction.angle_to((0, -1))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, x, y):
        self.rect.move_ip(x * self.velocity, y * self.velocity)


pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

player = Player(*window.get_rect().center)
all_sprites = pygame.sprite.Group(player)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.point_at(*pygame.mouse.get_pos())
    keys = pygame.key.get_pressed()
    player.move(keys[pygame.K_d]-keys[pygame.K_a], keys[pygame.K_s]-keys[pygame.K_w])

    window.fill((255, 255, 255))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()