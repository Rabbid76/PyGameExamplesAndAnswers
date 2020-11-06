# pygame.mouse module
# https://www.pygame.org/docs/ref/mouse.html
#
# Pygame mouse clicking detection
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684
#
# How to distinguish left click , right click mouse clicks in pygame?
# https://stackoverflow.com/questions/34287938/how-to-distinguish-left-click-right-click-mouse-clicks-in-pygame
#
# GitHub - Mouse - Mouse and mouse event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md

import pygame

pygame.init()
window = pygame.display.set_mode((800, 200))
font40 = pygame.font.SysFont(None, 40)  
clock = pygame.time.Clock()

mouse_buttons = {1 : "left", 2 : "middle", 3 : "right" }
button_name = lambda b : mouse_buttons[b] if b in mouse_buttons else "#" + str(b)
text = "Wait for event ..."

run = True
while run:
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            text = '{} MOUSEBUTTONDOWN at ({}, {})'.format(button_name(event.button), *event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            text = '{} MOUSEBUTTONUP at ({}, {})'.format(button_name(event.button), *event.pos)
    
    window.fill((255, 255, 255))
    text_surf = font40.render(text, True, (0, 0, 0))
    window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
    pygame.display.update()

pygame.quit()
exit()

