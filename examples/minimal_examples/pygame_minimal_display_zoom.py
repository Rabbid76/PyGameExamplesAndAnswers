# pygame.display module
# https://www.pygame.org/docs/ref/display.html

# Zooming in and out of a PyGame window with all objects still in place
# https://stackoverflow.com/questions/64936805/zooming-in-and-out-of-a-pygame-window-with-all-objects-still-in-place/64937795#64937795
#
# GitHub - PyGameExamplesAndAnswers - Display, display position and Resize - Scale and zoom window
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_display_resize_and_scroll.md
#
# https://replit.com/@Rabbid76/PyGame-ZoomInAndOut

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

window = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
map =  pygame.image.load('image/parrot1.png')
maprect = map.get_rect(center = window.get_rect().center)
mapsurface = map

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.dict['size'], pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
            mapsurface = pygame.transform.smoothscale(map, maprect.size)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 or event.button == 5:
                zoom = 2 if event.button == 4 else 0.5
                mx, my = event.pos
                left   = mx + (maprect.left - mx) * zoom
                right  = mx + (maprect.right - mx) * zoom
                top    = my + (maprect.top - my) * zoom
                bottom = my + (maprect.bottom - my) * zoom
                maprect = pygame.Rect(left, top, right-left, bottom-top)
                mapsurface = pygame.transform.smoothscale(map, maprect.size)
                
    window.fill(0)
    window.blit(mapsurface, maprect)
    pygame.display.flip()

pygame.quit()
exit()
