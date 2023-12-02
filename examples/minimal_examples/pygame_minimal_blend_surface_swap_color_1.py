# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# [How do I palette swap sprites in pygame without the rectangle in the back
# https://stackoverflow.com/questions/77590955/how-do-i-palette-swap-sprites-in-pygame-without-the-rectangle-in-the-back/77591351#77591351
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Change color of an image - Tint a grayscale image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md

import pygame

pygame.init()
window = pygame.display.set_mode((350, 200))
clock = pygame.time.Clock()

def palette_swap(surf, old_c, new_c):
    color_mask = pygame.mask.from_threshold(image, old_c, threshold=(1, 1, 1, 255))
    color_change_surf = color_mask.to_surface(setcolor=new_c, unsetcolor=(0, 0, 0, 0))
    img_copy = surf.copy()
    img_copy.blit(color_change_surf, (0, 0))
    return img_copy

image = pygame.Surface((100, 100), pygame.SRCALPHA)
#image.fill((0, 255, 0))
#image.set_colorkey((0, 255, 0))
pygame.draw.circle(image, "black", (50, 50), 50)
pygame.draw.circle(image, (255, 148, 66), (50, 50), 40)
pygame.draw.circle(image, "black", (30, 35), 10)
pygame.draw.circle(image, "black", (70, 35), 10)

new_iamge = palette_swap(image, (255, 148, 66), (249, 4, 99))

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    window.fill("gray")
    window.blit(image, image.get_rect(center = (100, 100)))
    window.blit(new_iamge, new_iamge.get_rect(center = (250, 100)))
    pygame.display.flip()

pygame.quit()
exit()