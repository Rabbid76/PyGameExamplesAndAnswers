# Spritesheet
# https://www.pygame.org/wiki/Spritesheet)
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How do I create animated sprites using Sprite Sheets in Pygame?
# https://stackoverflow.com/questions/55200501/how-do-i-create-animated-sprites-using-sprite-sheets-in-pygame/55200625#55200625
#
# Invalid destination position for blit error, not seeing how
# https://stackoverflow.com/questions/55199591/invalid-destination-position-for-blit-error-not-seeing-how/55199736#55199736
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load Sprite Sheet
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class SpriteSheet:
    def __init__(self, filename, px, py, tw, th, m, tiles, color_key = None):
        self.sheet = pygame.image.load(filename)
        if color_key:
            self.sheet = self.sheet.convert()
            self.sheet.set_colorkey(color_key)
        else:
            self.sheet = self.sheet.convert_alpha()
        self.cells = [(px + tw * i, py, tw-m, th) for i in range(tiles)]
        self.index = 0

    def update(self):
        self.tile_rect = self.cells[self.index % len(self.cells)]
        self.index += 1

    def draw(self, surface, x, y):
        rect = pygame.Rect(self.tile_rect)
        rect.center = (x, y) 
        surface.blit(self.sheet, rect, self.tile_rect)

pygame.init()
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

sprite_sheet = SpriteSheet('spritesheet/awesomepossum sheet.bmp', 18, 580, 64, 66, 0, 6, (0, 128, 0))

run = True
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    sprite_sheet.update()

    window.fill(0)
    sprite_sheet.draw(window, *window.get_rect().center)
    pygame.display.update()
    
pygame.quit()
exit()

