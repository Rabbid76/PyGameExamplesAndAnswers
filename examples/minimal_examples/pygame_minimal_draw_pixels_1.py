# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Pygame: Draw single pixel
# https://stackoverflow.com/questions/10354638/pygame-draw-single-pixel/64571453#64571453
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md
#
# https://replit.com/@Rabbid76/PyGame-DrawPixel-1

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
clock.tick()
count = 0
dt_list = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size())//2]*2))
    
    for x in range(rect.width):
        u = x / (rect.width - 1)
        color = (round(u*255), 0, round((1-u)*255))
        for y in range(rect.height):
            window.set_at((rect.left + x, rect.top + y), color) 
    """
    for x in range(rect.width):
        for y in range(rect.height):
            u = x / (rect.width - 1)
            v = y / (rect.height - 1)
            color = (round(u*255), round(v*255), round((1-u)*(1-v)*255))
            window.set_at((rect.left + x, rect.top + y), color) 
    """

    pygame.display.flip()
   
    dt_list += [clock.tick()]
    if len(dt_list) > 100:
        del dt_list[0]
    if (count % 100 == 0):
        dt_sum = sum(dt_list)
        if dt_sum > 0:
           pygame.display.set_caption("FPS: " + str(round(len(dt_list) / sum(dt_list) * 1000)))
    count += 1

pygame.quit()
exit()