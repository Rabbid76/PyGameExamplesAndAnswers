# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# Pygame mouse clicking detection
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684
#
# GitHub - Mouse - Mouse and mouse event
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md
#
# GitHub - Sprite, Group and Sprite mask - Click Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-MouseClick

import pygame

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)
        self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.click_image, color, (25, 25), 25)
        pygame.draw.circle(self.click_image, (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.clicked = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked 
        
        self.image = self.click_image if self.clicked else self.original_image

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

group = pygame.sprite.Group([
    SpriteObject(window.get_width() // 3, window.get_height() // 3, (128, 0, 0)),
    SpriteObject(window.get_width() * 2 // 3, window.get_height() // 3, (0, 128, 0)),
    SpriteObject(window.get_width() // 3, window.get_height() * 2 // 3, (0, 0, 128)),
    SpriteObject(window.get_width() * 2// 3, window.get_height() * 2 // 3, (128, 128, 0)),
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
