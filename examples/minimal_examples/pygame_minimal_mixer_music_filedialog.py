# pygame.mixer.music module
# https://www.pygame.org/docs/ref/music.html
#
# I want to play selected mp3 files in my folder but it doesn't work
# https://stackoverflow.com/questions/64842008/i-want-to-play-selected-mp3-files-in-my-folder-but-it-doesnt-work/65352966#65352966
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md 

import os
import pygame
import tkinter.filedialog

song = tkinter.filedialog.askopenfile(
    initialdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource/notification'), 
    filetypes = (('mp3 Files.', '*.mp3'), ))

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(song.name)
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    #clock.tick(60)
    pygame.event.poll()

pygame.quit()
exit()