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
# GitHub - Sprite, Group and Sprite mask - Sprite on mouse hover
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-MouseHover

import pygame

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)
        self.hover_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.hover_image, color, (25, 25), 25)
        pygame.draw.circle(self.hover_image, (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.hover = False

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        #self.hover = self.rect.collidepoint(mouse_pos) 
        self.hover = self.rect.collidepoint(mouse_pos) and any(mouse_buttons)
               
        self.image = self.hover_image if self.hover else self.original_image

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

sprite_object = SpriteObject(*window.get_rect().center, (128, 128, 0))
group = pygame.sprite.Group([
    SpriteObject(window.get_width() // 3, window.get_height() // 3, (128, 0, 0)),
    SpriteObject(window.get_width() * 2 // 3, window.get_height() // 3, (0, 128, 0)),
    SpriteObject(window.get_width() // 3, window.get_height() * 2 // 3, (0, 0, 128)),
    SpriteObject(window.get_width() * 2// 3, window.get_height() * 2 // 3, (128, 128, 0)),
])

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
