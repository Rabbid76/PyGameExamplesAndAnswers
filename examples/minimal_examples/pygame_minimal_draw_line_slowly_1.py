# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# How to slowly draw a line in Python
# https://stackoverflow.com/questions/57618029/how-to-slowly-draw-a-line-in-python/57621742#57621742

# Slowly drawing a line in pygame while other lines remain static
# https://stackoverflow.com/questions/57630853/slowly-drawing-a-line-in-pygame-while-other-lines-remain-static/57631750#57631750
#
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Draw lines and polygons
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame

pygame.init()
window = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

line_start = [(100, 0),   (200, 0),   (0, 100),   (0, 200)]
line_end   = [(100, 300), (200, 300), (300, 100), (300, 200)]

def draw_red_line(surf, color, start, end, w):
    xe = start[0] * (1-w) + end[0] * w
    ye = start[1] * (1-w) + end[1] * w
    pygame.draw.line(surf, color, start, (round(xe), round(ye)))

count=0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    for i in range(int(count)):
        draw_red_line(window, (255, 255, 255), line_start[i], line_end[i], 1)
    if count < 4:
        i = int(count)
        draw_red_line(window, (255, 0, 0), line_start[i], line_end[i], count-i)
        count += 0.01
    else:
        count = 0
        
    pygame.display.flip()

pygame.quit()
exit()
