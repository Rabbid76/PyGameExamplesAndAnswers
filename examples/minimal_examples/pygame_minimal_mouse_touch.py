# pygame.mouse module
# https://www.pygame.org/docs/ref/mouse.html
#
# How to detect touch screen clicks in python?
# https://stackoverflow.com/questions/69024021/how-to-detect-touch-screen-clicks-in-python/69032776#69032776
#
# GitHub - Mouse - Mouse and mouse event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont(None, 100)
clock = pygame.time.Clock()
text = font.render("Text", True, (255, 255, 0))

bomb = pygame.image.load('icon/Bomb-256.png').convert_alpha()
bomb_rect = bomb.get_rect(center = window.get_rect().center)
bomb_mask = pygame.mask.from_surface(bomb)
click_count = 0
click_text = font.render('touch: ' + str(click_count), True, "black")

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            image_x, image_y = event.pos[0] - bomb_rect.x, event.pos[1] - bomb_rect.y
            if bomb_rect.collidepoint(event.pos) and bomb_mask.get_at((image_x, image_y)):
                click_count += 1
                click_text = font.render('touch: ' + str(click_count), True, "black")

    window.fill((255, 255, 255))
    window.blit(bomb, bomb_rect)
    window.blit(click_text, click_text.get_rect(topleft = (20, 20)))
    pygame.display.flip()

pygame.quit()
exit()