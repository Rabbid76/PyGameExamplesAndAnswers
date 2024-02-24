# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# pygame. How to render the text like a all_sprites.update() but all_texts.update()?
# https://stackoverflow.com/questions/74158381/pygame-how-to-render-the-text-like-a-all-sprites-update-but-all-texts-update/74158474#74158474
#
# GitHub - Sprite, Group and Sprite mask - Sprite
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)

class Text(pygame.sprite.Sprite):
    def __init__(self, font, text, color, center_pos):
        super().__init__() 
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect(center = center_pos)

all_text = pygame.sprite.Group()
all_text.add(Text(font, "Hello", "white", (200, 150)))
all_text.add(Text(font, "World!", "white", (200, 250)))

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window.fill('black')
    all_text.draw(window)
    pygame.display.flip()

pygame.quit()
exit()