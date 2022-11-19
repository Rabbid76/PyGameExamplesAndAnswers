# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# pygame.sprite module
# https://www.pygame.org/docs/ref/sprite.html
#
# How to create a text input box with pygame?
# https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame/64613666#64613666
#
# How to allow the user to type only under certain conditions in pygame?
# https://stackoverflow.com/questions/64254687/how-to-allow-the-user-to-type-only-under-certain-conditions-in-pygame  
#
# GitHub - PyGameExamplesAndAnswers - Text and font
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# GitHub - Sprite, Group and Sprite mask - Text input
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md
#
# https://replit.com/@Rabbid76/PyGame-SpriteTextInput

import pygame

class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()

pygame.init()
window = pygame.display.set_mode((500, 160))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 80)

text_input_box = TextInputBox(50, 50, 400, font)
group = pygame.sprite.Group(text_input_box)

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
