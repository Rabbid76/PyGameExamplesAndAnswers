# pygame.mixer module
# https://www.pygame.org/docs/ref/mixer.html
#
# Pygame sound keeps repeating
# https://stackoverflow.com/questions/60013591/pygame-sound-keeps-repeating
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md

import os
import pygame.mixer
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

pygame.mixer.init()
my_sound = pygame.mixer.Sound('music/Alarm09.wav')
#my_sound = pygame.mixer.Sound('ringtone/zeldas_lullaby.mp3')
my_sound.play(0)
pygame.time.wait(int(my_sound.get_length() * 1000))

pygame.mixer.quit()
exit()