# pygame.math module, pygame.math.Vector2 object
# https://www.pygame.org/docs/ref/math.html
#
# GitHub - Move towards target - Follow target or mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md
#
# https://replit.com/@Rabbid76/PyGame-FollowBall

import os
import math
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class MarbelSprite(pygame.sprite.Sprite):
    def __init__(self, x, ground, diameter, velocity, filename):
        pygame.sprite.Sprite.__init__(self)
        try:
            self.image = pygame.transform.smoothscale(pygame.image.load(filename).convert_alpha(), (diameter, diameter))
        except:     
            self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 128, 0), (diameter // 2, diameter // 2), diameter // 2)
        self.original_image = self.image
        self.rect = self.image.get_rect(midbottom = (x, ground))
        self.diameter = diameter
        self.x = x
        self.velocity = velocity
        self.move_x = 0
        self.follow = None
        self.angle = 0
        
    def update(self, time, restriction):
        move_x = 0
        prev_x = self.x
        if self.move_x != 0:
            move_x = self.move_x * self.velocity * time
        elif self.follow:
            dx = self.follow.rect.centerx - self.x
            move_x = (-1 if dx < 0 else 1) * min(self.velocity * time, abs(dx))
        self.x += move_x
        self.x = max(restriction.left + self.diameter // 2, min(restriction.right - self.diameter // 2, self.x))
        self.rect.centerx = round(self.x)
        self.angle -= (self.x - prev_x) / self.diameter * 180 / math.pi
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)

pygame.init()
window = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

ground_level = 220
object = MarbelSprite(window.get_rect().centerx, ground_level, 100, 0.4, 'icon/BaskteBall64.png')
follower = MarbelSprite(window.get_width() // 4, ground_level, 50, 0.2, 'icon/TennisBall64.png')
all_sprites = pygame.sprite.Group([object, follower])

run = True
while run:
    time = clock.tick(60)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    object.move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    follower.follow = object
    all_sprites.update(time, window.get_rect())

    window.fill((32, 64, 224))
    pygame.draw.rect(window, (80, 64, 64), (0, ground_level, window.get_width(), window.get_height()-ground_level))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()