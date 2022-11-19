# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# GitHub - Sprite, Group and Sprite mask - Rotate Sprite - Follow mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

obstacle = pygame.sprite.Sprite()
obstacle.image = pygame.Surface((40, 40))
obstacle.image.fill((255, 0, 0))
obstacle.rect = obstacle.image.get_rect(center = window.get_rect().center)

player = pygame.sprite.Sprite()
player.image = pygame.Surface((40, 40))
player.image.fill((0, 255, 0))
player.rect = obstacle.image.get_rect(center = (100, 100))

all_sprites = pygame.sprite.Group([player, obstacle])

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    player.rect.x += (keys[pygame.K_d]-keys[pygame.K_a]) * 5
    player.rect.y += (keys[pygame.K_s]-keys[pygame.K_w]) * 5
    player.rect.clamp_ip(window.get_rect())

    back_color = (255, 127, 127) if pygame.sprite.collide_rect(player, obstacle) else (127, 127, 127)
    window.fill(back_color)
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()