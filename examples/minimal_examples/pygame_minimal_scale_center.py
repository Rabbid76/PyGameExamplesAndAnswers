# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# How do I scale a PyGame image (Surface) with respect to its center?
# https://stackoverflow.com/questions/59919826/how-do-i-scale-a-pygame-image-surface-with-respect-to-its-center/59919909#59919909
#
# How to change an image size in Pygame?
# https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame/66611330#66611330 
#
# GitHub - PyGameExamplesAndAnswers - Scale and zoom - Transform scale and zoom surface
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_scale_and_zoom.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class ScaleSprite(pygame.sprite.Sprite):
    def __init__(self, center, image):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center = center)
        self.mode = 1
        self.grow = 0

    def update(self):
        if self.grow > 100:
            self.mode = -1
        if self.grow < 1:
            self.mode = 1
        self.grow += 1 * self.mode 

        orig_x, orig_y = self.original_image.get_size()
        size_x = orig_x + round(self.grow)
        size_y = orig_y + round(self.grow)
        self.image = pygame.transform.scale(self.original_image, (size_x, size_y))
        self.rect = self.image.get_rect(center = self.rect.center)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

sprite = ScaleSprite(window.get_rect().center, pygame.image.load("icon/Banana64.png"))
group = pygame.sprite.Group(sprite)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    group.update()

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()