# pygame.time module
# https://www.pygame.org/docs/ref/time.html
#
# How to wait some time in pygame?
# https://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame/64701602#64701602
#
# GitHub - PyGameExamplesAndAnswers - Time, timer event and clock - Time - Until a certain time
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_time_and_timer_event.md
#
# https://replit.com/@Rabbid76/PyGame-MessageDelay#main.py

import pygame

pygame.init()
font = pygame.font.SysFont(None, 50)
text = font.render('press key or mouse', True, (255, 0, 0))

window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()
message_end_time = pygame.time.get_ticks() + 3000

run = True
while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            text = font.render(pygame.key.name(event.key) + ' pressed', True, (255, 0, 0))
            message_end_time = pygame.time.get_ticks() + 2000
        if event.type == pygame.MOUSEBUTTONDOWN:
            text = font.render('button ' + str(event.button) + ' pressed', True, (255, 0, 0))
            message_end_time = pygame.time.get_ticks() + 2000

    window.fill(0)
    if current_time < message_end_time:
        window.blit(text, text.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()