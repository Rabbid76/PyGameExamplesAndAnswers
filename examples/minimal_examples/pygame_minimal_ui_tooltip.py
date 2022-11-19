# How do i make a text box pop up when i hover over a button in pygame
# https://stackoverflow.com/questions/69833827/how-do-i-make-a-text-box-pop-up-when-i-hover-over-a-button-in-pygame/69961155#69961155)
# 
# GitHub - PyGameExamplesAndAnswers - UI elements -  Tool tip
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_ui_elements.md

import pygame
pygame.init()

class Button():
    def __init__(self, x, y, w, h, color, highlight_color, font, text, tip_text, tool_tip):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.highlight_color = highlight_color
        self.image = font.render(text, True, (0, 0, 0))
        self.hover = False
        self.tip_text = tip_text
        self.tool_tip = tool_tip
        
    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)
        if self.hover and self.tool_tip:
            self.tool_tip.set_text(self.tip_text)

    def draw(self, surf):
        color = self.color if self.hover  else self.highlight_color
        pygame.draw.rect(surf, color, self.rect)
        surf.blit(self.image, self.image.get_rect(center = self.rect.center))

class ToolTip():
    def __init__(self, font):
        self.font = font 
        self.tip_text = None
        self.current_text = None
        self.rect = None
        self.image = None

    def set_text(self, tip_text):
        self.tip_text = tip_text

    def update(self, mouse_pos):
        if self.tip_text != self.current_text:
            self.current_text = self.tip_text
            if self.current_text == None:
                self.image = None
                self.rect = None
            else:
                self.image = self.font.render(self.tip_text, True, (0, 0, 0))
                self.rect = self.image.get_rect().inflate(6, 2)
        if self.rect:
            self.rect.topleft = mouse_pos[0]+16, mouse_pos[1]

    def draw(self, surf):
        if self.rect and self.image:
            pygame.draw.rect(surf, (255, 255, 0), self.rect)
            surf.blit(self.image, self.image.get_rect(center = self.rect.center))
                
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
button_font = pygame.font.Font(None, 48)
tip_font = pygame.font.Font(None, 32)
tool_tip = ToolTip(tip_font)
buttons = [
    Button(50, 50, 150, 50, "gray", "lightblue", button_font, "Start", "Start the game", tool_tip),
    Button(50, 120, 150, 50, "gray", "lightblue", button_font, "About", "Show about box", tool_tip),
    Button(50, 190, 150, 50, "gray", "lightblue", button_font, "Exit", "Terminate application", tool_tip)
]

run = True
while run:    
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pos = pygame.mouse.get_pos()
    tool_tip.set_text(None)
    for button in buttons:
        button.update(mouse_pos)
    tool_tip.update(mouse_pos)
  
    window.fill((255, 255, 255))
    for button in buttons:
        button.draw(window)
    tool_tip.draw(window)
    pygame.display.flip()

pygame.quit()
exit()