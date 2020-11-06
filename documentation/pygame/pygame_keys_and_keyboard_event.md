[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Keys and keyboard events

## Keys

## Key representation

## Key state

**What does `pygame.key.get_pressed()` do?**

Related Stack Overflow questions:

- [How to hold a 'key down' in Pygame?](https://stackoverflow.com/questions/63816977/how-to-hold-a-key-down-in-pygame/63817093#63817093)
- [How to get if a key is pressed pygame](https://stackoverflow.com/questions/59830738/how-to-get-if-a-key-is-pressed-pygame/59831073#59831073)
- [“Tuple object not callable” when inspecting the result of pygame.key.get_pressed()](https://stackoverflow.com/questions/62666910/tuple-object-not-callable-when-inspecting-the-result-of-pygame-key-get-pressed/62669811#62669811)

Related Stack Overflow questions:

- [pygame get key pressed as a string](https://stackoverflow.com/questions/59935639/pygame-get-key-pressed-as-a-string/59935886#59935886)  

A unser friendly name of a key can be get by `pygame.key.name()`:

```py
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:

        print(pygame.key.name(event.key))
```

## Keyboard event

**What is `pygame.KEYDOWN`, `pygame.KEYUP`?**

Related Stack Overflow questions:

- [Python Pygame press two direction key and another key to shoot there's no bullet](https://stackoverflow.com/questions/59004524/python-pygame-press-two-direction-key-and-another-key-to-shoot-theres-no-bullet/59005776#59005776)
- [Getting Pygame keyboard input and check if it's a number](https://stackoverflow.com/questions/64124050/getting-pygame-keyboard-input-and-check-if-its-a-number/64124342#64124342)
- [Problem when using keyboard commands in pygame](https://stackoverflow.com/questions/58299480/problem-when-using-keyboard-commands-in-pygame/58307655#58307655)
- [How to get a variable keyboard input in pygame?](https://stackoverflow.com/questions/63449626/how-to-get-a-variable-keyboard-input-in-pygame/63449886#63449886)
- [Pygame keys convention](https://stackoverflow.com/questions/64651122/pygame-keys-convention/64651187#64651187)

[`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html) returns a list with the state of all keyboard buttons. This is not intended to get the key of a keyboard event. The key that was pressed can be obtained from the `key` attribute of the [`pygame.event.Event`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object:

```py
if event.type == pg.KEYDOWN:
    if event.key == pg.K_a:
        # [...]
```

`unicode` contains a single character string that is the fully translated character:

```py
if event.type == pg.KEYDOWN:
    if event.unicode == 'a':
        # [...]
```

See also [`pygame.event`](https://www.pygame.org/docs/ref/event.html) module and [pygame.key](https://www.pygame.org/docs/ref/key.html).

If you press <kbd>UP</kbd> + <kbd>LEFT</kbd> + <kbd>SPACE</kbd> then the <kbd>SPACE</kbd> key doesn't appear to be pressed immediately. You've to release the <kbd>UP</kbd> or <kbd>LEFT</kbd> key to get the `pygame.KEYDOWN` event for <kbd>SPACE</kbd>.  

This is a known bug in pygame and doesn't seem to be solved yet: [Incorrect handling of pressed keys #235](https://github.com/pygame/pygame/issues/235).

Sadly even [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) doesn't state the <kbd>SPACE</kbd> key in this case, so I can't even think a workaround.

While `pygame.K_f` is a key enumerator constant (see [`pygame.key`](https://www.pygame.org/docs/ref/key.html)) the content of `event.type` is event enumerator constant (see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)).  
If you want to determine if a certain key is pressed, the you've to verify if the event type is `pygame.KEYDOWN` (or `pygame.KEYUP` for button release) and if the `.key` attribute of the event is equal the key enumerator. e.g.:

```py
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        self.quit()

    # [...]

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_f:
            # [...]
```

## Detecting key states and events

### Difference between key state key event

Related Stack Overflow questions:

- [How to get keyboard input in pygame?](https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame/64494842#64494842)
  [How can I make a sprite move when key is held down](https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down)

  :scroll: **[minimal example - Move object with keys](../../examples/minimal_examples/pygame_minimal_move_object.py)**

- [What all things happens inside pygame when I press a key? When to use pygame.event==KEYDOWN](https://stackoverflow.com/questions/63050139/what-all-things-happens-inside-pygame-when-i-press-a-key-when-to-use-pygame-eve/63056690#63056690)
- [PyGame press two buttons at the same time](https://stackoverflow.com/questions/59181962/pygame-press-two-buttons-at-the-same-time/59182228#59182228)
- [Pygame Keys Activating in Multiple Frames](https://stackoverflow.com/questions/64540381/pygame-keys-activating-in-multiple-frames/64540554#64540554)

[`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) returns a list with the state of each key. If a key is held down, the state for the key is `True`, otherwise `False`. Use [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) to evaluate the current state of a button and get continuous movement:

```py
while True:

    pressed_key= pygame.key.get_pressed()
    x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
```

The keyboard events (see [pygame.event](https://www.pygame.org/docs/ref/event.html) module) occur only once when the state of a key changes. The `KEYDOWN` event occurs once every time a key is pressed. `KEYUP` occurs once every time a key is released. Use the keyboard events for a single action or a step-by-step movement

```py
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed
            if event.key == pygame.K_RIGHT:
                x += speed
            if event.key == pygame.K_UP:
                y -= speed
            if event.key == pygame.K_DOWN:
                y += speed
```

### When is the key state used and when the keyboard event

When does it make sense to use keyboard events (`pygame.KEYDOWN`, `pygame.KEYUP` see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)), and when is it better to get the state of the keys ([`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html))?

Related Stack Overflow questions:

- [Python only running while loop once](https://stackoverflow.com/questions/59706667/python-only-running-while-loop-once/59706711#59706711)
- [I want my character to do something as long as I'm holding a button, then go back to normal once I let go of the button](https://stackoverflow.com/questions/60741355/i-want-my-character-to-do-something-as-long-as-im-holding-a-button-then-go-bac/60742556#60742556)
- [how to control snake with only two keys i.e left and right](https://stackoverflow.com/questions/61862293/how-to-control-snake-with-only-two-keys-i-e-left-and-right/61863664#61863664)
- [how to drop a bomb in character position in a pygame game](https://stackoverflow.com/questions/62066092/how-to-drop-a-bomb-in-character-position-in-a-pygame-game/62067605#62067605)
- [how to make rectangle “sprint”](https://stackoverflow.com/questions/64209885/how-to-make-rectangle-sprint/64209944#64209944)

:scroll: **[minimal example - Move object with keys](../../examples/minimal_examples/pygame_minimal_move_object.py)**

:scroll: **[minimal example - Move object with keys limit it to the window borders](../../examples/minimal_examples/pygame_minimal_move_object_limit_window.py)**

[How do I get the size (width x height) of my pygame window](https://i.stack.imgur.com/xMMCz.gif)

:scroll: **[minimal example - Move object fast when key is hit twice](../../examples/minimal_examples/pygame_minimal_move_object_fast_on_key_twice.py)**

:scroll: **[minimal example - Move object fast when key is in opposite direction is hit](../../examples/minimal_examples/pygame_minimal_move_object_slow_on_opposite_key.py)**

### Shoot bullet

Related Stack Overflow questions:

- [How can i shoot a bullet with space bar?](https://stackoverflow.com/questions/59687250/how-can-i-shoot-a-bullet-with-space-bar/59689297#59689297)  
  ![How can i shoot a bullet with space bar?](https://i.stack.imgur.com/2sp5D.gif)
- [How do I stop more than 1 bullet firing at once?](https://stackoverflow.com/questions/60122492/how-do-i-stop-more-than-1-bullet-firing-at-once/60125448#60125448)  
  ![How do I stop more than 1 bullet firing at once?](https://i.stack.imgur.com/1DY2O.gif)
