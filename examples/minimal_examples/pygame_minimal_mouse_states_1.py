# pygame.mouse module
# https://www.pygame.org/docs/ref/mouse.html
#
# Pygame mouse clicking detection
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684
#
# How to distinguish left click, right click mouse clicks in pygame?
# https://stackoverflow.com/questions/34287938/how-to-distinguish-left-click-right-click-mouse-clicks-in-pygame/64625285#64625285
#
# GitHub - Mouse - Mouse and mouse event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md
#
# https://replit.com/@Rabbid76/PyGame-MouseStates

import pygame

pygame.init()
window = pygame.display.set_mode((500, 400))
font40 = pygame.font.SysFont(None, 40)  
clock = pygame.time.Clock()

mouse_button_map = {0 : "left", 1 : "middle", 2 : "right" }
button_name = lambda b : mouse_button_map[b] if b in mouse_button_map else "#" + str(b)

run = True
while run:
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()

    text_pos = "mouse cursor at ({}, {})".format(*mouse_pos)
    text_button = ""
    for i, state in enumerate(mouse_buttons):
        if state:
            text_button += (", " if len(text_button) != 0 else "") + button_name(i)
    text_button += ("no" if len(text_button) == 0 else "") + " button(s) pressed"
    
    window.fill((255, 255, 255))
    window_rect = window.get_rect()
    text_pos_surf = font40.render(text_pos, True, (0, 0, 0))
    window.blit(text_pos_surf, text_pos_surf.get_rect(center = (window_rect.centerx, window_rect.centery-30)))
    text_button_surf = font40.render(text_button, True, (0, 0, 0))
    window.blit(text_button_surf, text_button_surf.get_rect(center = (window_rect.centerx, window_rect.centery+30)))
    pygame.display.update()

pygame.quit()
exit()

