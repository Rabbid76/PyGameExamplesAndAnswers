# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# “Spin” coin image in python, pygame clicker game
# https://stackoverflow.com/questions/65173270/spin-coin-image-in-python-pygame-clicker-game/65173486#65173486  
#
# GitHub - PyGameExamplesAndAnswers - Scale and zoom - Spin effect through scaling
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_scale_and_zoom.md

import pygame
import math

pygame.init()
window = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

coin = pygame.Surface((160, 160), pygame.SRCALPHA)
pygame.draw.circle(coin, (255, 255, 0), (80, 80), 80, 10)
pygame.draw.circle(coin, (128, 128, 0), (80, 80), 75)
cointext = pygame.font.SysFont(None, 80).render("10", True, (255, 255, 0))
coin.blit(cointext, cointext.get_rect(center = coin.get_rect().center))
coin_rect = coin.get_rect(center = window.get_rect().center)
angle = 0

run = True
while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)    
    
    new_width = round(math.sin(math.radians(angle)) * coin_rect.width) 
    angle += 2
    rot_coin = coin if new_width >= 0 else pygame.transform.flip(coin, True, False) 
    rot_coin = pygame.transform.scale(rot_coin, (abs(new_width), coin_rect.height))
    window.blit(rot_coin, rot_coin.get_rect(center = coin_rect.center))
    
    pygame.display.flip()

pygame.quit()
exit()
