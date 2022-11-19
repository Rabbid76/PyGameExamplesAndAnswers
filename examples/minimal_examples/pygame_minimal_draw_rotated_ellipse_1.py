# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# drawing a diagonal ellipse with pygame
# https://stackoverflow.com/questions/23281952/drawing-a-diagonal-ellipse-with-pygame/65774382#65774382
#
# How to draw a rotated ellipse using Pygame?
# https://stackoverflow.com/questions/65767785/how-to-draw-a-rotated-ellipse-using-pygame/65769408#65769408
# 
# GitHub - PyGameExamplesAndAnswers - Shape and contour
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md
#
# https://replit.com/@Rabbid76/PyGame-TransparentShapes

import pygame

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

pygame.init()
window = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (160, 160, 160), (192, 192, 192)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

angle = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    draw_ellipse_angle(window, (0, 0, 255), (25, 75, 200, 100), angle, 5)
    angle += 1
    pygame.display.flip()

pygame.quit()
exit()