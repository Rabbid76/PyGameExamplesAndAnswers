# pygame.key module
# https://www.pygame.org/docs/ref/key.html
# 
# How to make a character jump in Pygame?
# https://stackoverflow.com/questions/70591591/how-to-make-a-character-jump-in-pygame/70591592#70591592
# 
# How to make a circular object jump using pygame?
# https://stackoverflow.com/questions/62822322/how-to-make-a-circular-object-jump-using-pygame/62822601#62822601
# 
# GitHub - PyGameExamplesAndAnswers - Jump
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_jump.md
#
# https://replit.com/@Rabbid76/PyGame-JumpFloat#main.py

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

player = pygame.sprite.Sprite()
player.image = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.circle(player.image, (255, 0, 0), (15, 15), 15)
player.rect = player.image.get_rect(center = (150, 235))
all_sprites = pygame.sprite.Group([player])

y, vel_y = player.rect.bottom, 0
vel = 5
ground_y = 250
jump_height = 12
jump = False

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                vel_y = jump_height

    keys = pygame.key.get_pressed()    
    player.rect.centerx = (player.rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel) % 300
    
    if jump:
        if vel_y >= -jump_height:
            m = -1 if vel_y < 0 else 1
            f = 0.2 * m * (vel_y**2)
            vel_y -= 1
            y -= f
        else:
            jump = False
    player.rect.bottom = round(y)

    window.fill((0, 0, 64))
    pygame.draw.rect(window, (64, 64, 64), (0, 250, 300, 100))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit() 