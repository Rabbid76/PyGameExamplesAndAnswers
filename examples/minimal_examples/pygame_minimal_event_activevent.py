# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# In pygame for event.type == ACTIVEEVENT, where is the documentation on what the different event.state and event.gain parameters mean?
# https://stackoverflow.com/questions/61488114/in-pygame-for-event-type-activeevent-where-is-the-documentation-on-what-the/73275032#73275032
#
# GitHub - Event and application loop - Event loop - Game state
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_event_and_application_loop.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
pause_text = font.render("pause", True, (255, 255, 0))

pause = False 
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.ACTIVEEVENT:
            print(event.__dict__ )
            if hasattr(event, 'gain'):
                pause = event.gain == 0

    window.fill(0)
    if pause:
        window.blit(pause_text, pause_text.get_rect(center = window.get_rect().center))
    pygame.display.update()

pygame.quit()
exit()