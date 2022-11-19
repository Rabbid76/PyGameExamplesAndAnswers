# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# [How to move Sprite in Pygame
# https://stackoverflow.com/questions/16183265/how-to-move-sprite-in-pygame/66515040#66515040
#
# How can I make a sprite move when key is held down
# https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down/64611463#64611463
#
# GitHub - Motion and movement
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class Bird(object):
    def __init__(self, x, y):
        self.image =  pygame.image.load('icon/Bird64.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def draw(self, surf):
        surf.blit(self.image, self.rect)

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
player = Bird(*window.get_rect().center)

run = True
while run:
    clock.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
    
    keys = pygame.key.get_pressed()
    move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    player.move(move_x * 5, move_y * 5)

    window.fill([255, 255, 255])
    player.draw(window)
    pygame.display.update()

pygame.quit()
exit()