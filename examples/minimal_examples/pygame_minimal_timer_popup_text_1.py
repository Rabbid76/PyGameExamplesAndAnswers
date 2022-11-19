# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# Pygame "pop up" text
# https://stackoverflow.com/questions/70996802/pygame-pop-up-text/70996856#70996856
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - For a period of time
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 200))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

text = font.render("+1", True, (0, 255, 0))
text_pos_and_time = []
pop_up_seconds = 1

player = pygame.Rect(0, 80, 40, 40)
coins = [pygame.Rect(i*100+100, 80, 40, 40) for i in range(3)]

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    player.x = (player.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 3) % 300    

    current_time = pygame.time.get_ticks()
    for coin in coins[:]:
        if player.colliderect(coin):
            text_pos_and_time.append((coin.center, current_time + pop_up_seconds * 1000))
            coins.remove(coin)

    window.fill(0)    
    pygame.draw.rect(window, "red", player)
    for coin in coins:
        pygame.draw.circle(window, "yellow", coin.center, 20)
    for pos_time in text_pos_and_time[:]:
        if pos_time[1] > current_time:
            window.blit(text, text.get_rect(center = pos_time[0]))
        else:
            text_pos_and_time.remove(pos_time)    
    pygame.display.flip()

pygame.quit()
exit()