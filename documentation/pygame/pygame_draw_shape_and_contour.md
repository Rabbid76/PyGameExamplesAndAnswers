[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Shape and contour

Related Stack Overflow questions:

- [Pygame Drawing a Rectangle](https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle)
- [Draw a transparent rectangle in pygame](https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame/64630102#64630102)  

With the module [pygame.draw](https://www.pygame.org/docs/ref/draw.html) shapes like rectangles, circles, polygons or liens can be drawn.

[`pygame.draw.rect`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect) draws filled rectangular shapes or outlines. The arguments are the target _Surface_ (i.s. the display), the _color_, the _rectangle_ and the optional outline _width_. The _rectangle_ argument is a tuple with the 4 components (_x_, _y_, _width_, _height_), where (_x_, _y_) is the upper left point of the rectangle. Alternatively, the argument can be a [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) object:

```py
pygame.draw.rect(window, color, (x, y, width, height))
```

```py
rectangle = pygame.Rect(x, y, width, height)
pygame.draw.rect(window, color, rectangle)
```

[`pygame.draw.circle`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle) draws filled circles or outlines. The arguments are the target _Surface_ (i.s. the display), the _color_, the _center_, the _radius_ and the optional outline _width_. The _center_ argument is a tuple with the 2 components (_x_, _y_):

```py
pygame.draw.circle(window, color, (x, y), radius)
```

[`pygame.draw.polygon`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon) draws filled polygons or contours. The arguments are the target _Surface_ (i.s. the display), the _color_, a list of _points_ and the optional contour _width_. Each _point_ is a tuple with the 2 components (_x_, _y_):

```cpp
pygame.draw.polygon(window, color, [(x1, y1), (x2, y2), (x3, y3)])
```

:scroll: **[Minimal example - Draw shapes](../../examples/minimal_examples/pygame_minimal_draw_shapes_1.py)**

![https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame](https://i.stack.imgur.com/JGP5N.png)

Unfortunately there is no good way to draw a transparent shape. See [pygame.draw](https://www.pygame.org/docs/ref/draw.html) module:

> A color's alpha value will be written directly into the surface [...], but the draw function will not draw transparently.

Therefor you hve to do a workaround:

1. Create a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object with a per-pixel alpha format large enough to cover the shape.
2. Draw the shape on the _Surface.
3. Blend the _Surface_ with the target _Surface_. [`blit()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) by default blends 2 _Surfaces_

For example 3 functions, which can draw transparent rectangles, circles and polygons:

```py
def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)
```

```py
def draw_circle_alpha(surface, color, center, radius):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    surface.blit(shape_surf, target_rect)
```

```py
def draw_polygon_alpha(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)
```

:scroll: **[Minimal example - Draw transparent shapes](../../examples/minimal_examples/pygame_minimal_draw_transparent_shapes_1.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TransparentShapes](https://repl.it/@Rabbid76/PyGame-TransparentShapes#main.py)</kbd>

![Draw a transparent rectangle in pygame](https://i.stack.imgur.com/Zst87.png)

## Draw single pixle

Related Stack Overflow questions:

- [Pygame: Draw single pixel](https://stackoverflow.com/questions/10354638/pygame-draw-single-pixel)

The usual method of drawing a point on a _Surface_ or the display is to use  [`pygame.Surface.set_at']:

```py
window_surface.set_at((x, y), my_color)
```

However, this function is very slow and leads to a massive lack of performance if more than 1 point is to be drawn.

:scroll: **[Minimal example - Draw pixels with `set_at`](../../examples/minimal_examples/pygame_minimal_draw_pixels_1.py)**

![Pygame: Draw single pixel](https://i.stack.imgur.com/OiqGY.png)

Another option is to use a ["pygame.PixelArray"](https://www.pygame.org/docs/ref/pixelarray.html) object. This object enables direct pixel access to _Surface_ objects. A _PixelArray_ pixel item can be assigned directly. The pixel can be accessed by subscription. The PixelArray locks the _Surface_, You have to [`close()`](https://www.pygame.org/docs/ref/pixelarray.html#pygame.PixelArray.close) it when you have changed the pixel:

```py
pixel_array = pygame.PixelArray(window_surface)

pixel_array[x, y] = my_color
pixel_array[start_x:end_x, start_y:end_y] = my_color

pixel_array.close()
```

:scroll: **[Minimal example - Draw pixels with `pygame.PixelArray`](../../examples/minimal_examples/pygame_minimal_draw_pixels_2.py)**

![Pygame: Draw single pixel](https://i.stack.imgur.com/OiqGY.png)

## Draw rectangle

Related Stack Overflow questions:

- [How to show a pictures rectangle after calling get_rect()](https://stackoverflow.com/questions/62263115/how-to-show-a-pictures-rectangle-after-calling-get-rect/62263801#62263801)
- [My pygame rects are giving a rect argument is invalid error](https://stackoverflow.com/questions/63954352/my-pygame-rects-are-giving-a-rect-argument-is-invalid-error/63955733#63955733)
- [How can I draw a rectangular outline (not filled) with PyGame?](https://stackoverflow.com/questions/60854803/how-can-i-draw-a-hollow-rectangle-using-pygame/60855000#60855000)
- [Setting a pygame surface to have rounded corners](https://stackoverflow.com/questions/63700231/setting-a-pygame-surface-to-have-rounded-corners/63701005#63701005)  
  ![scene](https://i.stack.imgur.com/pDdn2.png)

The 3rd argument of [`pygame.draw.rect`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect) has to be a tuple with 4 elements:

<s>`pygame.draw.rect(win, (255, 0, 0),(x, y, width, height, vel))`</s>
```py
pygame.draw.rect(win, (255, 0, 0),(x, y, width, height))
```  

Alternatively it can be a [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) object, too:

```py
rect = pygame.Rect(x, y, width, height)
pygame.draw.rect(win, (255, 0, 0), rect)
```

You can achieve what you want by setting the key word argument `border_radius` of the function [`pygame.draw.rect`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect).

Create a rectangle the same size as the image and and per pixel alpha (`SRCALPHA`) and draw a completely white, opaque image with round corners on it:

```py
size = self.original_image.get_size()
self.rect_image = pg.Surface(size, pg.SRCALPHA)
pg.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)
```

Copy the original image and use the `BLEND_RGBA_MIN` blending mode to blend the rectangle with the image (see [`pygame.Surface.blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit)):

```py
self.image = self.original_image.copy().convert_alpha()
self.image.blit(self.rect_image, (0, 0), None, pg.BLEND_RGBA_MIN)
```

**Note, the keyword attribute `border_radius` is a new feature. You have to use the most recent pygame version (2.0.0.dev10).**

If you can't use version 2.0.0.dev10, you'll need to stick the rounded rectangle together yourself:

```py
class Rectangle(pg.sprite.Sprite):
    # [...]

    def set_rounded(self, roundness):
        size = self.original_image.get_size()
        self.rect_image = pg.Surface(size, pg.SRCALPHA)

        #pg.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)

        r, c = roundness, (255, 255, 255)
        pg.draw.rect(self.rect_image, c, (r, 0, size[0]-2*r, size[1]))
        pg.draw.rect(self.rect_image, c, (0, r, size[0], size[1]-2*r))
        for cpt in [(r, r), (size[0]-r, r), (r, size[1]-r), (size[0]-r, size[1]-r)]:  
            pg.draw.circle(self.rect_image, c, cpt, r)

        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pg.BLEND_RGBA_MIN) 
```

:scroll: **[Minimal example - draw a rectangle with rounded corners](../../examples/minimal_examples/pygame_minimal_draw_rectangle_round_corners.py)**

![scene](https://i.stack.imgur.com/b2NqN.png)

## Draw circle

Related Stack Overflow questions:

- [Pygame Wont Let Me Draw A Circle Error argument 3 must be sequence of length 2, not 4](https://stackoverflow.com/questions/62601880/pygame-wont-let-me-draw-a-circle-error-argument-3-must-be-sequence-of-length-2/62601934#62601934)
- [Slowing down the moving circle in pygame](https://stackoverflow.com/questions/64209772/slowing-down-the-moving-circle-in-pygame/64209853#64209853)
- [How to make a circular sprite appear - pygame](https://stackoverflow.com/questions/61445178/how-to-make-a-circular-sprite-appear-pygame/61445373#61445373)

The _center_ argument of [`pygame.draw.circle()`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle) has to be a tuple with 2 integral components. You have to [`round`](https://docs.python.org/3/library/functions.html#round) the coordinate to integral values:

```py
pygame.draw.circle(screen, (0, 0, 0), (round(circleX), round(circleY)), size)
```

## Draw lines and polygons

Related Stack Overflow questions:

- [Slowly drawing a line in pygame while other lines remain static](https://stackoverflow.com/questions/57630853/slowly-drawing-a-line-in-pygame-while-other-lines-remain-static/57631750#57631750)  
  ![Slowly drawing a line in pygame while other lines remain static](https://i.stack.imgur.com/RhasT.gif)
- [Looping mousebutton down to draw lines](https://stackoverflow.com/questions/55477799/looping-mousebutton-down-to-draw-lines/55478174#55478174)  
  ![Looping mousebutton down to draw lines](https://i.stack.imgur.com/3qL0b.gif)
- [Is there a way to get the coordinates of a specific object/click in pygame?](https://stackoverflow.com/questions/61610006/is-there-a-way-to-get-the-coordinates-of-a-specific-object-click-in-pygame/61610397#61610397)  
  ![Is there a way to get the coordinates of a specific object/click in pygame?](https://i.stack.imgur.com/n1FCG.gif)
- [How can you make the previous line disappear in python?](https://stackoverflow.com/questions/61682742/how-can-you-make-the-previous-line-disappear-in-python/61683877#61683877)  
  ![How can you make the previous line disappear in python?](https://i.stack.imgur.com/qcAOV.gif)
- [How to Make a Border in Pygame](https://stackoverflow.com/questions/63095839/how-to-make-a-border-in-pygame/63099536#63099536)  
  ![How to Make a Border in Pygame](https://i.stack.imgur.com/2ReKu.png)![How to Make a Border in Pygame](https://i.stack.imgur.com/s0Lji.png)
