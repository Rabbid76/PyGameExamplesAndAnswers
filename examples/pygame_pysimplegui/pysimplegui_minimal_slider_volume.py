# PySimpleGUI
# https://pysimplegui.readthedocs.io/en/latest/
#
# pygame.mixer.music module
# https://www.pygame.org/docs/ref/music.html
#
# Changing the volume when moving the slider
# https://stackoverflow.com/questions/59775588/changing-the-volume-when-moving-the-slider
#
# GitHub - PyGameExamplesAndAnswers - PyGame in combination with other libraries - PySimpleGUI
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_and_othere_libraries.md

import os
import pygame
import PySimpleGUI as sg
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

class Music:
    def __init__(self, file):
        self.file = file
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()
    def volchange(volume):
        pygame.mixer.music.set_volume(volume)
    def isplaying():
        return pygame.mixer.music.get_busy()

layout = [
    [sg.Button('Play'), 
     sg.Slider(key = 'Volume', range=(0, 100), 
     orientation = 'h', size = (10, 15), default_value = 100, 
     enable_events = True)]
]

filename = 'zeldas_lullaby.mp3'
path = 'ringtone/' + filename
window = sg.Window(filename, layout)

pygame.init()
music = Music(path)

run = True
while run:
    event, values = window.read()
    if event == None:
        run = False
    elif event == 'Play':
        music.play()
    elif event == 'Volume':
        if Music.isplaying():
            Music.volchange(float(values['Volume'] / 100))
    else:
        print(event, values)

pygame.quit()
exit()
        