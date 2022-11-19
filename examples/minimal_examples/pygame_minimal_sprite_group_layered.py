# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# pygame.sprite.LayeredUpdates.move_to_front() does not work
# https://stackoverflow.com/questions/69365433/pygame-sprite-layeredupdates-move-to-front-does-not-work/69365563#69365563
#
# GitHub - Sprite, Group and Sprite mask - Layers
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

obstacle = pygame.sprite.Sprite()
obstacle.image = pygame.Surface((50, 50))
obstacle.image.fill((128, 128, 128))
obstacle.rect = obstacle.image.get_rect(center = (140, 140))

player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill((255, 0, 0))
player.rect = obstacle.image.get_rect(center = (160, 160))

layered_sprites = pygame.sprite.LayeredUpdates([player, obstacle])
layered_sprites.change_layer(player, 1)
layered_sprites.change_layer(obstacle, 2)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                layered_sprites.move_to_front(player)
            if event.button == 3:
                layered_sprites.move_to_front(obstacle)

    window.fill(0)
    layered_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()