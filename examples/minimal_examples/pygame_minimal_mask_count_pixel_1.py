# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# Get the average Color of a Surface ignoring transparent pixels
# https://stackoverflow.com/questions/69876220/get-the-average-color-of-a-surface-ignoring-transparent-pixels/70056421#70056421)  v
#
# GitHub - Mask - Mask count pixel
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mask.mdightObject

import pygame

def get_averqge_color(surf):
    color = pygame.transform.average_color(surf, surf.get_rect())
    pxiel_count = pygame.mask.from_surface(surf).count()
    scale = surf.get_width() * surf.get_height() / pxiel_count
    print(color, scale, pxiel_count)
    return (round(color[0]*scale), round(color[1]*scale), round(color[2]*scale))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 70)

test_surface = pygame.Surface((300, 300))
test_surface.set_colorkey((0, 0, 0))
pygame.draw.rect(test_surface, (255, 0, 0), (50, 50, 100, 100))
pygame.draw.rect(test_surface, (0, 255, 0), (150, 50, 100, 100))
pygame.draw.rect(test_surface, (255, 255, 0), (50, 150, 100, 100))
pygame.draw.rect(test_surface, (0, 0, 255), (150, 150, 100, 100))

avg_color = get_averqge_color(test_surface)
color_text = font.render(f"{avg_color[0]} {avg_color[1]} {avg_color[2]}", True, "black")

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 80, *window.get_size(), (160, 160, 160), (96, 96, 96)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.blit(background, (0, 0))
    rect = test_surface.get_rect(center = window.get_rect().center)
    window.blit(test_surface, rect)
    pygame.draw.rect(window, "black", rect, 5, 5)
    window.blit(color_text, color_text.get_rect(center = rect.center))
    pygame.display.flip()

pygame.quit()
exit()