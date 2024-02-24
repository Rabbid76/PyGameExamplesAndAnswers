# pygame.mixer.music module
# https://www.pygame.org/docs/ref/music.html
#
# How can I Iterate through a list of songs and play them one after eachother
# https://stackoverflow.com/questions/70457867/how-can-i-iterate-through-a-list-of-songs-and-play-them-one-after-eachother/70458293#70458293
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md 


import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource/'))

import re

def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

import random



l = ['_0', '_1', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10', '_12']
random.shuffle(l)
print(l)

l.sort(key = lambda name: get_trailing_number(name))
print(l)

play_list = [f for f in os.listdir('ringtone') if f.endswith('.mp3')]
print(play_list)
current_list = []

pygame.init()
window = pygame.display.set_mode((600, 100))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

window_center = window.get_rect().center
title_surf = None

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if not pygame.mixer.music.get_busy():
        if not current_list:
           current_list = play_list[:]
        current_song = current_list.pop(0)
        pygame.mixer.music.load(os.path.join('ringtone', current_song))
        pygame.mixer.music.play()
        title_surf = font.render(current_song, True, (255, 255, 0))

    window.fill('black')
    if title_surf:
        window.blit(title_surf, title_surf.get_rect(center = window_center))
    pygame.display.flip()
    
pygame.quit()
exit()

