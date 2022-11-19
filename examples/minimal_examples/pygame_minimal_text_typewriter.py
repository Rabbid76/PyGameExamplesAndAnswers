# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Typewriter Effect Pygame
# https://stackoverflow.com/questions/41101662/typewriter-effect-pygame/70235527#70235527 
#
# Pygame Rendering Text 1 by 1 Causes Lag In Game How Do I Fix This?
# https://stackoverflow.com/questions/67273848/pygame-rendering-text-1-by-1-causes-lag-in-game-how-do-i-fix-this/67273892#67273892
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# https://replit.com/@Rabbid76/PyGame-Typewriter#main.py

import pygame

pygame.init()
window = pygame.display.set_mode((500, 150))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (32, 32, 32), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

text = 'Hello World'
text_len = 0
typewriter_event = pygame.USEREVENT+1
pygame.time.set_timer(typewriter_event, 100)
text_surf = None

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == typewriter_event:
            text_len += 1
            if text_len > len(text):
                text_len = 0
            text_surf = None if text_len == 0 else font.render(text[:text_len], True, (255, 255, 128))

    window.blit(background, (0, 0))
    if text_surf:
        window.blit(text_surf, text_surf.get_rect(midleft = window.get_rect().midleft).move(40, 0))
    pygame.display.flip()

pygame.quit()
exit()