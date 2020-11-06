[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Event and application loop

See also [Python PyGame Introduction](https://www.pygame.org/docs/tut/PygameIntro.html)

## Application loop

Related Stack Overflow questions:

- [Pygame window freezes when it opens](https://stackoverflow.com/questions/57642415/pygame-window-freezes-when-it-opens/57644255#57644255)
- [Why is my pygame application loop not working properly?](https://stackoverflow.com/questions/60387348/how-to-make-a-camera-for-a-2d-topdown-game-in-pygame/60390374#60390374)
- [Is it possible for a sprite to react to a specific color](https://stackoverflow.com/questions/61703850/is-it-possible-for-a-sprite-to-react-to-a-specific-color/61704072#61704072)

The typical PyGame application loop has to:

- handle the events by either [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump) or [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get).
- update the game states and positions of objects dependent on the input events and time (respectively frames)
- clear the entire display or draw the background
- draw the entire scene (`blit` all the objects)
- update the display by either [`pygame.display.update()`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) or [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip)

:scroll: **[Minimal example - Game loop](../../examples/minimal_examples/pygame_minimal_application_loop.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MinimalApplicationLoop](https://repl.it/@Rabbid76/PyGame-MinimalApplicationLoop#main.py)</kbd>

## Flickering

Related Stack Overflow questions:

- [Pygame Animation is glitching](https://stackoverflow.com/questions/62120723/pygame-animation-is-glitching/62120776?noredirect=1)

## Frames per second (Clock)

See [Time, timer event and clock](pygame_time_and_timer_event.md)

## Event loop

### Event loop and handle events

- [PyGame unresponsive display](https://stackoverflow.com/questions/63540062/pygame-unresponsive-display/63540113?noredirect=1)  
- [PyGame window not responding after a few seconds](https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds/61409221#61409221)
- [Why pygame.event.get() returns EventList?](https://stackoverflow.com/questions/61761718/why-pygame-event-get-returns-eventlist/61761995#61761995)
- [How can I limit events to one event per frame(iteration) in pygame](https://stackoverflow.com/questions/64192761/how-can-i-limit-events-to-one-event-per-frameiteration-in-pygame/64192788#64192788)

You have to handle the events in the application loop. See [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get) respectively [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump):

> For each frame of your game, you will need to make some sort of call to the event queue. This ensures your program can internally interact with the rest of the operating system.

#### Draw and delay, wait and sleep

Related Stack Overflow questions:

- [Why doesn't PyGame draw in the window before the delay or sleep?](https://stackoverflow.com/questions/63218889/why-is-pygame-not-showing-text-on-window/63218970#63218970)
- [How to wait some time in pygame?](https://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame)

#### Input in application loop

Related Stack Overflow questions:

- [Why does pygame.display.update() not work if an input is directly followed after it?](https://stackoverflow.com/questions/58794093/why-does-pygame-display-update-not-work-if-an-input-is-directly-followed-after/58812876#58812876)

### Multiple event loops

- **[Faster version of pygame.event.get()](https://stackoverflow.com/questions/58086113/faster-version-of-pygame-event-get/58087070#58087070)**

[`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get) get all the messages and remove them from the queue. If `pygame.event.get ()` is called in multiple event loops, only one loop receives the events, but never all loops receive all events. As a result, some events appear to be missed.

Get the events once and use them in multiple loops or pass the list or events to functions and methods where they are handled:

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

:scroll: **[Minimal example - Polymorphically event handling 1](../../examples/minimal_examples/pygame_minimal_event_polymorph_1.py)**

:scroll: **[Minimal example - Polymorphically event handling 2](../../examples/minimal_examples/pygame_minimal_event_polymorph_2.py)**
