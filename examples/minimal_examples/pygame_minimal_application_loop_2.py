# Pygame window freezes when it opens
# https://stackoverflow.com/questions/57642415/pygame-window-freezes-when-it-opens/57644255#57644255
#  
# How to add a background and simple square as a character for a single screen platformer in pygame?
# https://stackoverflow.com/questions/74161044/how-to-add-a-background-and-simple-square-as-a-character-for-a-single-screen-pla/74161707#74161707
#
# GitHub - PyGameExamplesAndAnswers - Event and application loop
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_event_and_application_loop.md

import pygame
pygame.init()

window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
speed = 5

# main application loop
run = True
while run:
    # limit frames per second
    clock.tick(100)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update the game states and positions of objects dependent on the input 
    keys = pygame.key.get_pressed()
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
    border_rect = window.get_rect()
    rect.clamp_ip(border_rect)

    # clear the display and draw background
    window.blit(background, (0, 0))

    # draw the scene   
    pygame.draw.rect(window, (255, 0, 0), rect)

    # update the display
    pygame.display.flip()

pygame.quit()
exit()