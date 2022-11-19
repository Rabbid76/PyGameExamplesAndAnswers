# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Polygon clipping
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

image = pygame.Surface((200, 200))
ts, w, h, c1, c2 = 20, *image.get_size(), (128, 0, 0), (255, 255, 255)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(image, color, rect) for rect, color in tiles]

mask_image = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.polygon(mask_image, (255, 255, 255, 255), [(0, 50), (100, 50), (100, 0), (200, 100), (100, 200), (100, 150), (0, 150)])
mask_image.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill(0)
    window.blit(mask_image, image.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()