# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# Adding a particle effect to my clicker game
# https://stackoverflow.com/questions/64793618/adding-a-particle-effect-to-my-clicker-game/64794954#64794954
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - For a period of time
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame
import random

pygame.init()
window = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

coin = pygame.Surface((160, 160), pygame.SRCALPHA)
pygame.draw.circle(coin, (255, 255, 0), (80, 80), 80, 10)
pygame.draw.circle(coin, (128, 128, 0), (80, 80), 75)
cointext = pygame.font.SysFont(None, 80).render("10", True, (255, 255, 0, 255))
coin.blit(cointext, cointext.get_rect(center = coin.get_rect().center))
coin_rect = coin.get_rect(center = window.get_rect().center)

text = font.render("+10", True, (0, 255, 0))
text_pos_and_time = []

run = True
while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if coin_rect.collidepoint(event.pos):
                pos = pygame.math.Vector2(coin_rect.center) + pygame.math.Vector2(105, 0).rotate(random.randrange(360))
                text_pos_and_time.insert(0, ((round(pos.x), round(pos.y)), current_time + 1000))

    window.fill('black')    
    window.blit(coin, coin_rect)
    for i in range(len(text_pos_and_time)):
        pos, text_end_time = text_pos_and_time[i] 
        if text_end_time > current_time:
            window.blit(text, text.get_rect(center = pos))
        else:
            del text_pos_and_time[i:]
            break
    pygame.display.flip()

pygame.quit()
exit()