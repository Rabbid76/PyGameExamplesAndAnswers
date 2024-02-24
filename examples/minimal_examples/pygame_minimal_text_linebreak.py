# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Pygame lagging with texts
# https://stackoverflow.com/questions/72425832/pygame-lagging-with-texts/72497655#72497655
#
# GitHub - PyGameExamplesAndAnswers - Text and font - Text
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def renderText(font, color, textList):
    fontHeihgt = font.get_height()
    textSurfaceList = [font.render(t, True, color) for t in textList]
    width = max([s.get_width() for s in textSurfaceList])
    height = len(textSurfaceList) * fontHeihgt
    textSurface = pygame.Surface((width, height), pygame.SRCALPHA)
    [textSurface.blit(s, (0, fontHeihgt*i)) for i, s in enumerate(textSurfaceList)]
    return textSurface

font = pygame.font.SysFont(None, 50)
text = renderText(font, (255, 255, 0), ["This is a", "multi-line text.", ";-)"])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window_center = window.get_rect().center
    window.fill('black')
    window.blit(text, text.get_rect(center = window_center))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()