# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# How to create button with transparent background and shadow in pygame?
# https://stackoverflow.com/questions/72352081/how-to-create-button-with-transparent-background-and-shadow-in-pygame/72352967#72352967
#
# GitHub - UI elements - Button
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_ui_elements.md

import pygame

class Button():
    def __init__(self, font, text, rect, inflate, text_color, button_color, hover_color, shadow_color):
        self.rect = pygame.Rect(rect)
        self.button_color = button_color
        self.hover_color = hover_color
        self.shadow_color = shadow_color
        self.inflate = inflate
        self.hover = False
        self.clicked = False
        self.text_surf = font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)

    def draw(self, screen):
        top_rect = self.rect.copy()
        bottom_rect = self.rect.move(self.inflate, self.inflate)
        button_color = self.button_color
        self.hover = top_rect.collidepoint(pygame.mouse.get_pos())
        self.clicked = self.hover and pygame.mouse.get_pressed()[0]
        if self.hover:
            button_color = self.hover_color
        if self.clicked:
            self.clicked = True
            bottom_rect.inflate_ip(self.inflate, self.inflate)
            top_rect.inflate_ip(self.inflate, self.inflate)

        bottom_surf = pygame.Surface(bottom_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(bottom_surf, self.shadow_color, (0, 0, *bottom_rect.size), border_radius = 12)
        screen.blit(bottom_surf, bottom_rect.topleft)
        top_surf = pygame.Surface(top_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(top_surf, button_color, (0, 0, *top_rect.size), border_radius = 12)
        screen.blit(top_surf, top_rect.topleft)
        screen.blit(self.text_surf, self.text_rect)

pygame.init()
window = pygame.display.set_mode((300, 200))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (128, 128, 128), (96, 96, 96)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

font = pygame.font.SysFont(None, 50)
button = Button(font, "Button", (40, 40, 200, 70), 20, (255, 255, 255), (128, 128, 255, 128), (255, 128, 255, 128), (64, 64, 128, 128))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.blit(background, (0, 0))
    button.draw(window)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()