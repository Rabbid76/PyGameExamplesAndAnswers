# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How to blur the edges of a surface in Pygame?
# https://stackoverflow.com/questions/77117250/how-to-blur-the-edges-of-a-surface-in-pygame/77117325#77117325
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Blur
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import pygame
from PIL import Image, ImageFilter

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (32, 32, 32), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

def blur_image(surf, radius):
    pil_string_image = pygame.image.tostring(surf, "RGBA",False)
    pil_image = Image.frombuffer("RGBA", surf.get_size(), pil_string_image)
    pil_blurred = pil_image.filter(ImageFilter.GaussianBlur(radius=radius))
    blurred_image = pygame.image.fromstring(pil_blurred.tobytes(), pil_blurred.size, pil_blurred.mode)
    return blurred_image.convert_alpha()

def blur_image_edges(surf, radius):
    rect = pygame.Rect(0, 0, surf.get_width()+radius*4, surf.get_height()+radius*4)
    blur_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
    blur_surf.blit(surf, surf.get_rect(center = rect.center))
    blurred_image = blur_image(blur_surf, radius)
    return blurred_image

image = pygame.Surface((200, 200))
image.fill('red')
blurred_image = blur_image_edges(image, 20)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.blit(background, (0, 0))
    window.blit(blurred_image, blurred_image.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()