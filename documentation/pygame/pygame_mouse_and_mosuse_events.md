[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Mouse

## Mouse and mouse event

Related Stack Overflow questions:

- [Pygame mouse clicking detection](https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684)
- [How to distinguish left click , right click mouse clicks in pygame?](https://stackoverflow.com/questions/34287938/how-to-distinguish-left-click-right-click-mouse-clicks-in-pygame)
- [Pygame - Mouse clicks not getting detected](https://stackoverflow.com/questions/64284668/python-w-pygame-mouse-detection-isnt-working)
- [mouse.get_pressed() inconsistent/returning (0, 0, 0)](https://stackoverflow.com/questions/63970977/mouse-get-pressed-inconsistent-returning-0-0-0/63971125#63971125)

The `MOUSEBUTTONDOWN` event occurs once when you click the mouse button and the `MOUSEBUTTONUP` event occurs once when the mouse button is released. The [`pygame.event.Event()`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object has two attributes that provide information about the mouse event. `pos` is a tuple that stores the position that was clicked. Each mouse button is associated a value. For instance the value of the attributes is 1, 2, 3, 4, 5 for the left mouse button, middle mouse button, right mouse button, mouse wheel up respectively mouse wheel down. When multiple keys are pressed, multiple mouse button events occur. Further explanations can be found in the documentation of the module [`pygame.event`](https://www.pygame.org/docs/ref/event.html).

:scroll: **[minimal example - Detect mouse button click events](../../examples/minimal_examples/pygame_minimal_mouse_event_1.py)**

:scroll: **[minimal example - Detect click on Sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_click.py)**

![Pygame - Mouse clicks not getting detected](https://i.stack.imgur.com/mW6vv.gif)

The coordinates which are returned by [`pygame.mouse.get_pressed()`](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed) are evaluated when the events are handled. You need to handle the events by either [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump) or [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get).

See [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get):

> For each frame of your game, you will need to make some sort of call to the event queue. This ensures your program can internally interact with the rest of the operating system.

The current position of the mouse can be determined via [`pygame.mouse.get_pos()`](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos). The return value is a tuple that represents the x and y coordinates of the mouse cursor. [`pygame.mouse.get_pressed()`](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed) returns a list of Boolean values ​​that represent the state (`True` or `False`) of all mouse buttons. The state of a button is `True` as long as a button is held down. When multiple buttons are pressed, multiple items in the list are `True`. The 1st, 2nd and 3rd elements in the list represent the left, middle and right mouse buttons. If a specific button is pressed, this can be evaluated by subscription:

```py
buttons = pygame.mouse.get_pressed()
if buttons[0]:
    print("left button pressed")
```

If any button is pressed, this can be evaluated with the [`any`](https://docs.python.org/3/library/functions.html#any) function:

Further explanations can be found in the documentation of the module [`pygame.mouse`](https://www.pygame.org/docs/ref/mouse.html).

```py
buttons = pygame.mouse.get_pressed()
if any(buttons):
    print("button pressed")
```

:scroll: **[minimal example - Detect mouse button states](../../examples/minimal_examples/pygame_minimal_mouse_states_1.py)**

:scroll: **[minimal example - Detect Sprite on hover](../../examples/minimal_examples/pygame_minimal_sprite_mouse_hover.py)**

![Pygame - Mouse clicks not getting detected](https://i.stack.imgur.com/UJVKi.gif)

For instance:

```py
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
  
    buttons = pygame.mouse.get_pressed()

    # if buttons[0]:  # for the left mouse button
    if any(buttons):  # for any mouse button
        print("You are clicking")
    else:
        print("You released")

    pygame.display.update()
```

If you just want to detect when the mouse button is pressed respectively released, then you have to implement the `MOUSEBUTTONDOWN` and `MOUSEBUTTONUP` (see [`pygame.event`](https://www.pygame.org/docs/ref/event.html) module):

```py
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("You are clicking", event.button)
        if event.type == pygame.MOUSEBUTTONUP:
            print("You released", event.button)

    pygame.display.update()
```

While `pygame.mouse.get_pressed()` returns the current state of the buttons, the  `MOUSEBUTTONDOWN` and `MOUSEBUTTONUP` occurs only once a button is pressed.

## Mouse cursor

Related Stack Overflow questions:

- [Image lagging while blitting on top of mouse rect](https://stackoverflow.com/questions/56961186/image-lagging-while-blitting-on-top-of-mouse-rect/56976454#56976454)

:scroll: **[Minimal example - Image on mouse cursor](../../examples/minimal_examples/pygame_minimal_mouse_cursor_image.py)**

## Change mouse position

Related Stack Overflow questions:

- [Make cursor unable to move through sprite PyGame](https://stackoverflow.com/questions/54509869/make-cursor-unable-to-move-through-sprite-pygame/54511823#54511823)  
  ![Make cursor unable to move through sprite PyGame](https://i.stack.imgur.com/QAJAL.gif)

  :scroll: **[Minimal example - Block mouse cursor by obstacle](../../examples/minimal_examples/pygame_minimal_mouse_cursor_block_by_obstacle.py)**

## Mouse Drag

Related Stack Overflow questions:

- [Dragging object along x-axis in pygame](https://stackoverflow.com/questions/61781533/dragging-object-along-x-axis-in-pygame/61781683#61781683)
  ![Dragging object along x-axis in pygame](https://i.stack.imgur.com/l9IOr.gif)
- [How to drag an object around the screen in pygame?](https://stackoverflow.com/questions/64241742/how-to-drag-an-object-around-the-screen-in-pygame/64249660#64249660)  
  ![How to drag an object around the screen in pygame?](https://i.stack.imgur.com/Qgh20.gif)
- [how to move multiple images in pygame?](https://stackoverflow.com/questions/64504480/how-to-move-multiple-images-in-pygame/64504767#64504767)  
  ![how to move multiple images in pygame?](https://i.stack.imgur.com/mOnHo.gif)
- [how i can make this with four images?](https://stackoverflow.com/questions/64592440/how-i-can-make-this-with-four-images/64592600#64592600)  
  ![how i can make this with four images?](https://i.stack.imgur.com/Cmxd9.gif)

:scroll: **[Minimal example - Drag rectangle](../../examples/minimal_examples/pygame_minimal_mouse_drag_rectangle.py)**

:scroll: **[Minimal example - Drag Sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_drag.py)**
