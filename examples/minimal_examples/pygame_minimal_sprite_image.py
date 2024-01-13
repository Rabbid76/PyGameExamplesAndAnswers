# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How to use sprites in PyGame?
# https://stackoverflow.com/questions/73924256/how-to-use-sprites-in-pygame/73924281#73924281
#
# Making and using pygame sprites for donkey kong style game
# https://stackoverflow.com/questions/68566126/making-and-using-pygame-sprites-for-donkey-kong-style-game/68600795#68600795
#
# GitHub - Sprite, Group and Sprite mask - Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

# https://replit.com/@Rabbid76/PyGame-Sprite

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, center_pos, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = center_pos)
    
    def update(self, surf):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_d]-keys[pygame.K_a]) * 5
        self.rect.y += (keys[pygame.K_s]-keys[pygame.K_w]) * 5
        self.rect.clamp_ip(surf.get_rect())

player_surf = pygame.image.load('icon/Bird64.png').convert_alpha()
player = Player(window.get_rect().center, player_surf)
all_sprites = pygame.sprite.Group([player])

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update(window)

    window.fill(0)
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()