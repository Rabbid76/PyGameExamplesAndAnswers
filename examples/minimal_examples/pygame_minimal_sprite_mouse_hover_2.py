# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How can I add an image or icon to a button rectangle in Pygame?
# https://stackoverflow.com/questions/64990710/how-can-i-add-an-image-or-icon-to-a-button-rectangle-in-pygame/64990819#64990819
#
# GitHub - Mouse - Mouse and mouse event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md
#
# GitHub - Sprite, Group and Sprite mask - Click Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__() 
        img = pygame.image.load(filename).convert_alpha()
        self.original_image = pygame.Surface((70, 70))
        self.original_image.blit(img, img.get_rect(center = self.original_image.fill((127, 127, 127)).center))
        self.hover_image = pygame.Surface((70, 70))
        self.hover_image.blit(img, img.get_rect(center = self.hover_image.fill((228, 228, 228)).center))
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.hover = False

    def update(self):
        self.hover = self.rect.collidepoint(pygame.mouse.get_pos())
        self.image = self.hover_image if self.hover else self.original_image

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

group = pygame.sprite.Group([
    SpriteObject(window.get_width() // 3, window.get_height() // 3, 'icon/Apple64.png'),
    SpriteObject(window.get_width() * 2 // 3, window.get_height() // 3, 'icon/Banana64.png'),
    SpriteObject(window.get_width() // 3, window.get_height() * 2 // 3, 'icon/Pear64.png'),
    SpriteObject(window.get_width() * 2// 3, window.get_height() * 2 // 3, 'icon/Plums64.png'),
])

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    group.update()

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
