# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Can I use an image on a moving object within Pygame as opposed to to a color?
# https://stackoverflow.com/questions/65851274/can-i-use-an-image-on-a-moving-object-within-pygame-as-opposed-to-to-a-color/65851431#65851431
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Circular clipping region
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

def create_circular_image(size, image):
    clip_image = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(clip_image, (255, 255, 255), (size//2, size//2), size//2)
    image_rect = my_image.get_rect(center = clip_image.get_rect().center)
    clip_image.blit(my_image, image_rect, special_flags=pygame.BLEND_RGBA_MIN)
    return clip_image

def create_test_image():
    image = pygame.Surface((100, 100))
    ts, w, h, c1, c2 = 25, 100, 100, (255, 64, 64), (32, 64, 255)
    [pygame.draw.rect(image, c1 if (x+y) % 2 == 0 else c2, (x*25, y*ts, ts, ts)) 
        for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
    return image

my_image = create_test_image()
circular_image = create_circular_image(100, my_image)

rect = circular_image.get_rect(center = window.get_rect().center)
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5            

    window.fill((64, 64, 64))
    window.blit(circular_image, rect)
    pygame.display.flip()

pygame.quit()
exit()