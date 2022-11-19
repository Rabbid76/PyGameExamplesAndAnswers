# pygame.joystick module
# https://www.pygame.org/docs/ref/joystick.html
#
# How do I get xbox controls outside event loop in pygame?
# https://stackoverflow.com/questions/73502525/how-do-i-get-xbox-controls-outside-event-loop-in-pygame/73502685#73502685
#
# GitHub - PyGameExamplesAndAnswers - Joystick
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_joystick.md

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
vel = 5
color = (255, 0, 0)

joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("joystick initialized")

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    if joystick:
        button = joystick.get_button(0)
        rect.x += round(joystick.get_axis(0) * vel)
        rect.y += round(joystick.get_axis(1) * vel)
        if joystick.get_button(0):
            color = (0, 255, 0)
        elif joystick.get_button(1):
            color = (255, 0, 0)
        elif joystick.get_button(2):
            color = (0, 0, 255)
        elif joystick.get_button(3):
            color = (255, 255, 0)

    keys = pygame.key.get_pressed()
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        
    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    window.fill(0)
    pygame.draw.rect(window, color, rect)
    pygame.display.flip()

pygame.quit()
exit()