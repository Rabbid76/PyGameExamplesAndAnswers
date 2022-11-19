# pygame.mixer module
# https://www.pygame.org/docs/ref/mixer.html
#
# How can I play two songs at once using Pygame.mixer.music?
# https://stackoverflow.com/questions/67232742/how-can-i-play-two-songs-at-once-using-pygame-mixer-music/67232995#67232995
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.mixer.init()
song_1 = pygame.mixer.Sound('ringtone/zeldas_rescue.mp3')
song_2 = pygame.mixer.Sound('ringtone/zelda_forest_theme.mp3')
song_1.play(0)
song_2.play(0)

while pygame.mixer.get_busy():
    pygame.time.delay(10)
    
pygame.quit()
exit()