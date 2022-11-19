# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Why We Have to Use self.rect and self.image to Determine Rect and Surf on Sprites?
# https://stackoverflow.com/questions/68454667/why-we-have-to-use-self-rect-and-self-image-to-determine-rect-and-surf-on-sprite/68456266#68456266
#
# GitHub - Sprite, Group and Sprite mask - Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, center_pos):
        super().__init__() 
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center = center_pos)
    
    def update(self, surf):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_d]-keys[pygame.K_a]) * 5
        self.rect.y += (keys[pygame.K_s]-keys[pygame.K_w]) * 5
        self.rect.clamp_ip(surf.get_rect())

all_sprites = pygame.sprite.Group([Player(window.get_rect().center)])

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