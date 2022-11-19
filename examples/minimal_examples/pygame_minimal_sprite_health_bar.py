# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How to put a health bar over the sprite in pygame
# https://stackoverflow.com/questions/64867475/how-to-put-a-health-bar-over-the-sprite-in-pygame/64878954#64878954  
#
# GitHub - Sprite, Group and Sprite mask - Rotate Sprite - Health Bar
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# 

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def draw_health_bar(surf, pos, size, borderC, backC, healthC, progress):
    pygame.draw.rect(surf, backC, (*pos, *size))
    pygame.draw.rect(surf, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+1, pos[1]+1)
    innerSize = ((size[0]-2) * progress, size[1]-2)
    rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
    pygame.draw.rect(surf, healthC, rect)
    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load('icon/CarBlue64.png')
        self.original_image = pygame.transform.rotate(self.original_image, 90)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = pygame.math.Vector2((0, -1))
        self.velocity = 5
        self.position = pygame.math.Vector2(x, y)
        self.health = 10

    def point_at(self, x, y):
        self.direction = pygame.math.Vector2(x, y) - self.rect.center
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        angle = self.direction.angle_to((0, -1))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, x, y, clamp_rect):
        self.position -= self.direction * y * self.velocity
        self.position += pygame.math.Vector2(-self.direction.y, self.direction.x) * x * self.velocity
        self.rect.center = round(self.position.x), round(self.position.y)

        test_rect = self.rect.clamp(clamp_rect)
        if test_rect.x != self.rect.x:
            self.rect.x = test_rect.x
            self.position.x = self.rect.centerx
            self.health = max(0, self.health - 1)
        if test_rect.y != self.rect.y:
            self.rect.y = test_rect.y
            self.position.y = self.rect.centery
            self.health = max(0, self.health - 1)

    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.original_image.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 10
        draw_health_bar(surf, health_rect.topleft, health_rect.size, 
                (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health/max_health)    

window = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()

player = Player(200, 200)
all_sprites = pygame.sprite.Group(player)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            player.point_at(*event.pos)

    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    if any(keys) or any(mouse_buttons):
        player.move(0, -1, window.get_rect())

    window.fill((127, 127, 127))
    pygame.draw.rect(window, (255, 0, 0), window.get_rect(), 3)
    all_sprites.draw(window)
    player.draw_health(window)
    pygame.display.update()

pygame.quit()
exit()