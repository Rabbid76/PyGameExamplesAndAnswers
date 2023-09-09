# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How do I rotate an image around its center using PyGame?
# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
#
# GitHub - Sprite, Group and Sprite mask - Rotate Sprite - Follow mouse
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SpriteRotateToMouse

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (x, y))
        self.angle = 0
    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.angle = (self.angle + 1) % 360

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

surface = pygame.Surface((100, 50), pygame.SRCALPHA)
surface.fill("black")
player = Player(surface, *window.get_rect().center)
all_sprites = pygame.sprite.Group(player)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()

    window.fill((255, 255, 255))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()