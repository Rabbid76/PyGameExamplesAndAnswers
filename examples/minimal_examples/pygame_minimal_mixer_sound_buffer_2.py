# pygame.mixer module
# https://www.pygame.org/docs/ref/music.html
#
# Trying to play a sound wave on python using pygame
# https://stackoverflow.com/questions/64950167/trying-to-play-a-sound-wave-on-python-using-pygame/64951687#64951687
#
# GitHub - PyGameExamplesAndAnswers - Music and sound - Sound - Sound from buffer
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md

import pygame
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=1)

print(pygame.mixer.get_init())

size = 44100
#buffer = np.random.randint(-32768, 32767, size)
#buffer = np.repeat(buffer.reshape(size, 1), 2, axis = 1)

buffer = np.random.randint(-32768, 32767, size*2)
buffer = buffer.reshape(size, 2)

sound = pygame.sndarray.make_sound(buffer)
sound.play()
pygame.time.wait(int(sound.get_length() * 1000))


