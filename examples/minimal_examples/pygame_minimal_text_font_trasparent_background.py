# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# How to separately change the opacity of a text on a button pygame?
# https://stackoverflow.com/questions/68128389/how-to-separately-change-the-opacity-of-a-text-on-a-button-pygame/68128949#68128949
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Transparent text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# https://replit.com/@Rabbid76/PyGame-TextTransparentBackground#main.py


import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

font = pygame.font.SysFont(None, 80)
text = font.render("Button", True, (255, 255, 255))

button = pygame.Surface((320, 120), pygame.SRCALPHA)
button.fill((255, 255, 255))
button.fill((196, 127, 127, 127), button.get_rect().inflate(-4, -4))
button.blit(text, text.get_rect(center = button.get_rect().center))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.blit(background, (0, 0))
    window.blit(button, button.get_rect(center = window.get_rect().center))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()