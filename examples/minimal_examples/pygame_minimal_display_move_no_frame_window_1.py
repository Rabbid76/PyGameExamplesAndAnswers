# pygame.display module
# https://www.pygame.org/docs/ref/display.html
#
# How to move a no frame pygame windows when user click on it?
# https://stackoverflow.com/questions/57674156/how-to-move-a-no-frame-pygame-windows-when-user-click-on-it/57681853#57681853
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Set position
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md

# duplicate
# Pygame, Resize and Move window with no frame?
# https://stackoverflow.com/questions/70233847/pygame-resize-and-move-window-with-no-frame/70234971#70234971v

import pygame
from ctypes import windll

pygame.init()
screen = pygame.display.set_mode((400, 400), pygame.NOFRAME)
clock = pygame.time.Clock()

def moveWin(new_x, new_y):
    hwnd = pygame.display.get_wm_info()['window']
    w, h = pygame.display.get_surface().get_size()
    windll.user32.MoveWindow(hwnd, new_x, new_y, w, h, False)

window_pos = [100, 100]
moveWin(*window_pos)

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                print (event.rel)
                window_pos[0] += event.rel[0]
                window_pos[1] += event.rel[1]
                moveWin(*window_pos)
    
    screen.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(60)

"""
window_pos = [100, 100]
moveWin(*window_pos)
drag_start_pos = None

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drag_start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drag_start_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if drag_start_pos:
                new_mouse_pos = pygame.mouse.get_pos()
                window_pos[0] += new_mouse_pos[0] - drag_start_pos[0]
                window_pos[1] += new_mouse_pos[1] - drag_start_pos[1]
                drag_start_pos = new_mouse_pos
                moveWin(*window_pos)

    screen.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(60)
"""   
