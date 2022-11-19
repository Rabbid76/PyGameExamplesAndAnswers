# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How would I make color collision using pygame.mask?
# https://stackoverflow.com/questions/65981815/how-would-i-make-color-collision-using-pygame-mask/65982315#65982315
#
# GitHub - Sprite, Group and Sprite mask - Sprite mask
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SpriteMask

import pygame

def ColorMask(image, mask_color):
    mask_image = image.convert()
    mask_image.set_colorkey(mask_color)
    mask = pygame.mask.from_surface(mask_image)
    mask.invert()
    return mask

pygame.init()
window = pygame.display.set_mode((450, 250))

test_image = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(test_image, (255, 0, 0), (70, 70), 70)
pygame.draw.circle(test_image, (0, 255, 0), (130, 70), 70)
pygame.draw.circle(test_image, (0, 0, 255), (70, 130), 70)
pygame.draw.circle(test_image, (255, 255, 255), (130, 130), 70)

mask = ColorMask(test_image, (255, 0, 0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(test_image, (25, 25))
    window.blit(mask.to_surface(), (250, 25))
    pygame.display.flip()

pygame.quit()
exit()