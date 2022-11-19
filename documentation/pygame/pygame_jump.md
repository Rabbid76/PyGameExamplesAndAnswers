[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"You must not fool yourself and you are the easiest person to fool."  
Richard P. Feynman

---

# Jump

Related Stack Overflow questions:

- **[How to make a character jump in Pygame?](https://stackoverflow.com/questions/70591591/how-to-make-a-character-jump-in-pygame/70591592#70591592)**  
  ![How to make a character jump in Pygame?](https://i.stack.imgur.com/6NReI.gif)
  ![How to make a character jump in Pygame?](https://i.stack.imgur.com/phpoF.gif)

- **[How can I do a double jump in pygame?](https://stackoverflow.com/questions/67667103/how-can-i-do-a-double-jump-in-pygame/67667585#67667585)**  
  ![How can I do a double jump in pygame?](https://i.stack.imgur.com/9ICi5.gif)  

- **[How to do a variable jump height based on how long key is held in Pygame](https://stackoverflow.com/questions/68839727/how-to-do-a-variable-jump-height-based-on-how-long-key-is-held-in-pygame/68843102#68843102)**  
  ![How to do a variable jump height based on how long key is held in Pygame](https://i.stack.imgur.com/jhf3z.gif)

- [python, pygame - jumping too fast?](https://stackoverflow.com/questions/58474204/python-pygame-jumping-too-fast/58474280#58474280)  
  ![python, pygame - jumping too fast?](https://i.stack.imgur.com/gWHCT.gif)

- [How does this algorithm make the character jump in pygame?](https://stackoverflow.com/questions/65873880/how-does-this-algorithm-make-the-character-jump-in-pygame/65874132#65874132)     

**How to make a character jump in Pygame?**

To make a character jump you have to use the [`KEYDOWN`](https://www.pygame.org/docs/ref/event.html) event, but not [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed). `pygame.key.get_pressed ()` is for continuous movement when a key is held down. The keyboard events are used to trigger a single action or to start an animation such as a jump. See alos [How to get keyboard input in pygame?](https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame/64494842#64494842)  

[`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) returns a sequence with the state of each key. If a key is held down, the state for the key is `True`, otherwise `False`. Use [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) to evaluate the current state of a button and get continuous movement.

```py
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jump = True
```

Use [`pygame.time.Clock`](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) (*"This method should be called once per frame."*) you control the frames per second and thus the game speed and the duration of the jump.

```py
clock = pygame.time.Clock()
while True:
   clock.tick(100)
```

The jumping should be independent of the player's movement or the general flow of control of the game. Therefore, the jump animation in the application loop must be executed in parallel to the running game.

When you throw a ball or something jumps, the object makes a parabolic curve. The object gains height quickly at the beginning, but this slows down until the object begins to fall faster and faster again. The change in height of a jumping object can be described with the following sequence:

```lang-none
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
```

Such a series can be generated with the following algorithm (`y` is the y coordinate of the object):

```py
jumpMax = 10
if jump:
    y -= jumpCount
    if jumpCount > -jumpMax:
        jumpCount -= 1
    else:
        jump = False 
```

:scroll: **[Minimal example - Jump (integral)](../../examples/minimal_examples/pygame_minimal_jump_1.py)**  
**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-Jump](https://replit.com/@Rabbid76/PyGame-Jump#main.py)**

:scroll: **[Minimal example - Jump (floating point)](../../examples/minimal_examples/pygame_minimal_jump_3.py)**  
**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-JumpFloat](https://replit.com/@Rabbid76/PyGame-JumpFloat#main.py)**

A more sophisticated approach is to define constants for the  gravity and player's acceleration as the player jumps:

```py
acceleration = 10
gravity = 0.5
```

The acceleration exerted on the player in each frame is the gravity constant, if the player jumps then the acceleration changes to the "jump" acceleration for a single frame:

```py
acc_y = gravity
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: 
        if vel_y == 0 and event.key == pygame.K_SPACE:
            acc_y = -acceleration
```

In each frame the vertical velocity is changed depending on the acceleration and the y-coordinate is changed depending on the velocity. When the player touches the ground, the vertical movement will stop:

```py
vel_y += acc_y
y += vel_y
if y > ground_y:
    y = ground_y
    vel_y = 0
    acc_y = 0
```

:scroll: **[Minimal example - Jump with acceleration](../../examples/minimal_examples/pygame_minimal_jump_2.py)**  
**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-JumpAcceleration](https://replit.com/@Rabbid76/Pygame-JumpAcceleration#main.py)**
