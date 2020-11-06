[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)
---

# Music and sound

[PyGame](https://www.pygame.org/news) has 2 different modules for playing sound and music, the [pygame.mixer](https://www.pygame.org/docs/ref/mixer.html) module and the [pygame.mixer.music](https://www.pygame.org/docs/ref/music.html) module. This module contains classes for loading Sound objects and controlling playback. The difference is explained in the documentation:

> The difference between the music playback and regular Sound playback is that the music is streamed, and never actually loaded all at once. The mixer system only supports a single music stream at once.

## Sound

Related Stack Overflow questions:

- [how to play wav file in python?](https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python)  
  [Pygame, sounds don't play](https://stackoverflow.com/questions/2936914/pygame-sounds-dont-play/64521581#64521581)  
  [PyGame sound keeps repeating](https://stackoverflow.com/questions/60013591/pygame-sound-keeps-repeating/60015169#60015169)

  :scroll: **[Minimal example - Play sound 1](../../examples/minimal_examples/pygame_minimal_mixer_sound_1.py)**

  :scroll: **[Minimal example - Play sound 2](../../examples/minimal_examples/pygame_minimal_mixer_sound_2.py)**

  :scroll: **[Minimal example - Play sound 3](../../examples/minimal_examples/pygame_minimal_mixer_sound_2.py)**

- [How can I play a sine/square wave using Pygame?](https://stackoverflow.com/questions/63980583/how-can-i-play-a-sine-square-wave-using-pygame/63980631#63980631)

  :scroll: **[Minimal example - Play sound buffer](../../examples/minimal_examples/pygame_minimal_mixer_sound_buffer.py)**

- [Pygame setting volume when target is a list](https://stackoverflow.com/questions/63099024/pygame-setting-volume-when-target-is-a-list/63099061#63099061)

If you want to play a single _wav_ file, you have to initialize the module and create a [`pygame.mixer.Sound()`](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound) object from the file. Invoke [`play()`](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.play) to start playing the file. Finally, you have to wait for the file to play.

Use [`get_length()`](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.get_length) to get the length of the sound in seconds and wait for the sound to finish: 
(The argument to [`pygame.time.wait()`](https://www.pygame.org/docs/ref/time.html#pygame.time.wait) is in milliseconds)

```py
import pygame

pygame.mixer.init()
my_sound = pygame.mixer.Sound('my_sound.wav')
my_sound.play()
pygame.time.wait(int(my_sound.get_length() * 1000))
```

Alternatively you can use [`pygame.mixer.get_busy`](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.play) to test if a sound is being mixed. Query the status of the mixer continuously in a loop.  
In the loop, you need to delay the time by either [`pygame.time.delay`](https://www.pygame.org/docs/ref/time.html#pygame.time.delay) or [`pygame.time.Clock.tick`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick). In addition, you need to handle the events in the application loop. See [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get) respectively [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump):

> For each frame of your game, you will need to make some sort of call to the event queue. This ensures your program can internally interact with the rest of the operating system.

```py
import pygame
pygame.init()

pygame.mixer.init()
my_sound = pygame.mixer.Sound('my_sound.wav')
my_sound.play()

while pygame.mixer.get_busy():
    pygame.time.delay(10)
    pygame.event.poll()
```

[Numpy arrays](https://numpy.org/doc/stable/reference/generated/numpy.array.html) can be loaded directly to a [`pygame.mixer.Sound`](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound) object and [`play`](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.play) it:

```py
import pygame
import numpy as np

pygame.mixer.init()

buffer = np.sin(2 * np.pi * np.arange(44100) * 440 / 44100).astype(np.float32)
sound = pygame.mixer.Sound(buffer)

sound.play(0)
pygame.time.wait(int(sound.get_length() * 1000))
```

## Music

Related Stack Overflow questions:

- [How can I play an mp3 with pygame?](https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame/64521533#64521533)

- [How to play random Mp3 files in Pygame](https://stackoverflow.com/questions/60250171/how-to-play-random-mp3-files-in-pygame/60250258#60250258)

  :scroll: **[Minimal example - Play random mp3 from directory](../../examples/minimal_examples/pygame_minimal_mixer_music_random.py)**

- [using PyGame to load mp3](https://stackoverflow.com/questions/58569476/using-pygame-to-load-mp3/58569531#58569531)
- [Pygame background music not playing](https://stackoverflow.com/questions/56572662/pygame-background-music-not-playing/56573636#56573636)
- [Why pygame.event.wait stops music play after 20 seconds or so](https://stackoverflow.com/questions/61389698/why-pygame-event-wait-stops-music-play-after-20-seconds-or-so/61390284#61390284)
- [Loop over a list containing path to sound files](https://stackoverflow.com/questions/63488105/loop-over-a-list-containing-path-to-sound-files/63488275#63488275)

:scroll: **[Minimal example - Play music 1](../../examples/minimal_examples/pygame_minimal_mixer_music_1.py)**

:scroll: **[Minimal example - Play music 2](../../examples/minimal_examples/pygame_minimal_mixer_music_2.py)**

If you want to play a _mp3_ file, you need to initialize the module. Load the file with [`pygame.mixer.music.load`](https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.load). Invoke [`pygame.mixer.music.play()`](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.play) to start playback of the music stream. Finally, you have to wait for the file to play.  
Use [`pygame.mixer.music.get_busy()`](https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_busy) to test if a sound is being mixed. Query the status of the mixer continuously in a loop.  
In the loop, you need to delay the time by either [`pygame.time.delay`](https://www.pygame.org/docs/ref/time.html#pygame.time.delay) or [`pygame.time.Clock.tick`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick). In addition, you need to handle the events in the application loop. See [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get) respectively [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump):

> For each frame of your game, you will need to make some sort of call to the event queue. This ensures your program can internally interact with the rest of the operating system.

```py
import pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('my_music.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(60)
    pygame.event.poll()
```

The unit of the time parameter to [`pygame.mixer.music.fadeout()`](https://www.pygame.org/docs/ref/time.html) is milliseconds. 1 second is 1000 milliseconds:

```py
pygame.mixer.music.load(audio1)
pygame.mixer.music.play()

# play for 12.5 seconds
pygame.time.wait(12500)

# fade out for 10 seconds
pygame.mixer.music.fadeout(10000)
pygame.time.wait(10000)
```
