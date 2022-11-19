# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# Displaying unicode symbols using pygame
# https://stackoverflow.com/questions/63398332/displaying-unicode-symbols-using-pygame/63398488#63398488
#
# GitHub - PyGameExamplesAndAnswers - Text and font
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
# 
# Unicodeblock Smileys:                https://de.wikipedia.org/wiki/Unicodeblock_Smileys
# Emoticons (Unicode block):           https://en.wikipedia.org/wiki/Emoticons_(Unicode_block)
# Copy and Paste Emoji:                https://getemoji.com/
# Full Emoji List, v14.0:              https://unicode.org/emoji/charts/full-emoji-list.html
# Chess symbols in Unicode:            https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode
# Chess Symbols to copy and paste:     https://qwerty.dev/chess-symbols-to-copy-and-paste/

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))

seguisy80 = pygame.font.SysFont("segoeuisymbol", 80)
unicode_text = "♔ \u265C 😀 \U0001F603"
text_surface = seguisy80.render(unicode_text, True, "black")

run = True
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill("lightgray")
    window.blit(text_surface, text_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()