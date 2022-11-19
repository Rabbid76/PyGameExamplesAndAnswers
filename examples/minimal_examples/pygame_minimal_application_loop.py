# Pygame window freezes when it opens
# https://stackoverflow.com/questions/57642415/pygame-window-freezes-when-it-opens/57644255#57644255
#  
# Pygame unresponsive display
# https://stackoverflow.com/questions/63540062/pygame-unresponsive-display/63540113#63540113
#   
# Pygame window not responding after a few seconds
# https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds/61409221#61409221
# 
# GitHub - PyGameExamplesAndAnswers - Event and application loop
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_event_and_application_loop.md
#
# https://replit.com/@Rabbid76/PyGame-MinimalApplicationLoop

import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# main application loop
run = True
while run:

    # limit frames per second
    clock.tick(60)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # clear the display
    window.fill(0)

    # draw the scene   
    pygame.draw.circle(window, (255, 0, 0), (250, 250), 100)

    # update the display
    pygame.display.flip()

pygame.quit()
exit()