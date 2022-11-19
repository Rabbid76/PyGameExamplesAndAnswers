# pygame.mixer.music module
# https://www.pygame.org/docs/ref/music.html
#
# How can I change the name of audio stream in pygame mixer?
# https://stackoverflow.com/questions/68589200/how-can-i-change-the-name-of-audio-stream-in-pygame-mixer/68589599#68589599
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md 

import os
import pygame
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

song_name = "zelda_chest.mp3"

pygame.init()

font = pygame.font.SysFont(None, 40)
title_surf = font.render(song_name, True, (255, 255, 0))

pygame.display.set_icon(pygame.image.load("icon/MusicNote-64.png"))
window = pygame.display.set_mode((max(400, title_surf.get_width()+20), 100))
pygame.display.set_caption(song_name)

pygame.mixer.init()
pygame.mixer.music.load(os.path.join('ringtone', song_name))
pygame.mixer.music.play()

window_center = window.get_rect().center
clock = pygame.time.Clock()
run = True
while run and pygame.mixer.music.get_busy():
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(title_surf, title_surf.get_rect(center = window_center))
    pygame.display.flip()

pygame.quit()
exit()