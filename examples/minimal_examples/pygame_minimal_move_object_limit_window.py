# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# GitHub - PyGameExamplesAndAnswers - Keys and keyboard events - Keys
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md 

import pygame

pygame.init()

pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

object_rect = pygame.Rect(pygame.display.get_surface().get_rect().center, (0, 0)).inflate(30, 30)
vel = 5

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    object_rect.move_ip(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel,
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel)
        
    object_rect.clamp_ip(pygame.display.get_surface().get_rect())

    pygame.display.get_surface().fill([64] * 3)
    pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), object_rect)
    pygame.display.flip()

pygame.quit()
exit()