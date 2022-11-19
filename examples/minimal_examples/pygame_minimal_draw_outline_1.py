# pygame.draw module
# https://www.pygame.org/docs/ref/draw.html
#  
# Adding an outline around a snake in snake game
# https://stackoverflow.com/questions/73516121/adding-an-outline-around-a-snake-in-snake-game/73517037#73517037
#
# GitHub - PyGameExamplesAndAnswers - Shape and contour - Outline
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_draw_shape_and_contour.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def drawOutline(surf, rectangles, color, width):
    for r in rectangles:
        corners = [
            (r.left, r.top), (r.right-width, r.top), 
            (r.left, r.bottom-width), (r.right-width, r.bottom-width),
        ]
        for c in corners:
            pygame.draw.rect(surf, color, (*c, width, width))

    for i, r in enumerate(rectangles):
        neighbours = rectangles[i-1:i] + rectangles[i+1:i+2]
        sides = [
            (r.move(-1,  0), (r.left, r.top+width, width, r.height-2*width)),
            (r.move( 1,  0), (r.right-width, r.top+width, width, r.height-2*width)),
            (r.move( 0, -1), (r.left+width, r.top, r.width-2*width, width)),
            (r.move( 0,  1), (r.left+width, r.bottom-width, r.width-2*width, width)),
        ]
        for test_rect, line in sides:
            if test_rect.collidelist(neighbours) < 0:
                pygame.draw.rect(surf, color, line)

body = [
   pygame.Rect(50, 100, 50, 50),
   pygame.Rect(100, 100, 50, 50),
   pygame.Rect(150, 100, 50, 50),
   pygame.Rect(200, 100, 50, 50),
   pygame.Rect(200, 150, 50, 50),
   pygame.Rect(150, 150, 50, 50),
   pygame.Rect(100, 150, 50, 50),
   pygame.Rect(100, 200, 50, 50),
   pygame.Rect(100, 250, 50, 50),
   pygame.Rect(150, 250, 50, 50),
   pygame.Rect(200, 250, 50, 50),
   pygame.Rect(250, 250, 50, 50),
]

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill(0)
    drawOutline(window, body, "yellow", 3)
    pygame.display.flip()

pygame.quit()
exit()
