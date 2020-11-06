# pygame.mouse module
# https://www.pygame.org/docs/ref/mouse.html
#
# Image lagging while blitting on top of mouse rect
# https://stackoverflow.com/questions/56961186/image-lagging-while-blitting-on-top-of-mouse-rect/56976454#56976454
#
# GitHub - Mouse - Mouse cursor
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md

import os
import pygame
import win32api, win32gui, win32con
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()
window = pygame.display.set_mode((640, 480))

#cursor = win32api.LoadCursor(0, win32con.IDC_HELP)
cursor = win32gui.LoadImage(0, 'cursor/aero_arrow_xl.cur', win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE)
#cursor = win32gui.LoadImage(0, 'icon/ball64.ico', win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)

pygame.mouse.set_visible(False)

run = True
while run:
    pygame.time.Clock().tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win32api.SetCursor(cursor)
    pygame.display.update()

pygame.quit()
exit()

