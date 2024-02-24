[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"The goal of software architecture is to minimize the human resources required to build and maintain the required system."  
Robert C. Martin, Clean Architecture

---

# Event and application loop

See also [Python PyGame Introduction](https://www.pygame.org/docs/tut/PygameIntro.html)

## Post event

Related Stack Overflow questions:

- [How to write a unittest for script using pygame, and members like pygame.MOUSEBUTTONDOWN?](https://stackoverflow.com/questions/55903344/how-to-write-a-unittest-for-script-using-pygame-and-members-like-pygame-mousebu/70600477#70600477)

## Application loop

Related Stack Overflow questions:

- **[Why is my PyGame application not running at all?](https://stackoverflow.com/questions/65264616/why-is-my-pygame-application-not-running-at-all/65264742#65264742)**  
- **[Why is nothing drawn in PyGame at all?](https://stackoverflow.com/questions/65113967/why-is-nothing-drawn-in-pygame-at-all/65114059#65114059)**
- **[How to run multiple while loops at a time in Python](https://stackoverflow.com/questions/65263318/how-to-run-multiple-while-loops-at-a-time-in-python/65263396#65263396)**
- [Pygame window freezes when it opens](https://stackoverflow.com/questions/57642415/pygame-window-freezes-when-it-opens/57644255#57644255)
- [Why is my pygame application loop not working properly?](https://stackoverflow.com/questions/60387348/how-to-make-a-camera-for-a-2d-topdown-game-in-pygame/60390374#60390374)
- [Is it possible for a sprite to react to a specific color](https://stackoverflow.com/questions/61703850/is-it-possible-for-a-sprite-to-react-to-a-specific-color/61704072#61704072)
- [Why text display for 2 seconds in pygame](https://stackoverflow.com/questions/62459547/why-text-display-for-2-seconds-in-pygame/65528753#65528753)
- [pygame: low fps causes difficulties to detect events](https://stackoverflow.com/questions/65854146/pygame-low-fps-causes-difficulties-to-detect-events/65857125#65857125)
- [Pygame input which isn't keyboard/mouse](https://stackoverflow.com/questions/66910207/pygame-input-which-isnt-keyboard-mouse/66910257#66910257)

If you want something to be drawn permanently, you need to draw it in the application loop

The typical PyGame application loop has to:

- limit the frames per second to limit CPU usage with [`pygame.time.Clock.tick`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock)
- handle the events by calling either [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump) or [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get).
- update the game states and positions of objects dependent on the input events and time (respectively frames)
- clear the entire display or draw the background
- draw the entire scene (`blit` all the objects)
- update the display by calling either [`pygame.display.update()`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) or [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip)

```py
import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# main application loop
run = True
while run:
    # limit frames per second
    clock.tick(100)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # clear the display
    window.fill('black')

    # draw the scene   
    pygame.draw.circle(window, (255, 0, 0), (250, 250), 100)

    # update the display
    pygame.display.flip()

pygame.quit()
exit()
```

You are actually drawing on a [`Surface`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) object. If you draw on the _Surface_ associated to the PyGame display, this is not immediately visible in the display. The changes become visible, when the display is updated with either [`pygame.display.update()`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) or [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip).

See [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip):

> This will update the contents of the entire display.

📁 **[Minimal example - Game loop](../../examples/minimal_examples/pygame_minimal_application_loop.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MinimalApplicationLoop](https://replit.com/@Rabbid76/PyGame-MinimalApplicationLoop#main.py)**

- [How to add a background and simple square as a character for a single screen platformer in pygame?](https://stackoverflow.com/questions/74161044/how-to-add-a-background-and-simple-square-as-a-character-for-a-single-screen-pla/74161707#74161707)  
  ![How to add a background and simple square as a character for a single screen platformer in pygame?](https://i.stack.imgur.com/lC8JO.gif)

📁 **[Minimal example - Game loop and movement](../../examples/minimal_examples/pygame_minimal_application_loop_2.py)**

### Quit

Related Stack Overflow questions:

- [What is the difference between .quit and .QUIT in pygame](https://stackoverflow.com/questions/67526054/what-is-the-difference-between-quit-and-quit-in-pygame/67526103#67526103)  
- [I keep getting this error “pygame.error: display Surface quit” and dont know what to do](https://stackoverflow.com/questions/62887724/i-keep-getting-this-error-pygame-error-display-surface-quit-and-dont-know-wha/62888228#62888228)  
- [why is the exit window button work but the exit button in the game does not work?](https://stackoverflow.com/questions/55348418/why-is-the-exit-window-button-work-but-the-exit-button-in-the-game-does-not-work/55350638#55350638)  
- [pygame window closes immediatly after opening up](https://stackoverflow.com/questions/63684180/pygame-window-closes-immediatly-after-opening-up)

### Wait and input in application loop

Related Stack Overflow questions:

- [Why is my display not responding while waiting for input?](https://stackoverflow.com/questions/67111782/why-is-my-display-not-responding-while-waiting-for-input/67113040#67113040)  

  📁 **[Minimal example - Input in application loop](../../examples/minimal_examples/pygame_minimal_threading_input.py)**

- [Pygame Window not Responding after few seconds](https://stackoverflow.com/questions/64830453/pygame-window-not-responding-after-few-seconds/64832291#64832291)
- [Why does pygame.display.update() not work if an input is directly followed after it?](https://stackoverflow.com/questions/58794093/why-does-pygame-display-update-not-work-if-an-input-is-directly-followed-after/58812876#58812876)

You cannot use [`input`](https://docs.python.org/3/library/functions.html#input) in the application loop. `input` waits for an input. While the system is waiting for input, the application loop will halt and the game will not respond. Use the `KEYDOWN` event instead of `input`:

```py
run = True
while run:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if pygame.key == pygame.K_1:
                # [...]
            if pygame.key == pygame.K_2:
                # [...]
```

Another option is to get the input in a separate thread.

```py
import pygame
import threading

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

color = "red"
def get_input():
    global color
    color = input('enter color (e.g. blue): ')

input_thread = threading.Thread(target=get_input)
input_thread.start()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window_center = window.get_rect().center
    window.fill('black')
    pygame.draw.circle(window, color, window_center, 100)
    pygame.display.flip()

pygame.quit()
exit()
```

### Delay, wait and sleep

Related Stack Overflow questions:

- [Why doesn't PyGame draw in the window before the delay or sleep?](https://stackoverflow.com/questions/63218889/why-is-pygame-not-showing-text-on-window/63218970#63218970)

- [How to wait some time in pygame?](https://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame)
  📁 **[Minimal example - Display a message for a period of time](../../examples/minimal_examples/pygame_minimal_time_text_message_delay.py)**  
  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MessageDelay](https://replit.com/@Rabbid76/PyGame-MessageDelay#main.py)**

- [How do you make Pygame stop for a few seconds?](https://stackoverflow.com/questions/65083381/how-do-you-make-pygame-stop-for-a-few-seconds/65093284#65093284)

### Game state

Tag: "gamestate", "state of game"

Related Stack Overflow questions:

- [Pygame level/menu states](https://stackoverflow.com/questions/14700889/pygame-level-menu-states)
- [Python/Pygame adding a title screen with a button](https://stackoverflow.com/questions/65845689/python-pygame-adding-a-title-screen-with-a-button/65845819#65845819)  
- [Python : What is the better way to make multiple loops in pygame?](https://stackoverflow.com/questions/57908287/python-what-is-the-better-way-to-make-multiple-loops-in-pygame)  
- [How to add pause mode to Python program](https://stackoverflow.com/questions/56040906/how-to-add-pause-mode-to-python-program/56046554#56046554)  
- [Making a pause screen](https://stackoverflow.com/questions/66765850/making-a-pause-screen/66766232#66766232)  
- [Pygame how to enable and disable a function with the same key?](https://stackoverflow.com/questions/68257536/pygame-how-to-enable-and-disable-a-function-with-the-same-key/68258178#68258178)  

- [In pygame for event.type == ACTIVEEVENT, where is the documentation on what the different event.state and event.gain parameters mean](https://stackoverflow.com/questions/61488114/in-pygame-for-event-type-activeevent-where-is-the-documentation-on-what-the/73275032#73275032)  
  ![In pygame for event.type == ACTIVEEVENT, where is the documentation on what the different event.state and event.gain parameters mean](https://i.stack.imgur.com/ZsY84.gif)

  📁 **[Minimal example - event ACTIVEEVENT](../../examples/minimal_examples/pygame_minimal_event_activevent.py)**

### Recursiveness and restart

Related Stack Overflow questions:

- [In game loop, how do I restart game properly using nested class or loop?](https://stackoverflow.com/questions/74060376/in-game-loop-how-do-i-restart-game-properly-using-nested-class-or-loop/74071133#74071133)  
- [Reset and restart pygame program doesn't work](https://stackoverflow.com/questions/64715107/reset-and-restart-pygame-program-doesnt-work/64715310#64715310)

You've overcomplicated the system. What you are actually doing is recursively instantiating a new `Gui` object and new application loop into an existing `Gui` object and application loop.
If `GameState` is implemented correctly, it should be sufficient to create a new `GameState` object and continue the existing application loop instead of recursively creating a new `Gui` instance:

```py
import board as b

class Gui():
    def __init__(self):
        pygame.init()

        self.gamestate = b.GameState()

    def run(self):

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.gamestate = b.GameState()

            # [...]

if __name__ == '__main__':
    Gui().run()
```

The instruction `self.board = s.start_position` doesn't create a new board object. `self.board` and `s.start_position` refer to the same object. If you change one of the objects, the other object seems to change in the same way since there is only one object.  
Either you need to make a deep copy of the board object when you start the game or you need to reset the object when the game restarts.

A solution might be to use the Python [`copy`](https://docs.python.org/3/library/copy.html) module. `deepcopy` can create a deep copy of an object: 

```py
import copy
```

```py
self.board = copy.deepcopy(s.start_position)
```

Note, not all object can be _deep_ copied. For instance a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) cannot be _deep_ copied.

## Frames per second (Clock)

See [Time, timer event and clock](pygame_time_and_timer_event.md)

## Event loop

### Event loop and handle events

- [How does the for event in pygame.event.get() in python work?](https://stackoverflow.com/questions/68978872/how-does-the-for-event-in-pygame-event-get-in-python-work/69005258#69005258)  
- [PyGame unresponsive display](https://stackoverflow.com/questions/63540062/pygame-unresponsive-display/63540113#63540113)  
- [PyGame window not responding after a few seconds](https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds/61409221#61409221)
- [Why pygame.event.get() returns EventList?](https://stackoverflow.com/questions/61761718/why-pygame-event-get-returns-eventlist/61761995#61761995)
- [How can I limit events to one event per frame(iteration) in pygame](https://stackoverflow.com/questions/64192761/how-can-i-limit-events-to-one-event-per-frameiteration-in-pygame/64192788#64192788)

You have to handle the events in the application loop. See [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get) respectively [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump):

> For each frame of your game, you will need to make some sort of call to the event queue. This ensures your program can internally interact with the rest of the operating system.

### Multiple event loops

- **[Faster version of 'pygame.event.get()'. Why are events being missed and why are the events delayed?](https://stackoverflow.com/questions/58086113/faster-version-of-pygame-event-get-why-are-events-being-missed-and-why-are/58087070#58087070)**

[`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get) get all the messages and remove them from the queue. See the documentation:

> This will get all the messages and remove them from the queue. [...]

If `pygame.event.get()` is called in multiple event loops, only one loop receives the events, but never all loops receive all events. As a result, some events appear to be missed.

Get the events once per frame and use them in multiple loops or pass the list of events to functions and methods where they are handled:

```py
def handle_events(events):
    for event in events:
        # [...]

while run:

    event_list = pygame.event.get()

    # [...]

    # 1st event loop
    for event in event_list:
        # [...]

    # [...]

    # 2nd event loop
    for event in event_list:
        # [...]

    # [...]

    # function which handles events
    handle_events(event_list)
```

### Wait for event

Related Stack Overflow questions:

- [Pygame sprite is too slow](https://stackoverflow.com/questions/59597330/pygame-sprite-is-too-slow/59598060#59598060)

[`pygame.event.wait()`](https://www.pygame.org/docs/ref/event.html#pygame.event.wait) waits for a single event from the queue. If the queue is empty this function will wait until one is created. That makes your game lag.

### Polymorphic event loop

Related Stack Overflow questions:

- [Pygame: how to write event-loop polymorphically](https://stackoverflow.com/questions/60406647/pygame-how-to-write-event-loop-polymorphically/60408967#60408967)

In pygame the event type is an enumerator constant. You have to map this constant to the corresponding class. Use a [`dictionary`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries):

```py
def Exit(event):
    # [...]

def Keydown():
    # [...]

eventhandler = {pygame.QUIT: Exit, pygame.KEYDOWN: Keydown}
```

For a more general approach, the handlers can be managed in a list. So multiple actions can be associated to an event type

```py
def Exit(event):
    # [...]

def Keydown1():
    # [...]

def Keydown2():
    # [...]

eventhandler = {pygame.QUIT: [Exit], pygame.KEYDOWN: [Keydown1, Keydown2]}
```

The events must be delegated to the appropriate actions assigned in the event handler:

```py
while True:
    for event in pygame.event.get():
        if event.type in eventhandler:
            for target in eventhandler[event.type]:
                target(event)
```

📁 **[Minimal example - Polymorphically event handling 1](../../examples/minimal_examples/pygame_minimal_event_polymorph_1.py)**

📁 **[Minimal example - Polymorphically event handling 2](../../examples/minimal_examples/pygame_minimal_event_polymorph_2.py)**
