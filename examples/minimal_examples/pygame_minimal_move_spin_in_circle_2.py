# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Ship moves up and left faster than down and right when rotating in pygame
# https://stackoverflow.com/questions/62411259/ship-moves-up-and-left-faster-than-down-and-right-when-rotating-in-pygame/65347117#65347117
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 

import os
import math
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class Player(pygame.sprite.Sprite):
    def __init__(self, img, pos, angle):
        super().__init__()
        img.set_colorkey((0, 0, 0, 0))
        self.angle = angle
        self.original_img = pygame.transform.rotate(img, 180)
        self.image = self.original_img
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos
        self.speed = 5
        self.angle_step = 5
        self._update_image() 

    def _update_image(self):
        x, y = self.rect.center
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.angle += self.angle_step
        self._update_image()
        nx = math.sin(math.radians(self.angle)) * self.speed + self.pos[0]
        ny = math.cos(math.radians(self.angle)) * self.speed + self.pos[1]
        self.pos = (nx, ny)
        self.rect.center = round(nx), round(ny)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
background = pygame.Surface(window.get_size())
background.set_alpha(5)

all_sprites = pygame.sprite.Group()
ship_image = pygame.image.load('icon/Rocket64.png').convert_alpha()
player = Player(ship_image, (window.get_width()//2-40, window.get_height()//2+40), 45)
all_sprites.add(player)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()

    window.blit(background, (0, 0))
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()
exit()