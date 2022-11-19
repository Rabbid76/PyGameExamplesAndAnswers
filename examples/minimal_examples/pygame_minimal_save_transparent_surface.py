# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# pygame, saving a image with low opacity
# https://stackoverflow.com/questions/73802557/pygame-saving-a-image-with-low-opacity/73802685#73802685
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Transformation - Store Image (Save image)
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

the_img = pygame.Surface((200, 200))
pygame.draw.circle(the_img, (255, 0, 0), (100, 100), 100)
the_img.set_alpha(127)

the_img.set_colorkey((0, 0, 0))
the_img_alpha = pygame.Surface(the_img.get_size(), pygame.SRCALPHA)
the_img_alpha.blit(the_img, (0, 0))
pygame.image.save(the_img_alpha, "c:/temp/test.png")

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window_center = window.get_rect().center

    window.fill((127, 127, 127))
    window.blit(the_img, the_img.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()
