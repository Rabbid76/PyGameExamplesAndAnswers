# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Text with a Drop-shadow
# https://stackoverflow.com/questions/52960057/pygame-text-with-a-drop-shadow/73927438#73927438
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Transparent text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md


import pygame

def renderTextDropShadow(font, text, color, dx, dy, shadowColor=(127, 127, 127), shadowAlpha = 127):
    textSize = font.size(text)
    surf = pygame.Surface((textSize[0] + abs(dx), textSize[1] + abs(dy)), pygame.SRCALPHA)
    shadowSurf = font.render(text, True, shadowColor)
    shadowSurf.set_alpha(shadowAlpha)
    textSurf = font.render(text, True, color)
    surf.blit(shadowSurf, (max(0, dx), max(0, dy)))
    surf.blit(textSurf, (max(0, -dx), max(0, -dy)))
    return surf

pygame.init()
window = pygame.display.set_mode((700, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 150)

textSurf = renderTextDropShadow(font, 'Hello World!', (0, 0, 0), -15, 10)

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (255, 255, 255), (255, 164, 196)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    window.blit(textSurf, textSurf.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()