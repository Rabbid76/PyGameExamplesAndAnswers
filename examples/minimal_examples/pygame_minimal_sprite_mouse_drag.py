# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Creating multiple sprites with different update()'s from the same sprite class in Pygame
# https://stackoverflow.com/questions/64419223/creating-multiple-sprites-with-different-updates-from-the-same-sprite-class-i/64456959#64456959
#
# GitHub - Mouse - Mouse Drag
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md
#
# GitHub - Sprite, Group and Sprite mask - Drag Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://repl.it/@Rabbid76/PyGame-MouseDrag#main.py

import pygame

class DragOperator:
    def __init__(self, rect):
        self.rect = rect
        self.dragging = False
        self.rel_pos = (0, 0)
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = self.rect.collidepoint(event.pos)
                self.rel_pos = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            if event.type == pygame.MOUSEMOTION and self.dragging:
                self.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)
        self.drag_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.drag_image, color, (25, 25), 25)
        pygame.draw.circle(self.drag_image, (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.drag = DragOperator(self.rect)
    def update(self, event_list):
        self.drag.update(event_list) 
        self.image = self.drag_image if self.drag.dragging else self.original_image

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

sprite_object = SpriteObject(*window.get_rect().center, (255, 255, 0))
group = pygame.sprite.Group([
    SpriteObject(window.get_width() // 3, window.get_height() // 3, (255, 0, 0)),
    SpriteObject(window.get_width() * 2 // 3, window.get_height() // 3, (0, 255, 0)),
    SpriteObject(window.get_width() // 3, window.get_height() * 2 // 3, (0, 0, 255)),
    SpriteObject(window.get_width() * 2// 3, window.get_height() * 2 // 3, (255, 255, 0)),
])

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    group.update(event_list)

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
