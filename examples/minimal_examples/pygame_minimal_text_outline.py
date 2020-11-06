# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Have an outline of text in Pygame
# https://stackoverflow.com/questions/60987711/have-an-outline-of-text-in-pygame
#
# GitHub - PyGameExamplesAndAnswers - Text and font
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md

import pygame
import pygame.font

pygame.init()
font = pygame.font.SysFont(None, 40)
font.set_bold(True)

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
textRect = pygame.Rect(0, 0, 0, 0)

def text_speech(font, text : str, color, x, y, bold : bool, outline: int):
    global textRect 
    
    if outline > 0:
        outlineSurf = font.render(text, True, (255, 0, 0))
        outlineSize = outlineSurf.get_size()
        textSurf = pygame.Surface((outlineSize[0] + outline*2, outlineSize[1] + 2*outline))
        textRect = textSurf.get_rect()
        offsets = [(ox, oy) 
            for ox in range(-outline, 2*outline, outline)
            for oy in range(-outline, 2*outline, outline)
            if ox != 0 or ox != 0]
        for ox, oy in offsets:   
            px, py = textRect.center
            textSurf.blit(outlineSurf, outlineSurf.get_rect(center = (px+ox, py+oy))) 
        innerText = font.render(text, True, color).convert_alpha()
        textSurf.blit(innerText, innerText.get_rect(center = textRect.center)) 
    else:
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()    
    
    textRect.center = (x,y)
    screen.blit(textSurf, textRect)

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    hover = textRect.collidepoint(pygame.mouse.get_pos())
    outlineSize = 3 if hover else 0 

    screen.fill((0,0,0))
    text_speech(font, 'Hello', (255,255,255), (width/2), (height/2), False, outlineSize)
    pygame.display.flip()

pygame.quit()
exit()