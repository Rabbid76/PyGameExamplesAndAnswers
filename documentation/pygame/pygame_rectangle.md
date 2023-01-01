[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Of course bad code can be cleaned up. But it’s very expensive."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Rectangle

## Rectangle attributes

Related Stack Overflow questions:

- [AttributeError: 'pygame.Rect' object has no attribute 'up'](https://stackoverflow.com/questions/64738269/attributeerror-pygame-rect-object-has-no-attribute-up/64738582#64738582)
- [What's difference between .get_rect() and pygame.Rect()?](https://stackoverflow.com/questions/66731019/whats-difference-between-get-rect-and-pygame-rect/66731068#66731068)  
- [What is Pygame.Rect() is used for in a program?](https://stackoverflow.com/questions/66730012/what-is-pygame-rect-is-used-for-in-a-program/66730067#66730067)  

## Move rectangle

Related Stack Overflow questions:

- [Difference between rect.move() and rect.move_ip in pygame](https://stackoverflow.com/questions/61578694/difference-between-rect-move-and-rect-move-ip-in-pygame/61578756#61578756)
- [PyGame rect.move movement not functioning properly](https://stackoverflow.com/questions/55362160/pygame-rect-move-movement-not-functioning-properly/55362918#55362918)  
- [How do I make a sprite "stand' on another sprite in pygame?](https://stackoverflow.com/questions/66077484/how-do-i-make-a-sprite-stand-on-another-sprite-in-pygame/66077719#66077719)  

The method [`pygame.Rect.move_ip`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move_ip) doesn't return any value. It modifies the [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) object itself.

So after

>```py
> textrect = textrect.move_ip(-50, -50)
>```

the value of `textrect` is `None`.

## Change size of rectangle

Related Stack Overflow questions:

- [How can I make a rectangle in pygame be able to check for other rectangles around it?](https://stackoverflow.com/questions/66039033/how-can-i-make-a-rectangle-in-pygame-be-able-to-check-for-other-rectangles-aroun/66039941#66039941)  
- [How does the pygame function pygame.rect.fit() work?](https://stackoverflow.com/questions/67008378/how-does-the-pygame-function-pygame-rect-fit-work/67008437#67008437)

## Floating point coordinates

Related Stack Overflow questions:

- [Pygame doesn't let me use float for rect.move, but I need it](https://stackoverflow.com/questions/63468413/pygame-doesnt-let-me-use-float-for-rect-move-but-i-need-it/63468637#63468637)  
  ![Pygame doesn't let me use float for rect.move, but I need it](https://i.stack.imgur.com/xfB54.gif)  

  :scroll: **[Minimal example - Move rectangle diagonal](../../examples/minimal_examples/pygame_minimal_move_rect_float.py)**

- [Problems with moving an enemy towards a character in pygame](https://stackoverflow.com/questions/70549998/problems-with-moving-an-enemy-towards-a-character-in-pygame/70550038#70550038)
- [PyGame move one unit in degrees](https://stackoverflow.com/questions/69312639/pygame-move-one-unit-in-degrees/69312664#69312664)  
- [Problem with Pygame movement acceleration, platformer game](https://stackoverflow.com/questions/59501126/problem-with-pygame-movement-acceleration-platformer-game/59501533#59501533)
- [How to draw a moving circle in Pygame with a small angle at a low speed and blinking?](https://stackoverflow.com/questions/61528967/how-to-draw-a-moving-circle-in-pygame-with-a-small-angle-at-a-low-speed-and-blin/61529427#61529427)

- [moving with a normalized vector in pygame inconsistent?](https://stackoverflow.com/questions/68486375/moving-with-a-normalized-vector-in-pygame-inconsistent/68486486#68486486)  
  ![moving with a normalized vector in pygame inconsistent?](https://i.stack.imgur.com/oPdGS.gif)

  :scroll: **[Minimal example - Move rectangle diagonal](../../examples/minimal_examples/pygame_minimal_move_diagonal.py)**

- [Ship moves up and left faster than down and right when rotating in pygame](https://stackoverflow.com/questions/62411259/ship-moves-up-and-left-faster-than-down-and-right-when-rotating-in-pygame/65347117#65347117)  
  ![Ship moves up and left faster than down and right when rotating in pygame](https://i.stack.imgur.com/6IPS1.gif)

Since [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) is supposed to represent an area on the screen, a `pygame.Rect` object can only store integral data.  

> The coordinates for Rect objects are all integers. [...]

The fraction part of the coordinates gets lost when the new position of the object is assigned to the _Rect_ object. If this is done every frame, the position error will accumulate over time.

If you want to store object positions with floating point accuracy, you have to store the location of the object in separate variables respectively attributes and to synchronize the `pygame.Rect` object. [`round`](https://docs.python.org/3/library/functions.html#round) the coordinates and assign it to the location (e.g. `.topleft`) of the rectangle:

```py
x, y = # floating point coordinates
rect.topleft = round(x), round(y)
```

## Use a rectangle as a frame and limit the object to a rectangular area

Related Stack Overflow questions:

- [Setting up an invisible boundary for my sprite](https://stackoverflow.com/questions/69180916/setting-up-an-invisible-boundary-for-my-sprite/69181366#69181366)  
  ![Setting up an invisible boundary for my sprite](https://i.stack.imgur.com/TQ1Ys.gif)  

  :scroll: **[Minimal example - Restrict rectangle to frame](../../examples/minimal_examples/pygame_minimal_intersect_frame_clamp_1.py)**

- [How do I get the size (width x height) of my pygame window](https://stackoverflow.com/questions/36653519/how-do-i-get-the-size-width-x-height-of-my-pygame-window) 
  [How do I get the size (width x height) of my pygame window](https://i.stack.imgur.com/xMMCz.gif)

If you only want to limit the player to a bounding rectangle, I recommend using [`pygame.Rect.clamp_ip`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.clamp)

> moves the rectangle inside another, in place

Define the bounding respectively border rectangle. If the player is limited to the screen, you can get a rectangle that defines the border from the display _Surface_ with [`pygame.display.get_surface()`](https://www.pygame.org/docs/ref/display.html#pygame.display.get_surface) and [`pygame.Surface.get_rect`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect):

```py
border_rect = pygame.display.get_surface().get_rect()
```

Clamp the player [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) by `border_rect`:

```py
self.rect.clamp_ip(border_rect)
```

You can do this with 1 line of code:

```py
self.rect.clamp_ip(pygame.display.get_surface().get_rect())
```

- [Window border in pygame](https://stackoverflow.com/questions/64205777/window-border-in-pygame/64206877#64206877)

Use a [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) object to limit the a circle to the bounds of the window. In the following `window` is the display _Surface_ :

```py
radius = 16
clampRect = window.get_rect().inflate(-radius*2, -radius*2)
circleX = max(clampRect.left, min(clampRect.right, circleX))
circleY = max(clampRect.top, min(clampRect.bottom, circleY))
```

Explanation:

[`get_rect()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect) generates a `pygame.Rect` with the size oft the [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface) which is associated to the display. [`inflate()`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.inflate) generates a new rectangle with the size changed by the diameter oft the circle, where the rectangle remains centered around its current center.  
In the following, `min` and `max` are used to clamp the center of the circle in the area defined by the rectangle.

:scroll: **[minimal example - Move object with keys limit it to the window borders](../../examples/minimal_examples/pygame_minimal_move_object_limit_window.py)**

## Center of a rectangular area

Related Stack Overflow questions:

- [how to center image inside a rect pygame](https://stackoverflow.com/questions/63834628/how-to-center-image-inside-a-rect-pygame/63834731#63834731)  
- [How do I center objects so the rectangle is around my character?](https://stackoverflow.com/questions/65789733/how-do-i-center-objects-so-the-rectangle-is-around-my-character/65789980#65789980)  

- [How to pin an image in the center of sprite rect](https://stackoverflow.com/questions/74973872/how-to-pin-an-image-in-the-center-of-sprite-rect/74973887#74973887)  
  ![How to pin an image in the center of sprite rect](https://i.stack.imgur.com/TL6Q1.gif)  

## Nested rectangles

Related Stack Overflow questions:

- [pygame define different position order make the different result](https://stackoverflow.com/questions/59810922/pygame-define-different-position-order-make-the-different-result/59810986#59810986)
- [Circle won't draw in pygame](https://stackoverflow.com/questions/64595078/circle-wont-draw-in-pygame/64595264#64595264)
- [The draw polygon function in pygame doesn't draw the correct amount of vertices](https://stackoverflow.com/questions/72265149/the-draw-polygon-function-in-pygame-doesnt-draw-the-correct-amount-of-vertices/72265263#72265263)

## List of rectangles

Related Stack Overflow questions:

- [How to dynamically generate shapes in Pygame?](https://stackoverflow.com/questions/61956243/how-to-dynamically-generate-shapes-in-pygame/61956356#61956356)

## Touching rectangles

Related Stack Overflow questions:

- [I do not know how to end game when specific block is touched in pygame](https://stackoverflow.com/questions/61412616/i-do-not-know-how-to-end-game-when-specific-block-is-touched-in-pygame/61412877#61412877)

## Rotated rectangle

Related Stack Overflow questions:

- [rotating a rectangle in pygame](https://stackoverflow.com/questions/68927683/rotating-a-rectangle-in-pygame/68927744#68927744)  
  ![rotating a rectangle in pygame](https://i.stack.imgur.com/Vxo3P.gif)  

  :scroll: **[Minimal example - rotate rectangle](../../examples/minimal_examples/pygame_minimal_draw_rectangle_rotated_2.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-AnalogClock](https://replit.com/@Rabbid76/PyGame-AnalogClock#main.py)**
