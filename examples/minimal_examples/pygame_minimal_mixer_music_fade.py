# pygame.mixer.music module
# https://www.pygame.org/docs/ref/music.html
#
# using PyGame to load mp3
# https://stackoverflow.com/questions/58569476/using-pygame-to-load-mp3/58569531#58569531
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md 

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.init()

audio1 = 'ringtone/zelda_chest.mp3'
audio2 = 'ringtone/zeldas_lullaby.mp3'

pygame.mixer.init()

pygame.mixer.music.load(audio1)
pygame.mixer.music.play()
pygame.time.wait(5000)

pygame.mixer.music.fadeout(3000) 
pygame.time.wait(3000)

pygame.mixer.music.load(audio2)
pygame.mixer.music.play()
pygame.time.wait(5000)

pygame.mixer.music.fadeout(3000) 
pygame.time.wait(3000)

pygame.quit()
exit()