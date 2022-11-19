# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Changing colour of a surface without overwriting transparency
# https://stackoverflow.com/questions/64190277/changing-colour-of-a-surface-without-overwriting-transparency/64193109#64193109
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Change color of an image - Tint a grayscale image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md
#
# GitHub - Sprite, Group and Sprite mask - Sprite on mouse hover
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-ChangeColorOfSpriteArea

import pygame

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.Surface((150, 150))
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (150, 150))

    def set_colour(self, colour_value):
        self.colour = colour_value
        self.original_image.fill(self.colour)

        whiteTransparent = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        whiteTransparent.fill((255, 255, 255, 0))
        self.image.blit(whiteTransparent, (0, 0), special_flags = pygame.BLEND_MAX)

        self.image.blit(self.original_image, (0, 0), special_flags = pygame.BLEND_MULT)

    def set_outline(self, thickness):
        self.thickness = thickness
        size = self.image.get_size()

        calc = thickness/100
        p_width, p_height = size[0], size[1]
        width, height = size[0]*calc, size[1]*calc

        self.image = self.image.convert_alpha()

        center_x, center_y = (p_width//2)-(width//2), (p_height//2)-(height//2)
        pygame.draw.rect(self.image, (0, 0, 0, 0), (center_x, center_y, width, height))

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

sprite = Rectangle()
sprite.set_colour((255, 0, 0, 255))
sprite.set_outline(50)

group = pygame.sprite.Group(sprite)

colorVal = 0
colorAdd = 5
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    sprite.set_colour((min(colorVal, 255), max(0, min(511-colorVal, 255)), 0, 255))
    colorVal += colorAdd
    if colorVal <= 0 or colorVal >= 511:
        colorAdd *= -1

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()