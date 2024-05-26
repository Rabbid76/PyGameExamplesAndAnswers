[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Every time you write a comment, you should grimace and feel the failure of your ability of expression."  
Robert C. Martin, The Robert C. Martin Clean Code Collection (Collection)

---

# Shape and contour

[pygame.draw](https://www.pygame.org/docs/ref/draw.html)
[pygame.gfxdraw](https://www.pygame.org/docs/ref/gfxdraw.html)

## Shapes

Related Stack Overflow questions:

- [Pygame Drawing a Rectangle](https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle/64629716#64629716)  
  ![Pygame Drawing a Rectangle](https://i.sstatic.net/JGP5N.png)

  📁 **[Minimal example - Draw shapes](../../examples/minimal_examples/pygame_minimal_draw_shapes_1.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-Shapes](https://replit.com/@Rabbid76/PyGame-Shapes#main.py)**

- [Is there a class in pygame to represent a non-AABB polygon?](https://stackoverflow.com/questions/68718593/is-there-a-class-in-pygame-to-represent-a-non-aabb-polygon/68718661#68718661)  
- [How to draw rectangle and circles in Pygame environment](https://stackoverflow.com/questions/68854226/how-to-draw-rectangle-and-circles-in-pygame-environment/68854284#68854284)  

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

## Transparent shapes

Related Stack Overflow questions:

- [Draw a transparent rectangles and polygons in pygame](https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangles-and-polygons-in-pygame/64630102#64630102)  
  ![Draw a transparent rectangles and polygons in pygame](https://i.sstatic.net/Zst87.png)

  📁 **[Minimal example - Draw transparent shapes](../../examples/minimal_examples/pygame_minimal_draw_transparent_shapes_1.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-TransparentShapes](https://replit.com/@Rabbid76/PyGame-TransparentShapes#main.py)**

- [How to make transparent pygame.draw.circle](https://stackoverflow.com/questions/59293057/how-to-make-transparent-pygame-draw-circle/59294087#59294087)  
  ![How to make transparent pygame.draw.circle](https://i.sstatic.net/nOoJj.png)  

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

## Draw single Pixel

Related Stack Overflow questions:

- [Pygame: Draw single pixel](https://stackoverflow.com/questions/10354638/pygame-draw-single-pixel/64571453#64571453)

The usual method of drawing a point on a _Surface_ or the display is to use  [`pygame.Surface.set_at']:

```py
window_surface.set_at((x, y), my_color)
```

However, this function is very slow and leads to a massive lack of performance if more than 1 point is to be drawn.

📁 **[Minimal example - Draw pixels with `set_at`](../../examples/minimal_examples/pygame_minimal_draw_pixels_1.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-DrawPixel-1](https://replit.com/@Rabbid76/PyGame-DrawPixel-1#main.py)**

![Pygame: Draw single pixel](https://i.sstatic.net/OiqGY.png)

Another option is to use a ["pygame.PixelArray"](https://www.pygame.org/docs/ref/pixelarray.html) object. This object enables direct pixel access to _Surface_ objects. A _PixelArray_ pixel item can be assigned directly. The pixel can be accessed by subscription. The PixelArray locks the _Surface_, You have to [`close()`](https://www.pygame.org/docs/ref/pixelarray.html#pygame.PixelArray.close) it when you have changed the pixel:

```py
pixel_array = pygame.PixelArray(window_surface)

pixel_array[x, y] = my_color
pixel_array[start_x:end_x, start_y:end_y] = my_color

pixel_array.close()
```

📁 **[Minimal example - Draw pixels with `pygame.PixelArray`](../../examples/minimal_examples/pygame_minimal_draw_pixels_2.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-DrawPixel-2](https://replit.com/@Rabbid76/PyGame-DrawPixel-2#main.py)**

![Pygame: Draw single pixel](https://i.sstatic.net/OiqGY.png)

## Draw rectangle

Related Stack Overflow questions:

- [How can I draw a rectangular outline (not filled) with PyGame?](https://stackoverflow.com/questions/60854803/how-can-i-draw-a-hollow-rectangle-using-pygame/60855000#60855000)  
  ![How can I draw a rectangular outline (not filled) with PyGame?](https://i.sstatic.net/w6jSR.png)![How can I draw a rectangular outline (not filled) with PyGame?](https://i.sstatic.net/lXNmw.png)  

- [How to Make a Border in Pygame](https://stackoverflow.com/questions/63095839/how-to-make-a-border-in-pygame/63099536#63099536)  
  ![How to Make a Border in Pygame](https://i.sstatic.net/2ReKu.png)![How to Make a Border in Pygame](https://i.sstatic.net/s0Lji.png)

- [Setting a pygame surface to have rounded corners](https://stackoverflow.com/questions/63700231/setting-a-pygame-surface-to-have-rounded-corners/63701005#63701005)  
  ![scene](https://i.sstatic.net/pDdn2.png)  

- [Is there a way to turn a rectangle into a circle in pygame?](https://stackoverflow.com/questions/71058033/is-there-a-way-to-turn-a-rectangle-into-a-circle-in-pygame/71060513#71060513)  
  ![Is there a way to have different tick rates for differents parts of my code in pygame?](https://i.sstatic.net/j301o.gif)

  📁 **[Minimal example - draw a rectangle with rounded corners](../../examples/minimal_examples/pygame_minimal_draw_rectangle_round_corners_2.py)**

- [Getting rotated rect of rotated image in Pygame](https://stackoverflow.com/questions/66984521/getting-rotated-rect-of-rotated-image-in-pygame/66984713#66984713)  
  ![Getting rotated rect of rotated image in Pygame](https://i.sstatic.net/GsQwQ.png)

- [Why did drawing a PyGame rectangle with very thick borders draw a plus shape instead?](https://stackoverflow.com/questions/65890797/why-did-drawing-a-pygame-rectangle-with-very-thick-borders-draw-a-plus-shape-ins/65890887#65890887)  

- [What is the difference between pygame.draw.rect and screen_surface.blit()?](https://stackoverflow.com/questions/65964467/what-is-the-difference-between-pygame-draw-rect-and-screen-surface-blit/65965806#65965806)  

- [Handling rectangle with negative width and height in pygame](https://stackoverflow.com/questions/66316513/handling-rectangle-with-negative-width-and-height-in-pygame/66316783#66316783)  

- [rotating a rectangle in pygame](https://stackoverflow.com/questions/68927683/rotating-a-rectangle-in-pygame/68927744#68927744)

Use [`pygame.draw.rect()`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect) to draw a rectangle. The 3rd argument of [`pygame.draw.rect`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect) has to be a tuple with 4 elements:

```py
pygame.draw.rect(win, (255, 0, 0),(x, y, width, height))
```  

Alternatively it can be a [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) object, too:

```py
rect = pygame.Rect(x, y, width, height)
pygame.draw.rect(win, (255, 0, 0), rect)
```

The last parameter of `pygame.draw.rect` is the thickness of line the outline. If the parameter is 0 (or default), then the rectangle is filled, else a rectangle with the specified line thickness is drawn. e.g:

![How can I draw a rectangular outline (not filled) with PyGame?](https://i.sstatic.net/w6jSR.png)

```py
pygame.draw.rect(surf, color, (x, y, w, h), outlineThickness)
```  

The corners of the rectangle are jagged. However, the corner radius can be set (`border_radius`) to get a better result:

```py
pygame.draw.rect(surf, color, (x, y, w, h), outlineThickness, border_radius=1)
```  

![How can I draw a rectangular outline (not filled) with PyGame?](https://i.sstatic.net/lXNmw.png)

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

📁 **[Minimal example - draw a rectangle with rounded corners](../../examples/minimal_examples/pygame_minimal_draw_rectangle_round_corners.py)**

![scene](https://i.sstatic.net/b2NqN.png)

Use [`pygame.Rect.normalize()`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.normalize) to handle rectangles with negative width and height:

> `normalize() -> None`  
This will flip the width or height of a rectangle if it has a negative size. The rectangle will remain in the same place, with only the sides swapped.

Create a `pygame.Rect` object and `normalize` it:

```py
rect = pygame.Rect(rpos[0], rpos[1], pos2[0]-rpos[0], pos2[1]-rpos[1])
rect.normalize()
pygame.draw.rect(window, (100, 200, 100), rect)
```

A `pygame.Rect` stores a position and a size. It is always axis aligned and cannot represent a rotated rectangle. Use [`pygame.math.Vector2.rotate()`](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.rotate) to compute the corner points of the rotated rectangle. Draw the rotated rectangle with [`pygame.draw.polygon()`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon):

```py
def draw_rect_angle(surf, rect, pivot, angle, width=0):
    pts = [rect.topleft, rect.topright, rect.bottomright, rect.bottomleft]
    pts = [(pygame.math.Vector2(p) - pivot).rotate(-angle) + pivot for p in pts]
    pygame.draw.polygon(surf, (255, 255, 0), pts, width)
```

📁 **[Minimal example - draw rotated rectangle](../../examples/minimal_examples/pygame_minimal_draw_rectangle_rotated_1.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-RotatedRectangle](https://replit.com/@Rabbid76/PyGame-RotatedRectangle#main.py)**

![Getting rotated rect of rotated image in Pygame](https://i.sstatic.net/GsQwQ.png)  

📁 **[Minimal example - rotate rectangle](../../examples/minimal_examples/pygame_minimal_draw_rectangle_rotated_2.py)**

![rotating a rectangle in pygame](https://i.sstatic.net/2NNT6.gif)

## Draw circle

Related Stack Overflow questions:

- [Pygame Wont Let Me Draw A Circle Error argument 3 must be sequence of length 2, not 4](https://stackoverflow.com/questions/62601880/pygame-wont-let-me-draw-a-circle-error-argument-3-must-be-sequence-of-length-2/62601934#62601934)
- [Slowing down the moving circle in pygame](https://stackoverflow.com/questions/64209772/slowing-down-the-moving-circle-in-pygame/64209853#64209853)
- [How to make a circular sprite appear - pygame](https://stackoverflow.com/questions/61445178/how-to-make-a-circular-sprite-appear-pygame/61445373#61445373)
- [Getting quarter of a circle with pygame.draw.circle()](https://stackoverflow.com/questions/66566259/getting-quarter-of-a-circle-with-pygame-draw-circle/66566646#66566646)

The _center_ argument of [`pygame.draw.circle()`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle) has to be a tuple with 2 integral components. If the coordinates are of a floating point type, they must [`round`](https://docs.python.org/3/library/functions.html#round)ed to integer values, otherwise a warning will be generated (_TypeError: integer argument expected, got float_):

```py
pygame.draw.circle(screen, (0, 0, 0), (round(circleX), round(circleY)), size)
```

Use the `center` attribute of a rectangle to center a circle on the rectangle:

```py
self.rect = self.image.get_rect()
pygame.draw.circle(self.image, color, self.rect.center, min(self.rect.center))
```

### Antialiased circle

Related Stack Overflow questions:

- [How do you draw an antialiased circular line of a certain thickness? How to set width on pygame.gfx.aacircle()?](https://stackoverflow.com/questions/64816341/how-do-you-draw-an-antialiased-circular-line-of-a-certain-thickness-how-to-set/65353318#65353318)  
  ![How do you draw an antialiased circular line of a certain thickness? How to set width on pygame.gfx.aacircle()?](https://i.sstatic.net/FBCXx.png)  
  ![How do you draw an antialiased circular line of a certain thickness? How to set width on pygame.gfx.aacircle()?](https://i.sstatic.net/NrksR.png)

You can try to stitch the circle with a pygame.draw.circle() for the body and pygame.gfxdraw.circle() on the edges. However, the quality is low and can depend on the system:

📁 **[Minimal example - Antialiased circle](../../examples/minimal_examples/pygame_minimal_draw_antialiased_circle.py)**  

```py
def drawAACircle(surf, color, center, radius, width):
    pygame.gfxdraw.aacircle(surf, *center, 100, color)  
    pygame.gfxdraw.aacircle(surf, *center, 100-width, color)  
    pygame.draw.circle(surf, color, center, radius, width) 
```

I recommend drawing a image with an antialiased circle and _blit_ the image. You can create the image using OpenCV ([opencv-python](https://pypi.org/project/opencv-python/)). See [OpenCV - Drawing Functions](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html).

📁 **[Minimal example - Antialiased circle with OpenCV](../../examples/minimal_examples/pygame_minimal_draw_antialiased_circle_cv2.py)**

```py
import cv2
import numpy

def drawAACircle(surf, color, center, radius, width):
    circle_image = numpy.zeros((radius*2+4, radius*2+4, 4), dtype = numpy.uint8)
    circle_image = cv2.circle(circle_image, (radius+2, radius+2), radius-width//2, (*color, 255), width, lineType=cv2.LINE_AA)  
    circle_surface = pygame.image.frombuffer(circle_image.flatten(), (radius*2+4, radius*2+4), 'RGBA')
    surf.blit(circle_surface, circle_surface.get_rect(center = center))
```

Another approach is to construct the circle with [`numpy.fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html).

📁 **[Minimal example - Antialiased circle with NumPy](../../examples/minimal_examples/pygame_minimal_draw_antialiased_circle_numpy.py)**  

```py
import pygame
import numpy

def drawAACircle(surf, color, center, radius):
    f_circle = lambda i, j: numpy.clip(radius - numpy.hypot(i-radius-1, j-radius-1), 0, 1) * 255
    shape = (radius*2+4, radius*2+4)
    circle_rgb = numpy.full((*shape, len(color)), color, dtype = numpy.uint8)
    circle_alpha = numpy.fromfunction(f_circle, shape).astype(numpy.uint8).reshape((*shape, 1))
    circle_array = numpy.concatenate((circle_rgb, circle_alpha), 2)
    circle_surface = pygame.image.frombuffer(circle_array.flatten(), shape, 'RGBA')
    surf.blit(circle_surface, circle_surface.get_rect(center = center))
```

- [Remove border from opencv generated ellipse in pygame](https://stackoverflow.com/questions/75720083/remove-border-from-opencv-generated-ellipse-in-pygame/75724348#75724348)

```py
def drawAACircle(surf, color, center, radius, width, angle):
    circle_image = np.zeros((radius*2, radius*2, 4), dtype = np.uint8)
    circle_image = cv2.ellipse(circle_image, (radius, radius), (radius-width, radius-width), (angle*-.5)-90 , 0, angle, (*color, 255), width, lineType=cv2.LINE_AA)  
    circle_surf = pygame.image.frombuffer(circle_image.tobytes(), circle_image.shape[1::-1], "RGBA")
    pos = (center[0]-radius, center[1]-radius) 
    surf.blit(circle_surf, pos, special_flags=pygame.BLEND_PREMULTIPLIED)
```

## Draw ellipse

Related Stack Overflow questions:

- [drawing a diagonal ellipse with pygame](https://stackoverflow.com/questions/23281952/drawing-a-diagonal-ellipse-with-pygame/65774382#65774382)  
  ![drawing a diagonal ellipse with pygame](https://i.sstatic.net/ruNV5.gif)  

  📁 **[Minimal example - Draw shapes](../../examples/minimal_examples/pygame_minimal_draw_rotated_ellipse_1.py)**

- [How to draw a rotated ellipse using Pygame?](https://stackoverflow.com/questions/65767785/how-to-draw-a-rotated-ellipse-using-pygame/65769408#65769408)  
  ![How to draw a rotated ellipse using Pygame?](https://i.sstatic.net/1v4ln.png)

## Draw lines and polygons

Related Stack Overflow questions:

- [How do you create a polygon that fills the area between 2 circles?](https://stackoverflow.com/questions/75105181/how-do-you-create-a-polygon-that-fills-the-area-between-2-circles/75109072#75109072)  
  ![How do you create a polygon that fills the area between 2 circles?](https://i.sstatic.net/Sk4uj.png)

  📁 **[Minimal example - Draw circle polygon](../../examples/minimal_examples/pygame_minimal_draw_circle_polygon_1.py)**

- [How to slowly draw a line in Python](https://stackoverflow.com/questions/57618029/how-to-slowly-draw-a-line-in-python/57621742#57621742)  
  ![How to slowly draw a line in Python](https://i.sstatic.net/Uhn7W.gif)

  📁 **[Minimal example - Draw a line slowly](../../examples/minimal_examples/pygame_minimal_draw_line_slowly_1.py)**

- [Slowly drawing a line in pygame while other lines remain static](https://stackoverflow.com/questions/57630853/slowly-drawing-a-line-in-pygame-while-other-lines-remain-static/57631750#57631750)  
  ![Slowly drawing a line in pygame while other lines remain static](https://i.sstatic.net/RhasT.gif)
- [Looping mousebutton down to draw lines](https://stackoverflow.com/questions/55477799/looping-mousebutton-down-to-draw-lines/55478174#55478174)  
  ![Looping mousebutton down to draw lines](https://i.sstatic.net/3qL0b.gif)
- [Is there a way to get the coordinates of a specific object/click in pygame?](https://stackoverflow.com/questions/61610006/is-there-a-way-to-get-the-coordinates-of-a-specific-object-click-in-pygame/61610397#61610397)  
  ![Is there a way to get the coordinates of a specific object/click in pygame?](https://i.sstatic.net/n1FCG.gif)
- [How can you make the previous line disappear in python?](https://stackoverflow.com/questions/61682742/how-can-you-make-the-previous-line-disappear-in-python/61683877#61683877)  
  ![How can you make the previous line disappear in python?](https://i.sstatic.net/qcAOV.gif)
- [How to use different colors for each line in pygame.draw.lines](https://stackoverflow.com/questions/67085359/how-to-use-different-colors-for-each-line-in-pygame-draw-lines/67085554#67085554)  
  ![How to use different colors for each line in pygame.draw.lines](https://i.sstatic.net/7zWbo.png)
- [Generating and drawing sin wave using pygame](https://stackoverflow.com/questions/67874803/generating-and-drawing-sin-wave-using-pygame/67875045#67875045)  
  ![Generating and drawing sin wave using pygame](https://i.sstatic.net/E5yaq.png)
- [How to translate and rotate the coordinate axis about a point in pygame screen?](https://stackoverflow.com/questions/68835224/how-can-i-make-my-code-more-optimised-by-not-drawing-a-rect-on-each-pixel/68835795#68835795)  
  ![How to translate and rotate the coordinate axis about a point in pygame screen?](https://i.sstatic.net/PqfHO.png)  

  📁 **[Minimal example - Draw a line slowly](../../examples/minimal_examples/pygame_minimal_draw_polygon_1.py)**

- [Drawing polygons in pygame using list](https://stackoverflow.com/questions/70482667/drawing-polygons-in-pygame-using-list/70482709#70482709)  
  ![Drawing polygons in pygame using list](https://i.sstatic.net/NKCI5.png)  

If you want to draw a polygon line with different colors for each segment, you need to draw each line segment separately. Write a function that uses a list of points and colors to draw the line:

```py
def draw_colorful_line(surf, colors, closed, points, width=1):
    for i in range(len(points)-1):
        pygame.draw.line(surf, colors[i], points[i], points[i+1], width)
    if closed:
        pygame.draw.line(surf, colors[-1], points[-1], points[0], width)
```

Use the function to draw the line:

```py
colors = ['green', 'blue', 'red']
points = [(10, 100), (20, 200), (30, 100)]
draw_colorful_line(screen, colors, True, points)
```

### Outline

Related Stack Overflow questions:

- [Adding an outline around a snake in snake game](https://stackoverflow.com/questions/73516121/adding-an-outline-around-a-snake-in-snake-game/73517037#73517037)
  ![Adding an outline around a snake in snake game](https://i.sstatic.net/93V8y.png)

  📁 **[Minimal example - Outline of rectangles](../../examples/minimal_examples/pygame_minimal_draw_outline_1.py)**

- [Why am I not getting appropriate values for the outline I am creating - mask with pygame](https://stackoverflow.com/questions/73716557/why-am-i-not-getting-appropriate-values-for-the-outline-i-am-creating-mask-wit/74172766#74172766)
  ![Why am I not getting appropriate values for the outline I am creating - mask with pygame](https://i.sstatic.net/TsGJb.png)

  📁 **[Minimal example - Sprite outline](../../examples/minimal_examples/pygame_minimal_draw_outline_2.py)**

### Line with round corners

Related Stack Overflow questions:

- [draw lines with round edges in pygame](https://stackoverflow.com/questions/70051590/draw-lines-with-round-edges-in-pygame/70053349#70053349)  
  ![draw lines with round edges in pygame](https://i.sstatic.net/XXp5w.png)

  📁 **[Minimal example - Line with round corners](../../examples/minimal_examples/pygame_minimal_draw_line_round_corners.py)**

### Dashed line

Related Stack Overflow questions:

- [How to draw a dashed curved line with pygame?](https://stackoverflow.com/questions/66943011/how-to-draw-a-dashed-curved-line-with-pygame/66944050#66944050)  
  ![How to draw a dashed curved line with pygame?](https://i.sstatic.net/uV3Sy.png)

  📁 **[Minimal example - Draw a dashed line](../../examples/minimal_examples/pygame_minimal_draw_line_dashed.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/DashedLine](https://replit.com/@Rabbid76/PyGame-DashedLine#main.py)**

To draw a dashed line, write a function that operates similar as [`pygame.draw.line()`](http://www.pygame.org/docs/ref/draw.html#pygame.draw.lines) but draws a dashed straight line. The function has an additional argument `prev_line_len` which indicates where the line segment is within a consecutive curve. Compute the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between the points and the [Unit vector](https://en.wikipedia.org/wiki/Unit_vector) that points from the beginning of the line segment to its end. Distribute the strokes along the line:

```py
def draw_dashed_line(surf, color, p1, p2, prev_line_len, dash_length=8):
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    if dx == 0 and dy == 0:
        return 
    dist = math.hypot(dx, dy)
    dx /= dist
    dy /= dist

    step = dash_length*2
    start = (int(prev_line_len) // step) * step
    end = (int(prev_line_len + dist) // step + 1) * step
    for i in range(start, end, dash_length*2):
        s = max(0, start - prev_line_len)
        e = min(start - prev_line_len + dash_length, dist)
        if s < e:
            ps = p1[0] + dx * s, p1[1] + dy * s 
            pe = p1[0] + dx * e, p1[1] + dy * e 
            pygame.draw.line(surf, color, pe, ps
```

Write another function that behaves similarly to [`pygame.draw.lines()`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines), but uses the former function (`draw_dashed_line`) to draw the dashed curve. Calculate the length from the beginning of the curve to the beginning of each line segment and pass it to the function:  

```py
def draw_dashed_lines(surf, color, points, dash_length=8):
    line_len = 0
    for i in range(1, len(points)):
        p1, p2 = points[i-1], points[i]
        dist = math.hypot(p2[0]-p1[0], p2[1]-p1[1])
        draw_dashed_line(surf, color, p1, p2, line_len, dash_length)
        line_len += dist
```

## Draw arc

Related Stack Overflow questions:

- [Creating an arc between two points pygame](https://stackoverflow.com/questions/58954526/creating-an-arc-between-two-points-pygame/58959662#58959662)

  📁 **[Minimal example - Draw an arc from point to point](../../examples/minimal_examples/pygame_minimal_draw_arc_between_points.py)**

 ![Creating an arc between two points pygame](https://i.sstatic.net/494KZ.png)

### Antialiased arc

Related Stack Overflow questions:

- [How to make a circular countdown timer in Pygame?](https://stackoverflow.com/questions/67168804/how-to-make-a-circular-countdown-timer-in-pygame/67168896#67168896)  
  ![How to make a circular countdown timer in Pygame?](https://i.sstatic.net/D2QqH.gif)
  ![How to make a circular countdown timer in Pygame?](https://i.sstatic.net/J6AIy.gif)

  📁 **[Minimal example - Draw an arc](../../examples/minimal_examples/pygame_minimal_timer_count_down_2.py)**

An arc can be drawn using [`pygame.draw.arc`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc):

```py
def drawArc(surf, color, center, radius, width, end_angle):
    arc_rect = pygame.Rect(0, 0, radius*2, radius*2)
    arc_rect.center = center
    pygame.draw.arc(surf, color, arc_rect, 0, end_angle, width)
```

Sadly the quality of `pygame.draw.arc` with a _width_ > 1 is  poor. However this can be improved, using [cv2](https://pypi.org/project/opencv-python/) and [`cv2.ellipse`](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga57be400d8eff22fb946ae90c8e7441f9):

```py
import cv2
import numpy

def drawArcCv2(surf, color, center, radius, width, end_angle):
    circle_image = numpy.zeros((radius*2+4, radius*2+4, 4), dtype = numpy.uint8)
    circle_image = cv2.ellipse(circle_image, (radius+2, radius+2),
        (radius-width//2, radius-width//2), 0, 0, end_angle, (*color, 255), width, lineType=cv2.LINE_AA) 
    circle_surface = pygame.image.frombuffer(circle_image.flatten(), (radius*2+4, radius*2+4), 'RGBA')
    surf.blit(circle_surface, circle_surface.get_rect(center = center))
```

## Bezier

Related Stack Overflow questions:

- [Trying to make a Bezier Curve on PyGame library](https://stackoverflow.com/questions/69804595/trying-to-make-a-bezier-curve-on-pygame-library/69816648#69816648)  
  ![Trying to make a Bezier Curve on PyGame library](https://i.sstatic.net/1GYKJ.gif)

  📁 **[Minimal example - Draw bezier](../../examples/minimal_examples/pygame_minimal_draw_bezier_1.py)**

- [How Can I Make a Thicker Bezier in Pygame?](https://stackoverflow.com/questions/71365567/how-can-i-make-a-thicker-bezier-in-pygame/71365892#71365892)  
  ![How Can I Make a Thicker Bezier in Pygame?](https://i.sstatic.net/gBXdX.png)

  📁 **[Minimal example - Draw bezier](../../examples/minimal_examples/pygame_minimal_draw_bezier_2.py)**

- [How can I connect two points with a series of circles?](https://stackoverflow.com/questions/73838853/how-can-i-connect-two-points-with-a-series-of-circles/73839646#73839646)  
  ![How can I connect two points with a series of circles?](https://i.sstatic.net/SReXX.gif)

  📁 **[Minimal example - Water waves](../../examples/minimal_examples/pygame_minimal_water_waves_1.py)**

- [How to make sprite move to point along a curve in pygame](https://stackoverflow.com/questions/74070512/how-to-make-sprite-move-to-point-along-a-curve-in-pygame/74070714#74070714)  
  ![How to make sprite move to point along a curve in pygame](https://i.sstatic.net/jmgzy.gif)  

  📁 **[Minimal example - Draw bezier](../../examples/minimal_examples/pygame_minimal_draw_bezier_2.py)**

## Wireframe shape

Related Stack Overflow questions:

- [Expand wireframe 3d shape made in pygame](https://stackoverflow.com/questions/68204153/expand-wireframe-3d-shape-made-in-pygame/68204459#68204459)  
  ![Expand wireframe 3d shape made in pygame](https://i.sstatic.net/GaaXb.png)
