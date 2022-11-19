# pygame.mixer.music module
# https://www.pygame.org/docs/ref/music.html
#
# Unable to load music
# https://stackoverflow.com/questions/69649372/unable-to-load-music/69649760?noredirect=1
#
# GitHub - PyGameExamplesAndAnswers - Music and sound
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_music_and_sound.md 

from pygame import mixer
import time
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

mixer.init()
mixer.music.load('ringtone/zeldas_lullaby.mp3')
mixer.music.play()

while mixer.music.get_busy():
   time.sleep(0.01)

mixer.quit()