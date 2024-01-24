[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Surface array, pixel array, buffer proxy

## Surface array

[`pygame.surfarray`](https://www.pygame.org/docs/ref/surfarray.html) module

Related Stack Overflow questions:

- [Get image array from display in pygame](https://stackoverflow.com/questions/64558238/get-image-array-from-display-in-pygame)  
- [Get RGB pixel data of a section of a screen as an array in pygame](https://stackoverflow.com/questions/68414745/get-rgb-pixel-data-of-a-section-of-a-screen-as-an-array-in-pygame/68414812#68414812)  
- [pygame.surfarray.pixels3d doesn’t give correct pixel values with a text surface](https://stackoverflow.com/questions/70565956/pygame-surfarray-pixels3d-doesn-t-give-correct-pixel-values-with-a-text-surface/70566155#70566155)

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

To get the all channels of an transparent image, you have to get the color channels ([`array3d`](https://www.pygame.org/docs/ref/surfarray.html#pygame.surfarray.array3d) or [`pixels3d`](https://www.pygame.org/docs/ref/surfarray.html#pygame.surfarray.pixels3d)) and the alpha channel ([`array_alpha`](https://www.pygame.org/docs/ref/surfarray.html#pygame.surfarray.array_alpha) or [`pixels_alpha`](https://www.pygame.org/docs/ref/surfarray.html#pygame.surfarray.pixels_alpha)) and stick them together. Recreate the _Surface_ with [` pygame.image.frombuffer`](https://www.pygame.org/docs/ref/image.html#pygame.image.frombuffer):

```py
pixels_rgb = pygame.surfarray.array3d(rgba_image)
pixels_alpha = pygame.surfarray.array_alpha(rgba_image).reshape((*pixels_rgb.shape[0:2], 1))
pixels_rgba = np.concatenate((pixels_rgb, pixels_alpha), 2)

new_rgba_image = pygame.image.frombuffer(pixels_rgba.transpose((1, 0, 2)).copy(order='C'), text.get_size(), 'RGBA')
```


## Pixel array

[`pygame.PixelArray`](https://www.pygame.org/docs/ref/pixelarray.html) object

Related Stack Overflow questions:

- [Pygame: Draw single pixel](https://stackoverflow.com/questions/10354638/pygame-draw-single-pixel)
- [Speed up double for loop PyGame draw](https://stackoverflow.com/questions/61856330/speed-up-double-for-loop-pygame-draw/61856399#61856399)  
- [pixel image to tile map](https://stackoverflow.com/questions/29133065/pixel-image-to-tile-map/65966555#65966555)  

 Use a ["pygame.PixelArray"](https://www.pygame.org/docs/ref/pixelarray.html) object to enable direct pixel access to _Surface_ objects. A _PixelArray_ pixel item can be assigned directly. The pixel can be accessed by subscription. The PixelArray locks the _Surface_, You have to [`close()`](https://www.pygame.org/docs/ref/pixelarray.html#pygame.PixelArray.close) it when you have changed the pixel:

```py
pixel_array = pygame.PixelArray(window_surface)

pixel_array[x, y] = my_color
pixel_array[start_x:end_x, start_y:end_y] = my_color

pixel_array.close()
```

📁 **[Minimal example - Draw pixels with `pygame.PixelArray`](../../examples/minimal_examples/pygame_minimal_draw_pixels_2.py)**

![Pygame: Draw single pixel](https://i.stack.imgur.com/OiqGY.png)

## Buffer proxy

[`pygame.BufferProxy`](https://www.pygame.org/docs/ref/bufferproxy.html) object
