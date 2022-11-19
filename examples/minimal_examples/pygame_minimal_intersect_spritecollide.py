# pygame.Rect object
# https://www.pygame.org/docs/ref/rect.html#pygame.Rect
#
# How do I detect collision in pygame?
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame/65064907#65064907
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Overview
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
#
# https://replit.com/@Rabbid76/PyGame-spritecollide

import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))

sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((75, 75))
sprite1.image.fill((255, 0, 0))
sprite1.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)
sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((75, 75))
sprite2.image.fill((0, 255, 0))
sprite2.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)

all_group = pygame.sprite.Group([sprite2, sprite1])
test_group = pygame.sprite.Group(sprite2)

group2 = pygame.sprite.Group(sprite1)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    sprite1.rect.center = pygame.mouse.get_pos()
    collide = pygame.sprite.spritecollide(sprite1, test_group, False)

    enemytilecollision = pygame.sprite.groupcollide(group2, test_group, False, False)
    for tile, collidingEnemies in enemytilecollision.items():
        for enemy in collidingEnemies:
            # tile collides with enemy 
            # [...]
            print(tile.rect, enemy.rect)
    
    window.fill(0)
    all_group.draw(window)
    for s in collide:
        pygame.draw.rect(window, (255, 255, 255), s.rect, 5, 1)
    pygame.display.flip()

pygame.quit()
exit()
