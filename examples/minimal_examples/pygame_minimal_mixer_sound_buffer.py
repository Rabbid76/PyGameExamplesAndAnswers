# pygame.mixer module
# https://www.pygame.org/docs/ref/music.html
#
# How can I play a sine/square wave using Pygame?
# https://stackoverflow.com/questions/63980583/how-can-i-play-a-sine-square-wave-using-pygame/63980631#63980631
#
# GitHub - PyGameExamplesAndAnswers - Music and sound - Sound - Sound from buffer
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md

import pygame
import numpy as np

pygame.mixer.init()
buffer = np.sin(2 * np.pi * np.arange(44100) * 440 / 44100).astype(np.float32)
sound = pygame.mixer.Sound(buffer)
sound.play(0)
pygame.time.wait(int(sound.get_length() * 1000))

