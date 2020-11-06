[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Surface array, pixel array, buffer proxy

## Surface array

[`pygame.surfarray`](https://www.pygame.org/docs/ref/surfarray.html) module

Related Stack Overflow questions:

- [Get image array from display in pygame](https://stackoverflow.com/questions/64558238/get-image-array-from-display-in-pygame)

Use `pygame.surfarray.pixels2d`, `pygame.surfarray.array2d`, `pygame.surfarray.pixels3d`, or `pygame.surfarray.array3d` to create a pixel array from a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object (see [`pygame.surfarray`](https://www.pygame.org/docs/ref/surfarray.html) module):

```py
import pygame

# [...]

window = pygame.display.set_mode()
```

```py
array2D = pygame.surfarray.array2d(window)
```

```py
array3D = pygame.surfarray.array3d(window)
```

While `array*` creates copies of the pixels from a _Surface_ object, `pixel*` creates a new array that directly references the pixel values ​​in a _Surface_ object.  
The `*2d` version generates a two-dimensional array, with each pixel represented by a single integral value. The `*3d` version generates a three-dimensional array in which each color channel is represented by an integer value.

## Pixel array

[`pygame.PixelArray`](https://www.pygame.org/docs/ref/pixelarray.html) object

Related Stack Overflow questions:

- [Pygame: Draw single pixel](https://stackoverflow.com/questions/10354638/pygame-draw-single-pixel)

 Use a ["pygame.PixelArray"](https://www.pygame.org/docs/ref/pixelarray.html) object to enable direct pixel access to _Surface_ objects. A _PixelArray_ pixel item can be assigned directly. The pixel can be accessed by subscription. The PixelArray locks the _Surface_, You have to [`close()`](https://www.pygame.org/docs/ref/pixelarray.html#pygame.PixelArray.close) it when you have changed the pixel:

```py
pixel_array = pygame.PixelArray(window_surface)

pixel_array[x, y] = my_color
pixel_array[start_x:end_x, start_y:end_y] = my_color

pixel_array.close()
```

:scroll: **[Minimal example - Draw pixels with `pygame.PixelArray`](../../examples/minimal_examples/pygame_minimal_draw_pixels_2.py)**

![Pygame: Draw single pixel](https://i.stack.imgur.com/OiqGY.png)

## Buffer proxy

[`pygame.BufferProxy`](https://www.pygame.org/docs/ref/bufferproxy.html) object
