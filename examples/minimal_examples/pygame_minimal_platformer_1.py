# pygame.key module
# https://www.pygame.org/docs/ref/key.html
# 
# How to make a collision system in pygame?
# https://stackoverflow.com/questions/74332401/how-to-make-a-collision-system-in-pygame/74333777#74333777
# 
# GitHub - PyGameExamplesAndAnswers - Jump 'n' Run and Platformer
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_platformer.md

import pygame
import random

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    JUMP_ACCELERATION = -7
    def __init__(self, midbottom_pos):
        super().__init__() 
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.image.fill("red") 
        self.rect = self.image.get_rect(midbottom = midbottom_pos)
        self.y = self.rect.bottom
        self.vel_y = 0
        self.acc_y = 0
    def jump(self):
        self.acc_y = Player.JUMP_ACCELERATION
    def update(self, platforms):
        self.vel_y += GRAVITY
        self.y += self.vel_y
        self.rect.bottom = round(self.y + 1)
        colliders = pygame.sprite.spritecollide(self, platforms, False)
        if colliders:
            self.y = colliders[0].rect.top
            self.vel_y = self.acc_y
            self.y += self.vel_y
        elif self.y > window.get_height():
            self.y = 100
        self.acc_y = 0
        self.rect.bottom = round(self.y)

class Platform(pygame.sprite.Sprite):
    PLATFORM_SHIFT = 1.5
    def __init__(self, topleft_pos):
        super().__init__() 
        self.image = pygame.Surface((200, 10), pygame.SRCALPHA)
        self.image.fill("gray") 
        self.rect = self.image.get_rect(topleft = topleft_pos)
        self.x = self.rect.x
    def update(self):
        self.x -= Platform.PLATFORM_SHIFT
        self.rect.x = round(self.x)
        if self.rect.right <= 0:
            self.kill()

GRAVITY = 0.2
platfrom_group = pygame.sprite.Group(Platform((0, 250)))
player = Player((50, 100))
plyer_sprites = pygame.sprite.GroupSingle(player)

run = True
while run:
    clock.tick(100)
    acc_y = GRAVITY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                player.jump()

    platfrom_group.update()
    while platfrom_group.sprites()[-1].rect.right < window.get_width():
        last_platform_rect = platfrom_group.sprites()[-1].rect
        if last_platform_rect.top - 50 < 150:
            new_y = last_platform_rect.top + 50
        elif last_platform_rect.top + 50 > window.get_height() - 50:
            new_y = last_platform_rect.top - 50
        else:
            new_y = last_platform_rect.top + (50 if random.random() > 0.5 else -50)
        platfrom_group.add(Platform((last_platform_rect.right, new_y)))
        print(len(platfrom_group.sprites()))
    player.update(platfrom_group)

    window.fill((0, 0, 64))
    platfrom_group.draw(window)
    plyer_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit() 