[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"So if you want to go fast, if you want to get done quickly, if you want your code to be easy to write, make it easy to read."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Time, timer event and clock

Related Stack Overflow questions:

- [Is there a way to have different tick rates for differents parts of my code in pygame?](https://stackoverflow.com/questions/71088920/is-there-a-way-to-have-different-tick-rates-for-differents-parts-of-my-code-in-p/71089817#71089817)  
- [I define a movement method for a character, but I don't know how to itmake it pause for a moment between each move](https://stackoverflow.com/questions/71546585/i-define-a-movement-method-for-a-character-but-i-dont-know-how-to-itmake-it-pa/71546649#71546649)  
- **[Do something every x (milli)seconds in pygame](https://stackoverflow.com/questions/18948981/do-something-every-x-milliseconds-in-pygame/76697145#76697145)**  
- [Pygame- way to create more USEREVENT type events?](https://stackoverflow.com/questions/23571956/pygame-way-to-create-more-userevent-type-events/77005065#77005065)  

If you want to control something over time in Pygame you have two options:

1. Use [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks) to measure time and and implement logic that controls the object depending on the time.

2. Use the timer event. Use [`pygame.time.set_timer()`](https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer) to repeatedly create a [`USEREVENT`](https://www.pygame.org/docs/ref/event.html) in the event queue. Change object states when the event occurs.

![time example](https://i.stack.imgur.com/QTT2q.gif)

📁 **[Minimal example - `get_ticks`](../../examples/minimal_examples/pygame_minimal_timer_get_ticks_1.py)**  
▶ **[run minimal example - `get_ticks`](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimla_timer_get_ticks_1/build/web/)**

📁 **[Minimal example - timer event](../../examples/minimal_examples/pygame_minimal_timer_event_1.py)**  
▶ **[run minimal example - timer event](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimal_timer_event_1/build/web/)**

- [Rendering Images At a Different Framerate Than The Game Window](https://stackoverflow.com/questions/75712024/rendering-images-at-a-different-framerate-than-the-game-window/75712065#75712065)
  ![Rendering Images At a Different Framerate Than The Game Window](https://i.stack.imgur.com/ZTPYx.gif)

📁 **[Minimal example - different frame rates](../../examples/minimal_examples/pygame_minimal_timer_animation_2.py)**  
▶ **[run minimal example - different frame rates](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimal_timer_animation_2/build/web/)**

## Wait for a period of time

Related Stack Overflow questions:

- **[Why doesn't PyGame draw in the window before the delay or sleep?](https://stackoverflow.com/questions/63218889/why-is-pygame-not-showing-text-on-window/63218970#63218970)**
- [How to wait some time in pygame?](https://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame/64701602#64701602)

If you just wait for some time, you can use [`pygame.time.wait`](https://www.pygame.org/docs/ref/time.html#pygame.time.wait) or [`pygame.time.delay`](https://www.pygame.org/docs/ref/time.html#pygame.time.delay). However, if you want to display a message and then wait some time, you need to update the display beforehand. The display is updated only if either [`pygame.display.update()`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) or [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip)
is called. See [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip):

> This will update the contents of the entire display.

Further you've to handles the events with [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump), before the update of the display becomes visible in the window. See [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump):

> For each frame of your game, you will need to make some sort of call to the event queue. This ensures your program can internally interact with the rest of the operating system.

This all means that you have to call `pygame.display.flip()` and `pygame.event.pump()` before `pygame.time.wait()`: 

```py
screen.blit(text, (x, y))
pygame.display.flip()
pygame.event.pump()
pygame.time.delay(delay * 1000) # 1 second == 1000 milliseconds
```

In any case, this is not the way to wait or delay something in a typical application. The game does not respond while you wait. Use [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks) to measure the time.  
For instance if you want to show a message on the display, get the current time and calculate the point in time after that the message has to disappear. Display the message as long as the current time is below the calculated time:

```py
message_end_time = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # [...]

    current_time = pygame.time.get_ticks()
    if something_has_happened:
        message_surf = font.render('Important message!', True, (255, 0, 0))
        message_end_time = pygame.time.get_ticks() + 3000 # display for 3 seconds

    window.fill('black')

    # [...]

    if current_time < message_end_time:
        window.blit(message_surf, (x, y))
    pygame.display.flip()
```

📁 **[Minimal example - Display a message for a period of time](../../examples/minimal_examples/pygame_minimal_time_text_message_delay.py)**  
▶ **[run minimal example - Display a message for a period of time](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimal_time_text_message_delay/build/web/)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MessageDelay](https://replit.com/@Rabbid76/PyGame-MessageDelay#main.py)**

## Time

In pygame the system time can be obtained by calling [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks), which returns the number of milliseconds since [`pygame.init()`](https://www.pygame.org/docs/ref/pygame.html#pygame.init) was called. See [`pygame.time`](https://www.pygame.org/docs/ref/time.html) module.

### After a certain time

Related Stack Overflow questions:

- [How to display an image after a time interval?](https://stackoverflow.com/questions/45609076/how-to-display-an-image-after-a-time-interval/63761611#63761611)
- [CREATING A REACTION TIME TEST GAME IN PYGAME](https://stackoverflow.com/questions/66029125/creating-a-reaction-time-test-game-in-pygame/66033644#66033644)  

You have to draw the image in the main application loop. Use [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks) to get the number of milliseconds since [`pygame.init()`](https://www.pygame.org/docs/ref/pygame.html#pygame.init) was called. When the `MOUSEBUTTONDOWN` event occurs, then calculate the point in time after that the image has to be displayed. Display the image after the current time is greater than the calculated point of time:

```py
image_time = 0

run = True
while run:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if image_time > 0 and current_time >= image_time:
        image_time = current_time + 1000 # 1000 milliseconds == 3 seconds

    # [...]

    if current_time >= image_time:
        # draw object or do action
        # [...]
```

📁 **[Minimal example - Until a certain time](../../examples/minimal_examples/pygame_minimal_timer_after_a_certain_time.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TimerAfterACertainTime](https://replit.com/@Rabbid76/PyGame-TimerAfterACertainTime#main.py)**

### Lock for a period of time

Related Stack Overflow questions:

- [How do I stop more than 1 bullet firing at once?](https://stackoverflow.com/questions/60122492/how-do-i-stop-more-than-1-bullet-firing-at-once/60125448#60125448)  
  ![How do I stop more than 1 bullet firing at once?](https://i.stack.imgur.com/W6lzh.gif)

  📁 **[minimal example - Shoot bullet](../../examples/minimal_examples/pygame_minimal_shoot_bullet.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ShootBullet](https://replit.com/@Rabbid76/PyGame-ShootBullet#main.py)**

  📁 **[minimal example - Sustained fire](../../examples/minimal_examples/pygame_minimal_shoot_bullet_sustained_fire.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ShootBulletSustainedFire](https://replit.com/@Rabbid76/PyGame-ShootBulletSustainedFire#main.py)**

- [Python Pygame Tetris, problems with handling of keypresses. implement delayed auto shift. how long a key has to be pressed before moving](https://stackoverflow.com/questions/69344528/python-pygame-tetris-problems-with-handling-of-keypresses-implement-delayed-au/69344706#69344706)  

If you want to implement some kind of rapid fire, then the things get more tricky. If you would use the state of `pygame.key.get_pressed()` then you would spawn one bullet in every frame. That is far too fast. You have to implement some timeout.  
When a bullet is fired, the get the current time by [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html). Define a number of milliseconds for the delay between to bullets. Add the delta to the time and state the time in a variable (`next_bullet_threshold`). Skip bullets, as long the time is not exceeded:

```py
next_bullet_threshold = 0

run = True
while run == True:

    # [...]

    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_time > next_bullet_threshold:

        bullet_delay = 500 # 500 milliseconds (0.5 seconds)
        next_bullet_threshold = current_time + bullet_delay

        if player1.left == True:   ## handles the direction of the bullet
            facing = -1
        else:
            facing = 1  
        if len(bullets) < 5:
            bx, by = player1.x + player1.width //2 ,player1.y + player1.height//2
            bullets.append(projectile(bx, by, 6, black, facing))
```

### For a period of time

Related Stack Overflow questions:

- [How can I show explosion image when collision happens?](https://stackoverflow.com/questions/64305426/how-can-i-show-explosion-image-when-collision-happens/64305746#64305746)  
  ![How can I show explosion image when collision happens?](https://i.stack.imgur.com/mdCj6.gif)

   📁 **[Minimal example - Timer for a period of time](../../examples/minimal_examples/pygame_minimal_timer_for_a_period_of_time.py)**  

- [Adding a particle effect to my clicker game](https://stackoverflow.com/questions/64793618/adding-a-particle-effect-to-my-clicker-game/64794954#64794954)  
  ![Adding a particle effect to my clicker game](https://i.stack.imgur.com/bWOOF.gif)

  📁 **[Minimal example - Spawn text on click](../../examples/minimal_examples/pygame_minimal_timer_for_a_period_of_time_random_text.py)**  
  ▶ **[run minimal example - Spawn text on click](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimal_timer_for_a_period_of_time_random_text/build/web/)**

- [Pygame "pop up" text - How to show an image only for a period of time?](https://stackoverflow.com/questions/70996802/pygame-pop-up-text-how-to-show-an-image-only-for-a-period-of-time/70996856#70996856)  
  ![Pygame "pop up" text - How to show an image only for a period of time?](https://i.stack.imgur.com/TIyPv.gif)  

  📁 **[Minimal example - pop up text](../../examples/minimal_examples/pygame_minimal_timer_popup_text_1.py)**  
  ▶ **[run minimal example - Spawn text on click](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimal_timer_popup_text_1/build/web/)**

- [How can i controll collision from sprites?](https://stackoverflow.com/questions/71184756/how-can-i-controll-collision-from-sprites/73938856#73938856)  
  ![How can i controll collision from sprites?](https://i.stack.imgur.com/eRmUW.gif)  

  📁 **[Minimal example - random pop up text](../../examples/minimal_examples/pygame_minimal_timer_popup_text_2.py)**  
  ▶ **[run minimal example - random pop up text](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimal_timer_popup_text_2/build/web/)**

- [how to handle time for different components in pygame](https://stackoverflow.com/questions/62151703/how-to-handle-time-for-different-components-in-pygame)
- [How to make image stay on screen in pygame?](https://stackoverflow.com/questions/63718110/how-to-make-image-stay-on-screen-in-pygame/63726447#63726447)
- [Time Delay and keeping track of the of # of click](https://stackoverflow.com/questions/65047229/time-delay-and-keeping-track-of-the-of-of-click/65047717#65047717)  
- [How to know if the spacebar is pressed for more than 2 seconds in pygame](https://stackoverflow.com/questions/67800220/how-to-know-if-the-spacebar-is-pressed-for-more-than-2-seconds-in-pygame/67800253#67800253)  

Calculate the point in time after that the explosion image has to be removed. Add the coordinates of the explosion and the end time point to the head of a list (`explosionList`). Draw the explosion(s) in the main application loop. Remove the expired explosions from the tail of the list.  
With this algorithm it is possible to manage multiple explosions.

Test algorithm:

```py
current_time = 0.5
explosionList = [(4, 1, 1), (3, 2, 2), (2, 3, 3), (1, 4, 4)]
while len(explosionList) > 0:
    for i in range(len(explosionList)):
        if current_time < explosionList[i][0]:
            print(explosionList[i][1:])
        else:
            explosionList = explosionList[:i]
            break
    print(explosionList)
    current_time += 1
```

📁 **[Minimal example - For a period of time](../../examples/minimal_examples/pygame_minimal_timer_for_a_period_of_time.py)**

### Triggered by a time interval

Related Stack Overflow questions:

- [pygame tetris fever_mode adding timer](https://stackoverflow.com/questions/69590294/pygame-tetris-fever-mode-adding-timer/69590304#69590304)  
  ![pygame tetris fever_mode adding timer](https://i.stack.imgur.com/00weE.gif)

  📁 **[Minimal example - Timer toggle](../../examples/minimal_examples/pygame_minimal_timer_toggle.py)**

- **[Spawning multiple instances of the same object concurrently in python](https://stackoverflow.com/questions/62112754/spawning-multiple-instances-of-the-same-object-concurrently-in-python/62112894#62112894)**  
  ![Spawning multiple instances of the same object concurrently in python](https://i.stack.imgur.com/cVQze.gif)

  📁 **[Minimal example - Spawn objects](../../examples/minimal_examples/pygame_minimal_timer_spawn_objects.py)**  
  ▶ **[run minimal example - Spawn objects](https://rabbid76.github.io/PyGameExamplesAndAnswers/examples/minimal_exmaples_web/pygame_minimal_timer_spawn_objects/build/web/)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TimerSpawnObjects](https://replit.com/@Rabbid76/PyGame-TimerSpawnObjects#main.py)**

- [How do I make the image repeat - for example 10x in a row - in Pygame](https://stackoverflow.com/questions/69884697/how-do-i-make-the-image-repeat-for-example-10x-in-a-row-in-pygame/69884946#69884946)  
  ![How do I make the image repeat - for example 10x in a row - in Pygame](https://i.stack.imgur.com/2kbR7.gif)

  📁 **[Minimal example - Spawn sprites](../../examples/minimal_examples/pygame_minimal_sprite_spawn.py)**

- [How to make instances spawn automatically around the player?](https://stackoverflow.com/questions/54717938/how-to-make-instances-spawn-automatically-around-the-player/54723594#54723594)  
  ![How to make instances spawn automatically around the player?](https://i.stack.imgur.com/RIskl.gif)
  ![Spawning multiple instances of the same object concurrently in python](https://i.stack.imgur.com/1X0kk.gif)
- [How to run multiple while loops at a time in Pygame](https://stackoverflow.com/questions/65263318/how-to-run-multiple-while-loops-at-a-time-in-pygame/65263396#65263396)  
- [Issues with pygame.time.get_ticks()](https://stackoverflow.com/questions/65529525/issues-with-pygame-time-get-ticks/65529554#65529554)  

It does not work that way. `time.sleep`, [`pygame.time.wait()`](https://www.pygame.org/docs/ref/time.html#pygame.time.wait) or [`pygame.time.delay`](https://www.pygame.org/docs/ref/time.html#pygame.time.delay) is not the right way to control time and gameplay within an application loop. The game does not respond while you wait. The application loop runs continuously. You have to measure the time in the loop and spawn the objects according to the elapsed time. Add the newly created objects to a list. Redraw all of the objects and the entire scene in each frame.

Use [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks) to measure the time. Define a time interval after which a new object should appear. Create an object when the point in time is reached and calculate the point in time for the next object:

```py
object_list = []
time_interval = 500 # 500 milliseconds == 0.5 seconds
next_object_time = 0 

while run:
    # [...]
    
    current_time = pygame.time.get_ticks()
    if current_time > next_object_time:
        next_object_time += time_interval
        object_list.append(Object())
```

### Display application (game) time

Related Stack Overflow questions:

- [Python Pygame - How do I add a time counter for my game?](https://stackoverflow.com/questions/55327065/python-pygame-how-do-i-add-a-time-counter-for-my-game/55327292#55327292)
- [Stopwatch between mouse up/down](https://stackoverflow.com/questions/56062519/stopwatch-between-mouse-up-down/56063229#56063229)
- [how to add a stopwatch to pygame?](https://stackoverflow.com/questions/61994805/how-to-add-a-stopwatch-to-pygame/61997846#61997846)  
  ![how to add a stopwatch to pygame?](https://i.stack.imgur.com/ahANd.gif)
- [Trying to change image of moving character in every 0.25 seconds PyGame](https://stackoverflow.com/questions/64188831/trying-to-change-image-of-moving-character-in-every-0-25-seconds-pygame-1-9-6-py/65380355#65380355)

Use [`pygame.time.get_ticks`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks) to get the current time in milliseconds and set the start time, before the main loop:

```py
start_time = pygame.time.get_ticks()
while True:

    # [...]
```

Calculate the elapsed time in every frame. To convert from milliseconds to seconds, the time difference has to be divided by 1000.  
Render the time text to a surface by ([`font.render`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render)). Note, `.render()` returns a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object and a [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html). The rectangle can be used to calculate the position of the text. In the following the text is placed at the bottom right, with a margin of 20 to the border of the window:

```py
while True:

    # [...]

    if inventory[coins] < 100:
        current_time = pygame.time.get_ticks()
        delta_time_s = (current_time - start_time) // 1000

        text_surf, text_rect = font.render(str(delta_time_s), (255, 255, 255), size=30) 
        margin = 20       # margin to the window 
        size = (200, 200) # window size
        text_pos = (size[0] - text_rect.width - margin, size[1] - text_rect.height - margin)

        displaysurf.blit(text_surf, text_pos)
```

If you want to show the tenths of seconds, then the calculation of `delta_time_s` has to be changed:  

```py
delta_time_s = (current_time - start_time) // 100 / 10
```

Store the milliseconds when `MOUSEBUTTONDOWN` and calculate the time difference in the main loop:

```py
from pygame import *

screen = display.set_mode((160, 90))

clock = time.Clock()
run = True
started = False
while run:

    for new_event in event.get():
        if new_event.type == QUIT:
            run = False

        if new_event.type == MOUSEBUTTONDOWN:
            start_time = time.get_ticks()
            started = True

        if new_event.type == MOUSEBUTTONUP:
            started = False

    if started:
        current_time = time.get_ticks()
        sec = (current_time - start_time) / 1000.0
        print(sec)

    display.update()
```

## Timer event

In pygame exists a timer event. Use [`pygame.time.set_timer()`](https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer) to repeatedly create a [`USEREVENT`](https://www.pygame.org/docs/ref/event.html) in the event queue. The time has to be set in milliseconds.  
For a timer event you need to define a unique user events id. The ids for the user events have to be between `pygame.USEREVENT` (24) and `pygame.NUMEVENTS` (32). In this case `pygame.USEREVENT+1` is the event id for the timer event.
Receive the event in the event loop:

```py
timer_interval = 500 # 0.5 seconds
timer_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event_id, timer_interval)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

         elif event.type == timer_event_id:
             # [...]
```

The timer event can be stopped by passing 0 to the _time_ argument of `pygame.time.set_timer`.

### Counter based on timer event

Related Stack Overflow questions:

- [Countdown timer in Pygame](https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame/63551239#63551239)  
  ![Countdown timer in Pygame](https://i.stack.imgur.com/10Gj0.gif)
- [How do I use a PyGame timer event? How to add a clock to a pygame screen using a timer?](https://stackoverflow.com/questions/59944795/python-3-8-pygame-timer/59944869#59944869)  
  ![How do I use a PyGame timer event? How to add a clock to a pygame screen using a timer?](https://i.stack.imgur.com/axkzq.gif)
- [How to display dynamically in Pygame?](https://stackoverflow.com/questions/56453574/how-to-display-dynamically-in-pygame/56454295#56454295)  
  ![How to display dynamically in Pygame?](https://i.stack.imgur.com/C3RZ8.gif)

📁 **[Minimal example - Counter](../../examples/minimal_examples/pygame_minimal_timer_counter.py)**

📁 **[Minimal example - Count down](../../examples/minimal_examples/pygame_minimal_timer_count_down.py)**

📁 **[Minimal example - Timer callback](../../examples/minimal_examples/pygame_minimal_timer_callback.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TimerCallback](https://replit.com/@Rabbid76/PyGame-TimerCallback#main.py)**

### Action trigger based on timer event

Related Stack Overflow questions:

- **[Spawning multiple instances of the same object concurrently in python](https://stackoverflow.com/questions/62112754/spawning-multiple-instances-of-the-same-object-concurrently-in-python/62112894#62112894)**  
  ![Spawning multiple instances of the same object concurrently in python](https://i.stack.imgur.com/cVQze.gif)

  📁 **[Minimal example - Spawn objects](../../examples/minimal_examples/pygame_minimal_timer_event_spawn_objects.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TimerEventSpawn](https://replit.com/@Rabbid76/PyGame-TimerEventSpawn#main.py)**

- [Trying to delay a specific function for spawning enemy after a certain amount of time](https://stackoverflow.com/questions/61409702/trying-to-delay-a-specific-function-for-spawning-enemy-after-a-certain-amount-of/61410788#61410788)
- [How do I continuously trigger an action at certain time intervals? Enemy shoots constant beam instead of bullets in pygame](https://stackoverflow.com/questions/58224668/enemy-shoots-constant-beam-instead-of-bullets-in-pygame/58224870#58224870)
- [How can one continuously generate and track several random objects with a time delay in pygame?](https://stackoverflow.com/questions/57837263/how-to-spawn-and-track-multiple-random-objects-with-time-delay-in-pygame/57837320#57837320)

It does not work that way. `time.sleep`, [`pygame.time.wait()`](https://www.pygame.org/docs/ref/time.html#pygame.time.wait) or [`pygame.time.delay`](https://www.pygame.org/docs/ref/time.html#pygame.time.delay) is not the right way to control time and gameplay within an application loop. The game does not respond while you wait. The application loop runs continuously. You have to measure the time in the loop and spawn the objects according to the elapsed time. Add the newly created objects to a list. Redraw all of the objects and the entire scene in each frame.

Use the [`pygame.event`](https://www.pygame.org/docs/ref/event.html) module. Use [`pygame.time.set_timer()`](https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer) to repeatedly create a [`USEREVENT`](https://www.pygame.org/docs/ref/event.html) in the event queue. The time has to be set in milliseconds. e.g.:

```py
object_list = []
time_interval = 500 # 500 milliseconds == 0.5 seconds
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_interval)
```

Note, in pygame customer events can be defined. Each event needs a unique id. The ids for the user events have to be between `pygame.USEREVENT` (24) and `pygame.NUMEVENTS` (32). In this case `pygame.USEREVENT+1` is the event id for the timer event.  

Receive the event in the event loop:

```py
while run:
    for event in pygame.event.get():
        if event.type == timer_event:
            object_list.append(Object())
```

The timer event can be stopped by passing 0 to the _time_ argument of `pygame.time.set_timer`.

## Display time

Related Stack Overflow questions:

- [How to create a visual timer?](https://stackoverflow.com/questions/71134979/how-to-create-a-visual-timer/71165600#71165600)  
  ![How to create a visual timer?](https://i.stack.imgur.com/kE4zf.gif)

## Clock and frames per second

Related Stack Overflow questions:

- [Does running pygame usually make computers warm](https://stackoverflow.com/questions/74228538/does-running-pygame-usually-make-computers-warm/74228568#74228568)  
- [Pygame clock and event loops](https://stackoverflow.com/questions/60444161/pygame-clock-and-event-loops/60447013#60447013)
- [Framerate affect the speed of the game](https://stackoverflow.com/questions/61352366/framerate-affect-the-speed-of-the-game/61352472#61352472)
- [Pygame wait for screen to update](https://stackoverflow.com/questions/60029598/pygame-wait-for-screen-to-update/60030315#60030315)
- [I am having lag problems with this simple game I made in Pygame, Python 3. How can I fix this?](https://stackoverflow.com/questions/58263322/i-am-having-lag-problems-with-this-simple-game-i-made-in-pygame-python-3-how-c/58263682#58263682)
- [Pygame running differently from different python interpreters](https://stackoverflow.com/questions/65274217/pygame-running-differently-from-different-python-interpreters/65274248#65274248)  
- [How to have unlimited FPS and still control the FPS of your program in Pygame?](https://stackoverflow.com/questions/67977386/how-to-have-unlimited-fps-and-still-control-the-fps-of-your-program-in-pygame/67977432#67977432)  

Use [`pygame.time.Clock`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) to control the frames per second and thus the game speed.  

The method [`tick()`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) of a [`pygame.time.Clock`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock) object, delays the game in that way, that every iteration of the loop consumes the same period of time. See [`pygame.time.Clock.tick()`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick):

> This method should be called once per frame.

That means that the loop:

>```py
>clock = pygame.time.Clock()
>run = True
>while run:
>    clock.tick(60)
>```

runs 60 times per second.

See [`pygame.time.Clock.tick()`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick):

> This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.

### Time per frame

Related Stack Overflow questions:

- [Framerate affect the speed of the game](https://stackoverflow.com/questions/61352366/framerate-affect-the-speed-of-the-game/61352472#61352472)
- [Pygame snake velocity too high when the fps above 15](https://stackoverflow.com/questions/61034515/pygame-snake-velocity-too-high-when-the-fps-above-15/61034931#61034931)
- [Changing FPS on pygame in order to achieve smoothness of sprite's movement](https://stackoverflow.com/questions/59037251/changing-fps-on-pygame-in-order-to-achieve-smoothness-of-sprites-movement/65371237?noredirect=1)  
- [Anyone want to tell me why my pygame code lags while using pygame Vectors?](https://stackoverflow.com/questions/65758517/anyone-want-to-tell-me-why-my-pygame-code-lags-while-using-pygame-vectors/65758921#65758921)   

You have to calculate the movement per frame depending on the frame rate.

[`pygame.time.Clock.tick`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) returns the number of milliseconds since the last call. When you call it in the application loop, this is the number of milliseconds that have passed since the last frame. Multiply the objects speed by the elapsed time per frame to get constant movement regardless of FPS.

Define the distance in pixels that the player should move per second (`move_per_second`). Then compute the distance per frame in the application loop:

```py
move_per_second = 500
FPS = 60
run = True
clock = pygame.time.Clock()
while run:
    ms_frame = clock.tick()
    move_per_frame = move_per_second * ms_frame / 1000  

    # [...]
```

### Frames per second

Related Stack Overflow questions:

- [Why do I get a constant 0 fps in pygame](https://stackoverflow.com/questions/65346173/why-do-i-get-a-constant-0-fps-in-pygame/65346222#65346222)  
- [Show FPS in Pygame](https://stackoverflow.com/questions/67946230/show-fps-in-pygame/67946908#67946908)  

See [`get_fps()`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.get_fps):

> Compute your game's framerate (in frames per second). It is computed by averaging the last ten calls to `Clock.tick()`.

# Delay, Sleep, Wait

Related Stack Overflow questions:

- [Pygame: pygame.time.Clock, or time.sleep](https://stackoverflow.com/questions/67285976/pygame-pygame-time-clock-or-time-sleep/67286018#67286018) 
- [Is pygame.time.delay() better than time.sleep()?](https://stackoverflow.com/questions/61921644/is-pygame-time-delay-better-than-time-sleep/61922176#61922176)
