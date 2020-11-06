# pygame.mixer.music module
# https://www.pygame.org/docs/ref/music.html
#
# How to play random Mp3 files in Pygame
# https://stackoverflow.com/questions/60250171/how-to-play-random-mp3-files-in-pygame/60250258#60250258
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md 

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('ringtone/zeldas_lullaby.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.delay(10)
    pygame.event.poll()

pygame.quit()
exit()