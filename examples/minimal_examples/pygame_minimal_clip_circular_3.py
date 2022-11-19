# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How do I focus light or how do I only draw certain circular parts of the window in pygame?
# https://stackoverflow.com/questions/61657481/how-do-i-focus-light-or-how-do-i-only-draw-certain-circular-parts-of-the-window/61658124#61658124
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Circular clipping region
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md
#
# https://replit.com/@Rabbid76/PyGame-ClipCircularRegion-3

import pygame
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

cover_surf = pygame.Surface((400, 400))
cover_surf.set_colorkey((255, 255, 255))

px = [100, 200, 300]
dx = [1, 2, 3] 

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # create cover surface 
    cover_surf.fill(0)
    for i in range(3):
        radius = 40 + i*20
        pygame.draw.circle(cover_surf, (255, 255, 255), (px[i], 100+(i*100)), radius)
        px[i] += dx[i]
        if px[i] < radius or px[i] > 400 - radius:
            dx[i] = -dx[i]

    # draw the scene
    ts, w, h, c1, c2 = 50, *window.get_size(), (255, 255, 255), (255, 0, 0)
    tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
    for rect, color in tiles:
        pygame.draw.rect(window, color, rect)

    # draw transparent circle and update display
    window.blit(cover_surf, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()