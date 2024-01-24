[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"You should name a variable using the same care with which you name a first-born child."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Keys and keyboard events

Related Stack Overflow questions:

- **[How to get keyboard input in pygame?](https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame/64494842#64494842)**  
  ![How to get keyboard input in pygame?](https://i.stack.imgur.com/S24dj.gif)

  📁 **[minimal example - Move object with keys](../../examples/minimal_examples/pygame_minimal_move_object.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ContinuousMovement](https://replit.com/@Rabbid76/PyGame-ContinuousMovement#main.py)**

- **[How can I make a sprite move when key is held down](https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down)**  

  📁 **[minimal example - Move object with keys](../../examples/minimal_examples/pygame_minimal_move_object.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ContinuousMovement](https://replit.com/@Rabbid76/PyGame-ContinuousMovement#main.py)**

  ![How can I make a sprite move when key is held down](https://i.stack.imgur.com/S24dj.gif)

  📁 **[minimal example - Move object with keys limit it to the window borders](../../examples/minimal_examples/pygame_minimal_move_object_limit_window.py)**  
  📁 **[minimal example - Move object fast when key is hit twice](../../examples/minimal_examples/pygame_minimal_move_object_fast_on_key_twice.py)**  
  📁 **[minimal example - Move object fast when key is in opposite direction is hit](../../examples/minimal_examples/pygame_minimal_move_object_slow_on_opposite_key.py)**  

- [How to check if keyboard button is getting spammed and add a cool down on before it can be pressed again](https://stackoverflow.com/questions/56615781/how-to-check-if-keyboard-button-is-getting-spammed-and-add-a-cool-down-on-before/56617202#56617202)

- [I have a function that detects if i press a key in pygame, but it only detects one key?](https://stackoverflow.com/questions/73953058/i-have-a-function-that-detects-if-i-press-a-key-in-pygame-but-it-only-detects-o/73953116#73953116)

  📁 **[minimal example - Move object with keys continuous or step by step.py](../../examples/minimal_examples/pygame_minimal_move_object_continuous_or_step.py)**  

- [How can I allow keyboard inputs to override each other in pygame?](https://stackoverflow.com/questions/73937281/how-can-i-allow-keyboard-inputs-to-override-each-other-in-pygame/73937309#73937309)

  📁 **[minimal example - Move object, key queue](../../examples/minimal_examples/pygame_minimal_move_object_3.py)**

- [Two keypresses processed in each frame (pygame snake game)](https://stackoverflow.com/questions/74249252/two-keypresses-processed-in-each-frame-pygame-snake-game/74326162#74326162)  
  ![Two keypresses processed in each frame (pygame snake game)](https://i.stack.imgur.com/XQams.gif)

When does it make sense to use keyboard events (`pygame.KEYDOWN`, `pygame.KEYUP` see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)), and when is it better to get the state of the keys ([`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html))?

[`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) returns a sequence with the state of each key. If a key is held down, the state for the key is `1`, otherwise `0`. It is a snapshot of the keys at that very moment The new state of the keys must be retrieved continuously in each frame. So you can calculate the resulting movement when 2 keys are pressed with `keys[pygame.K_d] - keys[pygame.K_a]` and `keys[pygame.K_s] - keys[pygame.K_w]`. Use [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) to evaluate the current state of a button and get continuous movement.  

```py
while True:

    keys = pygame.key.get_pressed()
    x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
```

The keyboard events (see [pygame.event](https://www.pygame.org/docs/ref/event.html) module) occur only once when the state of a key changes. The `KEYDOWN` event occurs once every time a key is pressed. `KEYUP` occurs once every time a key is released. Use the keyboard events for a single action like jumping or spawning a bullet or a step-by-step movement.

Single Action:


```py
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullet()
```

Step-by-step movement:

```py
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

## Shoot bullet

Related Stack Overflow questions:

- [How can i shoot a bullet with space bar?](https://stackoverflow.com/questions/59687250/how-can-i-shoot-a-bullet-with-space-bar/59689297#59689297)  
  ![How can i shoot a bullet with space bar?](https://i.stack.imgur.com/2sp5D.gif)

  📁 **[minimal example - Sustained fire](../../examples/minimal_examples/pygame_minimal_shoot_bullet_sustained_fire.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ShootBulletSustainedFire](https://replit.com/@Rabbid76/PyGame-ShootBulletSustainedFire#main.py)**

- [How do I stop more than 1 bullet firing at once?](https://stackoverflow.com/questions/60122492/how-do-i-stop-more-than-1-bullet-firing-at-once/60125448#60125448)  
  ![How do I stop more than 1 bullet firing at once?](https://i.stack.imgur.com/W6lzh.gif)

  📁 **[minimal example - Shoot bullet](../../examples/minimal_examples/pygame_minimal_shoot_bullet.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ShootBullet](https://replit.com/@Rabbid76/PyGame-ShootBullet#main.py)**

- [Pygame: problems with shooting in Space Invaders](https://stackoverflow.com/questions/65759929/pygame-problems-with-shooting-in-space-invaders/65759972#65759972)  
  ![Pygame: problems with shooting in Space Invaders](https://i.stack.imgur.com/bSRed.gif)

- [Pygame How to check for second press of a key](https://stackoverflow.com/questions/65832446/pygame-how-to-check-for-second-press-of-a-key/65832768#65832768)  
  ![Pygame How to check for second press of a key](https://i.stack.imgur.com/vl3gn.gif)

The general approach to firing bullets is to store the positions of the bullets in a list (`bullet_list`). When a bullet is fired, add the bullet's starting position (`[start_x, start_y]`) to the list. The starting position is the position of the object (player or enemy) that fires the bullet. Use a `for`-loop to iterate through all the bullets in the list. Move position of each individual bullet in the loop. Remove a bullet from the list that leaves the screen (`bullet_list.remove(bullet_pos)`). For this reason, a copy of the list (`bullet_list[:]`) must be run through (see [How to remove items from a list while iterating?](https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating)). Use another ` for`-loop to `blit` the remaining bullets on the screen:

```py
bullet_list = []

while run == True:
    # [...]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_list.append([start_x, start_y])

    for bullet_pos in bullet_list[:]:
        bullet_pos[0] += move_bullet_x
        bullet_pos[1] += move_bullet_y
        if not screen.get_rect().colliderect(bullet_image.get_rect(center = bullet_pos))
            bullet_list.remove(bullet_pos)

    # [...]

    for bullet_pos in bullet_list[:]
        screen.blit(bullet_image, bullet_image.get_rect(center = bullet_pos))

    # [...]
```

## Key state

**What does `pygame.key.get_pressed()` do?**

Related Stack Overflow questions:

- [Why use (bitwise) & when handling keyboard events involving multiple keys?](https://stackoverflow.com/questions/65219618/why-use-bitwise-when-handling-keyboard-events-involving-multiple-keys/65219714#65219714)
- [Pygame's pygame.event.get()'s key value is a ridiculous number as of today, why?](https://stackoverflow.com/questions/66665341/pygames-pygame-event-gets-key-value-is-a-ridiculous-number-as-of-today-why/66667449#66667449)

## Key repeat

Related Stack Overflow questions:

- [Detect single key press using key.get_pressed()](https://stackoverflow.com/questions/65266365/detect-single-key-press-using-key-get-pressed/65267063#65267063)  
- [Why is pygame.KEYUP event triggering when the key has not been released?](https://stackoverflow.com/questions/53525617/why-is-pygame-keyup-event-triggering-when-the-key-has-not-been-released/65658666#65658666)  

## Keyboard event

**What is `pygame.KEYDOWN`, `pygame.KEYUP`?**

Related Stack Overflow questions:

- **[Getting Pygame keyboard input and check if it's a number](https://stackoverflow.com/questions/64124050/getting-pygame-keyboard-input-and-check-if-its-a-number/64124342#64124342)**
- [Python Pygame press two direction key and another key to shoot there's no bullet](https://stackoverflow.com/questions/59004524/python-pygame-press-two-direction-key-and-another-key-to-shoot-theres-no-bullet/59005776#59005776)
- [How to get a variable keyboard input in pygame?](https://stackoverflow.com/questions/63449626/how-to-get-a-variable-keyboard-input-in-pygame/63449886#63449886)

The keyboard events `KEYDOWN` and `KEYUP` (see [pygame.event](https://www.pygame.org/docs/ref/event.html) module) create a [`pygame.event.Event`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object with additional attributes. The key that was pressed can be obtained from the `key` attribute (e.g. `K_RETURN `, `K_a`) and the `mod` attribute contains a bitset with additional modifiers (e.g. `KMOD_LSHIFT`). The `unicode` attribute provides the Unicode representation of the keyboard input.  
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

If you press **UP** + **LEFT** + **SPACE** then the **SPACE** key doesn't appear to be pressed immediately. You've to release the **UP** or **LEFT** key to get the `pygame.KEYDOWN` event for **SPACE**.  

This is a known bug in pygame and doesn't seem to be solved yet: [Incorrect handling of pressed keys #235](https://github.com/pygame/pygame/issues/235).

Sadly even [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) doesn't state the **SPACE** key in this case, so I can't even think a workaround.

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


## Key representation

Related Stack Overflow questions:

- [pygame get key pressed as a string](https://stackoverflow.com/questions/59935639/pygame-get-key-pressed-as-a-string/59935886#59935886)  

A user friendly name of a key can be get by `pygame.key.name()`:

```py
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:

        print(pygame.key.name(event.key))
```
