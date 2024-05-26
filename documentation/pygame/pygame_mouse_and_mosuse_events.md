[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"I was born not knowing and have had only a little time to change that here and there."  
Richard P. Feynman

---

# Mouse

[MOUSEBUTTONUP vs mouse.get_pressed()](https://stackoverflow.com/questions/65914897/mousebuttonup-vs-mouse-get-pressed/65914980#65914980)

## Mouse and mouse event

Related Stack Overflow questions:

- [Pygame mouse clicking detection](https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684)  
  ![Pygame mouse clicking detection](https://i.sstatic.net/mW6vv.gif)![Pygame mouse clicking detection](https://i.sstatic.net/UJVKi.gif)  

- [How do I add a border to a sprite when the mouse hovers over it, and delete it after the mouse stops?0](https://stackoverflow.com/questions/70384004/how-do-i-add-a-border-to-a-sprite-when-the-mouse-hovers-over-it-and-delete-it-a/70384279#70384279)  
  ![How do I add a border to a sprite when the mouse hovers over it, and delete it after the mouse stops?](https://i.sstatic.net/DQdGr.gif)

  📁 **[minimal example - Hover and delete](../../examples/minimal_examples/pygame_minimal_sprite_mouse_hover_3.py)**

- [How can I add an image or icon to a button rectangle in Pygame?](https://stackoverflow.com/questions/64990710/how-can-i-add-an-image-or-icon-to-a-button-rectangle-in-pygame/64990819#64990819)  
  ![How can I add an image or icon to a button rectangle in Pygame?](https://i.sstatic.net/24ns9.gif)![How can I add an image or icon to a button rectangle in Pygame?](https://i.sstatic.net/UEIde.gif)

- [How to detect touch screen clicks in python?](https://stackoverflow.com/questions/69024021/how-to-detect-touch-screen-clicks-in-python/69032776#69032776)  
  ![How to detect touch screen clicks in python?](https://i.sstatic.net/3ENNw.gif)  

  📁 **[minimal example - Detect mouse touch](../../examples/minimal_examples/pygame_minimal_mouse_touch.py)**

- [Detect Mouse Scroll](https://stackoverflow.com/questions/72858633/detect-mouse-scroll/72858761#72858761)  
- [How to distinguish left click , right click mouse clicks in pygame?](https://stackoverflow.com/questions/34287938/how-to-distinguish-left-click-right-click-mouse-clicks-in-pygame)  
- [Pygame - Mouse clicks not getting detected](https://stackoverflow.com/questions/64284668/python-w-pygame-mouse-detection-isnt-working)
- [mouse.get_pressed() inconsistent/returning (0, 0, 0)](https://stackoverflow.com/questions/63970977/mouse-get-pressed-inconsistent-returning-0-0-0/63971125#63971125)  
- [Pygame mouse position not precise enough to rotate the 3D scene](https://stackoverflow.com/questions/71593670/pygame-mouse-position-not-precise-enough-to-rotate-the-3d-scene/74329544#74329544)  

The [`pygame.event.Event`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object has two attributes that provide information about the mouse event. `pos` is a tuple that stores the position that was clicked. `button` stores the button that was clicked. Each mouse button is associated a value. For instance the value of the attributes is 1, 2, 3, 4, 5 for the left mouse button, middle mouse button, right mouse button, mouse wheel up respectively mouse wheel down. When multiple keys are pressed, multiple mouse button events occur. Further explanations can be found in the documentation of the module [`pygame.event`](https://www.pygame.org/docs/ref/event.html).

📁 **[minimal example - Detect mouse button click events](../../examples/minimal_examples/pygame_minimal_mouse_event_1.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseEvents](https://replit.com/@Rabbid76/PyGame-MouseEvents#main.py)**

📁 **[minimal example - Detect click on Sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_click.py)**

![Pygame - Mouse clicks not getting detected](https://i.sstatic.net/mW6vv.gif)

The coordinates which are returned by [`pygame.mouse.get_pos()`](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed) are evaluated when the events are handled. You need to handle the events by either [`pygame.event.pump()`](https://www.pygame.org/docs/ref/event.html#pygame.event.pump) or [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get).

See [`pygame.event.get()`](https://www.pygame.org/docs/ref/event.html#pygame.event.get):

> For each frame of your game, you will need to make some sort of call to the event queue. This ensures your program can internally interact with the rest of the operating system.

The current position of the mouse can be determined via [`pygame.mouse.get_pos()`](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos). The return value is a tuple that represents the x and y coordinates of the mouse cursor. [`pygame.mouse.get_pressed()`](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed) returns a list of Boolean values ​​that represent the state (`True` or `False`) of all mouse buttons. The state of a button is `True` as long as a button is held down. When multiple buttons are pressed, multiple items in the list are `True`. The 1st, 2nd and 3rd elements in the list represent the left, middle and right mouse buttons. If a specific button is pressed, this can be evaluated by subscription:

```py
buttons = pygame.mouse.get_pressed()
if buttons[0]:
    print("left button pressed")
```

If any button is pressed, this can be evaluated with the [`any`](https://docs.python.org/3/library/functions.html#any) function:

```py
buttons = pygame.mouse.get_pressed()
if any(buttons):
    print("button pressed")
```

Further explanations can be found in the documentation of the module [`pygame.mouse`](https://www.pygame.org/docs/ref/mouse.html).

📁 **[minimal example - Detect mouse button states](../../examples/minimal_examples/pygame_minimal_mouse_states_1.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseStates](https://replit.com/@Rabbid76/PyGame-MouseStates#main.py)**

📁 **[minimal example - Detect Sprite on hover](../../examples/minimal_examples/pygame_minimal_sprite_mouse_hover.py)**

![Pygame - Mouse clicks not getting detected](https://i.sstatic.net/UJVKi.gif)

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
            print("clicked", event.button)
        if event.type == pygame.MOUSEBUTTONUP:
            print("released", event.button)

    pygame.display.update()
```

While `pygame.mouse.get_pressed()` returns the current state of the buttons, the  `MOUSEBUTTONDOWN` and `MOUSEBUTTONUP` occurs only once a button is pressed.

## Mouse cursor

Related Stack Overflow questions:

- [Image lagging while blitting on top of mouse rect](https://stackoverflow.com/questions/56961186/image-lagging-while-blitting-on-top-of-mouse-rect/56976454#56976454)  
- [Pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) is causing errors](https://stackoverflow.com/questions/65383098/pygame-mouse-set-cursor8-8-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-is-caus/65383209#65383209)  

📁 **[Minimal example - Image on mouse cursor](../../examples/minimal_examples/pygame_minimal_mouse_cursor_image.py)**

## Change mouse position

Related Stack Overflow questions:

- [Make cursor unable to move through sprite PyGame](https://stackoverflow.com/questions/54509869/make-cursor-unable-to-move-through-sprite-pygame/54511823#54511823)  
  ![Make cursor unable to move through sprite PyGame](https://i.sstatic.net/QAJAL.gif)

  📁 **[Minimal example - Block mouse cursor by obstacle](../../examples/minimal_examples/pygame_minimal_mouse_cursor_block_by_obstacle.py)**

## Mouse Drag

Related Stack Overflow questions:

- [pygame rect is slipping out of the mouse curser](https://stackoverflow.com/questions/74002619/pygame-rect-is-slipping-out-of-the-mouse-curser/74002649#74002649)  
  ![pygame rect is slipping out of the mouse curser](https://i.sstatic.net/2vVwB.gif)  
- [Drag multiple sprites with different “update ()” methods from the same Sprite class in Pygame](https://stackoverflow.com/questions/64419223/drag-multiple-sprites-with-different-update-methods-from-the-same-sprite-cl/64456959#64456959)  
  ![Drag multiple sprites with different “update ()” methods from the same Sprite class in Pygame](https://i.sstatic.net/BaFzb.gif)
- [How can I drag more than 2 images in PyGame?](https://stackoverflow.com/questions/64592440/how-can-i-drag-more-than-2-images-in-pygame/64592600#64592600)  
  ![How can I drag more than 2 images in PyGame?](https://i.sstatic.net/Cmxd9.gif)
- [How to drag multiple images in PyGame?](https://stackoverflow.com/questions/64504480/how-to-drag-multiple-images-in-pygame/64504767#64504767)  
  ![How to drag multiple images in PyGame?](https://i.sstatic.net/mOnHo.gif)
- [how to adapt the second code to put in the first?](https://stackoverflow.com/questions/64880962/how-to-adapt-the-second-code-to-put-in-the-first/64881500#64881500)  
  ![how to adapt the second code to put in the first?](https://i.sstatic.net/f3aOb.gif)  
  ![how to adapt the second code to put in the first?](https://i.sstatic.net/ZBvDp.gif)  
  ![how to adapt the second code to put in the first?](https://i.sstatic.net/M1k3p.gif)
- [Dragging object along x-axis in pygame](https://stackoverflow.com/questions/61781533/dragging-object-along-x-axis-in-pygame/61781683#61781683)  
  ![Dragging object along x-axis in pygame](https://i.sstatic.net/l9IOr.gif)
- [How to drag an object around the screen in pygame?](https://stackoverflow.com/questions/64241742/how-to-drag-an-object-around-the-screen-in-pygame/64249660#64249660)  
  ![How to drag an object around the screen in pygame?](https://i.sstatic.net/Qgh20.gif)

📁 **[Minimal example - Drag rectangle](../../examples/minimal_examples/pygame_minimal_mouse_drag_rectangle.py)**

📁 **[Minimal example - Drag Sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_drag.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseDragSimple](https://replit.com/@Rabbid76/PyGame-MouseDragSimple#main.py)**

- [Drawing square colour stored in a list of tuples?](https://stackoverflow.com/questions/69828786/drawing-square-colour-stored-in-a-list-of-tuples/69828913#69828913)  
  ![Drawing square colour stored in a list of tuples?](https://i.sstatic.net/e7ecp.gif)

   📁 **[Minimal example - Drag pieces](../../examples/minimal_examples/pygame_minimal_mouse_drag_pieces.py)**

### Mouse drag and rotate

Related Stack Overflow questions:

- [how rotate the images with keyboards?](https://stackoverflow.com/questions/64862405/how-rotate-the-images-with-keyboards/64862779#64862779)  
  ![how rotate the images with keyboards?](https://i.sstatic.net/aUlEe.gif)

### Mouse speed

Related Stack Overflow questions:

- [How can i calculate the mouse speed with Pygame?](https://stackoverflow.com/questions/66662219/how-can-i-calculate-the-mouse-speed-with-pygame/66662396#66662396)

### Touch input

Related Stack Overflow questions:

- [How to use Pygame touch events in a mobile game?](https://stackoverflow.com/questions/69593109/how-to-use-pygame-touch-events-in-a-mobile-game/69593913#69593913)

📁 **[Minimal example - Touch event](../../examples/minimal_examples/pygame_minimal_touch_event_1.py)**

- [Is it possible to drag two sprites independently using FINGERDOWN in pygame on mobile?](https://stackoverflow.com/questions/74891922/is-it-possible-to-drag-two-sprites-independently-using-fingerdown-in-pygame-on-m/74919117#74919117)
