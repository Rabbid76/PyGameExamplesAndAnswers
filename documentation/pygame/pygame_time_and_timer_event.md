[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Time, timer event and clock

## Wait for a period of time

Related Stack Overflow questions:

- [How to wait some time in pygame?](https://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame/64701602#64701602)

If you just wait for some time, you can use [`pygame.time.wait`](https://www.pygame.org/docs/ref/time.html#pygame.time.wait) or [`pygame.time.delay`](https://www.pygame.org/docs/ref/time.html#pygame.time.delay). However, if you want to display a message and then wait some time, you need to update the display beforehand. The display is updated only if either [`pygame.display.update()`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) or [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip)
is called. Further you've to handles the events by [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump), before the update of the display becomes visible in the window:

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

    window.fill(0)

    # [...]

    if current_time < message_end_time:
        window.blit(message_surf, (x, y))
    pygame.display.flip()
```

:scroll: **[Minimal example - Display a message for a period of time](../../examples/minimal_examples/pygame_minimal_time_text_message_delay.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MessageDelay](https://repl.it/@Rabbid76/PyGame-MessageDelay#main.py)</kbd>

## Time

In pygame the system time can be obtained by calling [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks), which returns the number of milliseconds since [`pygame.init()`](https://www.pygame.org/docs/ref/pygame.html#pygame.init) was called. See [`pygame.time`](https://www.pygame.org/docs/ref/time.html) module.

### After a certain time

Related Stack Overflow questions:

- [How to display an image after a time interval?](https://stackoverflow.com/questions/45609076/how-to-display-an-image-after-a-time-interval/63761611#63761611)

You have to draw the image in the main application loop. Use [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks) to return the number of milliseconds since [`pygame.init()`](https://www.pygame.org/docs/ref/pygame.html#pygame.init) was called. When the `MOUSEBUTTONDOWN` event occurs, then calculate the point in time after that the image has to be displayed. Display the image after the current time is greater than the calculated point of time:

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

:scroll: **[Minimal example - Until a certain time](../../examples/minimal_examples/pygame_minimal_timer_after_a_certain_time.py)**

### Lock for a period of time

Related Stack Overflow questions:

- [How do I stop more than 1 bullet firing at once?](https://stackoverflow.com/questions/60122492/how-do-i-stop-more-than-1-bullet-firing-at-once/60125448#60125448)  
  ![How do I stop more than 1 bullet firing at once?](https://i.stack.imgur.com/1DY2O.gif)

If you want to implement some kind of rapid fire, then the things get more tricky. If you would use the state of `pygame.key.get_pressed()` then you would spawn one bullet in every frame. That is far too fast. You have to implement some timeout.  
When a bullet is fired, the get the current time by [`pygame.time.get_ticks()`](https://www.pygame.org/docs/ref/time.html). Define a number of milliseconds for the delay between to bullets. Add the dela to the time and state the time in a variable (`next_bullet_threshold`). Skip bullets, as long the time is not exceeded:

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

- [How can I show explosion image when collision happens?](https://stackoverflow.com/questions/64305426/how-can-i-show-explosion-image-when-collision-happens)
- [how to handle time for different components in pygame](https://stackoverflow.com/questions/62151703/how-to-handle-time-for-different-components-in-pygame)
- [How to make image stay on screen in pygame?](https://stackoverflow.com/questions/63718110/how-to-make-image-stay-on-screen-in-pygame/63726447#63726447)

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

:scroll: **[Minimal example - For a period of time](../../examples/minimal_examples/pygame_minimal_timer_for_a_period_of_time.py)**

### Triggered by a time interval

Related Stack Overflow questions:

- [How to make instances spawn automatically around the player?](https://stackoverflow.com/questions/54717938/how-to-make-instances-spawn-automatically-around-the-player/54723594#54723594)  
  ![How to make instances spawn automatically around the player?](https://i.stack.imgur.com/RIskl.gif)
- [Spawning multiple instances of the same object concurrently in python](https://stackoverflow.com/questions/62112754/spawning-multiple-instances-of-the-same-object-concurrently-in-python/62112894#62112894)  
  ![Spawning multiple instances of the same object concurrently in python](https://i.stack.imgur.com/1X0kk.gif)

If the time exceeds `next_zombie_time` the span a zombie and set the time for the next zombie to spawn:

```py
current_time = pygame.time.get_ticks()
if current_time > next_zombie_time:
    next_zombie_time = current_time + 1000 # 1 second interval to the next zombie

    # [...] spawn the zombie
```

### Display application (game) time

Related Stack Overflow questions:

- [Python Pygame - How do I add a time counter for my game?](https://stackoverflow.com/questions/55327065/python-pygame-how-do-i-add-a-time-counter-for-my-game/55327292#55327292)
- [Stopwatch between mouse up/down](https://stackoverflow.com/questions/56062519/stopwatch-between-mouse-up-down/56063229#56063229)
- [how to add a stopwatch to pygame?](https://stackoverflow.com/questions/61994805/how-to-add-a-stopwatch-to-pygame/61997846#61997846)  
  ![how to add a stopwatch to pygame?](https://i.stack.imgur.com/ahANd.gif)

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

Related Stack Overflow questions:

In pygame exists a timer event. Use [`pygame.time.set_timer()`](https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer) to repeatedly create a [`USEREVENT`](https://www.pygame.org/docs/ref/event.html) in the event queue.. The time has to be set in milliseconds. e.g.:

```py
timer_interval = 500 # 0.5 seconds
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , timer_interval)
```

Note, in pygame customer events can be defined. Each event needs a unique id. The ids for the user events have to be between `pygame.USEREVENT` (24) and `pygame.NUMEVENTS` (32). In this case `pygame.USEREVENT+1` is the event id for the timer event.  

Receive the event in the event loop:

```py
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

         elif event.type == timer_event:
             # [...]
```

The timer event can be stopped by passing 0 to the _time_ argument of `pygame.time.set_timer`.

### Counter based on timer event

Related Stack Overflow questions:

- [Countdown timer in Pygame](https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame/63551239#63551239)  
  ![Countdown timer in Pygame](https://i.stack.imgur.com/10Gj0.gif)
- [Python 3.8 pygame timer?](https://stackoverflow.com/questions/59944795/python-3-8-pygame-timer/59944869#59944869)  
  ![Python 3.8 pygame timer?](https://i.stack.imgur.com/axkzq.gif)
- [How to display dynamically in Pygame?](https://stackoverflow.com/questions/56453574/how-to-display-dynamically-in-pygame/56454295#56454295)  
  ![How to display dynamically in Pygame?](https://i.stack.imgur.com/C3RZ8.gif)

:scroll: **[Minimal example - Counter](../../examples/minimal_examples/pygame_minimal_timer_counter.py)**

:scroll: **[Minimal example - Count down](../../examples/minimal_examples/pygame_minimal_timer_count_down.py)**

### Action trigger based on timer event

Related Stack Overflow questions:

- [Trying to delay a specific function for spawning enemy after a certain amount of time](https://stackoverflow.com/questions/61409702/trying-to-delay-a-specific-function-for-spawning-enemy-after-a-certain-amount-of/61410788?noredirect=1)
- [How do I continuously trigger an action at certain time intervals? Enemy shoots constant beam instead of bullets in pygame](https://stackoverflow.com/questions/58224668/enemy-shoots-constant-beam-instead-of-bullets-in-pygame/58224870#58224870)
- [How can one continuously generate and track several random objects with a time delay in pygame?](https://stackoverflow.com/questions/57837263/how-to-spawn-and-track-multiple-random-objects-with-time-delay-in-pygame/57837320#57837320)

:scroll: **[Minimal example - Timer callback](../../examples/minimal_examples/pygame_minimal_timer_callback.py)**

## Clock and frames per second

Related Stack Overflow questions:

- [Pygame clock and event loops](https://stackoverflow.com/questions/60444161/pygame-clock-and-event-loops/60447013#60447013)
- [Framerate affect the speed of the game](https://stackoverflow.com/questions/61352366/framerate-affect-the-speed-of-the-game/61352472#61352472)
- [Pygame wait for screen to update](https://stackoverflow.com/questions/60029598/pygame-wait-for-screen-to-update/60030315#60030315)
- [I am having lag problems with this simple game I made in Pygame, Python 3. How can I fix this?](https://stackoverflow.com/questions/58263322/i-am-having-lag-problems-with-this-simple-game-i-made-in-pygame-python-3-how-c/58263682#58263682)

Use [`pygame.time.Clock`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) to control the frames per second and thus the game speed.  

The method [`tick()`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) of a [`pygame.time.Clock`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock) object, delays the game in that way, that every iteration of the loop consumes the same period of time.  
That meas that the loop:

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

[`pygame.time.Clock.tick`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) returns the number of milliseconds passed since the previous call. If you call it in the application loop, then this is the number of milliseconds passed since the last frame.  
Multiply the velocity of the player by the passed time per frame, to get a constant movement independent on the FPS.

For instance define the distance in number of pixel, which the player should move per second (`move_per_second`). Then compute the distance per frame in the application loop:

```py
move_per_second = 500
FPS = 60
fun = True
clock = pygame.time.Clock() 
while run:
    ms_frame = clock .tick(FPS)
    move_per_frame = move_per_second * ms_frame / 1000  

    # [...]
```

# Delay

Related Stack Overflow questions:

- [Is pygame.time.delay() better than time.sleep()?](https://stackoverflow.com/questions/61921644/is-pygame-time-delay-better-than-time-sleep/61922176#61922176)
