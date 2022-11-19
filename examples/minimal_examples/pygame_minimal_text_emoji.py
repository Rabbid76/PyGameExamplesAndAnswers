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
#
# https://freetype-py.readthedocs.io/en/latest/
# use https://www.lfd.uci.edu/~gohlke/pythonlibs/#freetypepy
# # https://github.com/samuelngs/apple-emoji-linux
# https://github.com/rougier/freetype-py/blob/master/examples/emoji-color-cairo.py

import os
if os.path.exists("G:/My Drive/source/font/"):
    os.chdir("G:/My Drive/source/font/")

import freetype
import numpy as np
import pygame
import pygame.freetype

class EmojisMonochrom:
    def __init__(self):
        self. face = freetype.Face(r"C:/Windows/Fonts/seguiemj.ttf")
        self.face.set_char_size(64*64)  

    def create_surface(self, unicode):
        self.face.load_char(unicode)
        ft_bitmap = self.face.glyph.bitmap
        bitmap_array = np.array(ft_bitmap.buffer, dtype=np.uint8).reshape((ft_bitmap.rows, ft_bitmap.width))
        bitmap_array = np.repeat(bitmap_array.reshape(ft_bitmap.rows, ft_bitmap.width, 1), 4, axis = 2)
        return pygame.image.frombuffer(bitmap_array.flatten(), (ft_bitmap.width, ft_bitmap.rows), 'RGBA') 

class Emojis:
    def __init__(self):
        self. face = freetype.Face("AppleColorEmoji.ttf")
        self.face.set_char_size(int(self.face.available_sizes[-1].size)) 

    def create_surface(self, unicode):
        self.face.load_char(unicode, freetype.FT_LOAD_COLOR)
        ft_bitmap = self.face.glyph.bitmap
        bitmap = np.array(ft_bitmap.buffer, dtype=np.uint8).reshape((ft_bitmap.rows, ft_bitmap.width, 4))
        bitmap[:, :, [0, 2]] = bitmap[:, :, [2, 0]]
        return pygame.image.frombuffer(bitmap.flatten(), (ft_bitmap.width, ft_bitmap.rows), 'RGBA')

pygame.init()
window = pygame.display.set_mode((500, 300))
seguisy80 = pygame.freetype.SysFont("segoeuisymbol", 128)
emojis_monochrom = EmojisMonochrom()
emojis = Emojis()

monochrom_emoji_1, _ =  seguisy80.render('😃', "black")   
monochrom_emoji_2 = emojis_monochrom.create_surface('😃')
color_emoji = emojis.create_surface('😃')
#color_emoji = emojis.create_surface('\U0001F603')

run = True
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill("gray")
    window.blit(monochrom_emoji_1, monochrom_emoji_1.get_rect(center = (100, 150)))
    window.blit(monochrom_emoji_2, monochrom_emoji_2.get_rect(center = (250, 150)))
    window.blit(color_emoji, color_emoji.get_rect(center = (400, 150)))
    pygame.display.flip()

pygame.quit()
exit()
