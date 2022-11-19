# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How to free transform image in pygame?
# https://stackoverflow.com/questions/69271298/how-to-free-transform-image-in-pygame/69272398#69272398
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Clipping with masks
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md

import pygame

def clip_surface(surf, mask):
    return mask.to_surface(setsurface = surf.convert_alpha(), unsetcolor = (0, 0, 0, 0))

def checker_image(ts, w, h, c1, c2):
    surf = pygame.Surface((w, h))
    [pygame.draw.rect(surf, c1 if (x+y) % 2 == 0 else c2, (x*ts, y*ts, ts, ts)) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
    return surf

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

background = checker_image(40, *window.get_size(), (129, 128, 128), (96, 96, 96))
image = checker_image(20, 200, 200, (255, 128, 128), (255, 64, 64))
mask_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
pygame.draw.polygon(mask_image, (255, 255, 255), [(100, 10), (10, 190), (190, 190)])
mask = pygame.mask.from_surface(mask_image)

clipped_image = clip_surface(image, mask)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.blit(background, (0, 0))
    image_rect = clipped_image.get_rect(center = window.get_rect().center)
    pygame.draw.rect(window, (0, 0, 0), image_rect, 3)
    window.blit(clipped_image, image_rect)
    pygame.display.flip()

pygame.quit()
exit()