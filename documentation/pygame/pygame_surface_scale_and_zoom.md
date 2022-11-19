[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Once I get on a puzzle, I can't get off."  
Richard P. Feynman

---

# Scale and zoom

## Scale surface

Related Stack Overflow questions:

- [How can i reshape an array from (280, 280, 3) to (28, 28, 3)](https://stackoverflow.com/questions/62391656/how-can-i-reshape-an-array-from-280-280-3-to-28-28-3/62392403#62392403)
- [How to change an image size in Pygame?](https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame/66611330#66611330)  
- [What does the parameter DestSurface in Pygame.transform.scale mean and how do I use it?](https://stackoverflow.com/questions/60045882/what-does-the-parameter-destsurface-in-pygame-transform-scale-mean-and-how-do-i/60045993#60045993)
- [How do i properly rescale an image on PyGame without it being badly cropped?](https://stackoverflow.com/questions/55319967/how-do-i-properly-rescale-an-image-on-pygame-without-it-being-badly-cropped/55321552#55321552)
- [Set the width and height of a pygame surface](https://stackoverflow.com/questions/62467003/set-the-width-and-height-of-a-pygame-surface/62467567#62467567)
- [Resize Image Content but Keep Image Dimensions](https://stackoverflow.com/questions/63648196/resize-image-content-but-keep-image-dimensions/63648597#63648597)
- [How can you draw more detailed/smoother images in pygame?](https://stackoverflow.com/questions/65492782/how-can-you-draw-more-detailed-smoother-images-in-pygame/65492828#65492828)

- [How to scale an image by window size?](https://stackoverflow.com/questions/68424287/how-to-scale-an-image-by-window-size/68424354#68424354)  
  ![How to scale an image by window size?](https://i.stack.imgur.com/KIjG8.png)  

[`pygame.transform.scale()`](https://www.pygame.org/docs/ref/surface.html) does not scale the input Surface itself. It creates a new surface and does a scaled "blit" to the new surface. The new surface is returned by the return value:

`pygame.transform.scale()` does:

1. Creates a new surface (`newSurface`) with size `(width, height)`.
2. Scale and copy `Surface` to `newSurface`.
3. Return `newSurface`.

The destination surface is a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) where the scaled surface is copied to. That is quicker, because the memory for the Surface has not to be allocated.

It `DestSurface` is set, then `pygame.transform.scale()` does:

1. Scale and copy `Surface` to the `DestSurface`.
2. Return `DestSurface`.

For that reason, the size of `DestSurface` has to be `(width, height)`, the format of `DestSurface` has the same as the format of `Surface`.

A possible use case is if you have to continuously scale something to a fixed size in the main application loop (e.g. if the surface is dynamically generated). In the following `surf` is assumed to be a surface object:

```py
while True:
    # [...]

    scaledSurf = pygame.transform.scale(surf, (100, 100)) 
    window.blit(scaledSurf, (x, y)
```

The code can be improved by using the `DestSurface` parameter:

```py
scaledSurf = pygame.Surface((100, 100))

while True:
    # [...]

    pygame.transform.scale(surf, (100, 100), scaledSurf) 
    window.blit(scaledSurf, (x, y)
```

That is probably a rare case. In general you should try to scale the surfaces at the initialization, rather than continuously in the application loop and to use the scaled surfaces in the loop. 

Do not try to use the parameter compulsively and do not "construct" a use case for the `DestSurface` parameter. Do it the other way around. Write your application and make it run. Then investigate whether the `DestSurface` parameter can be an improvement for your specific use case.

## Transform scale and zoom surface

Related Stack Overflow questions:

- [How do I scale a PyGame image (Surface) with respect to its center?](https://stackoverflow.com/questions/59919826/how-do-i-scale-a-pygame-image-surface-with-respect-to-its-center/59919909#59919909)  
  [How to change an image size in Pygame?](https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame/66611330#66611330)  
  ![How do I scale a PyGame image (Surface) with respect to its center?](https://i.stack.imgur.com/soWSp.gif)

  :scroll: **[Minimal example - Spin](../../examples/minimal_examples/pygame_minimal_scale_center.py)**

- [pygame.transform.scale does not work on the “game” surface](https://stackoverflow.com/questions/56407891/pygame-transform-scale-does-not-work-on-the-game-surface/56408482#56408482)

- [Pygame cannot make image bigger over time](https://stackoverflow.com/questions/68395844/pygame-cannot-make-image-bigger-over-time/68395966#68395966)  
  ![Pygame cannot make image bigger over time](https://i.stack.imgur.com/BhC52.gif)  

Define a zoom factor and calculate the size of the of the zoom area. e.g. If the zoom factor is 2, the area that needs to be zoomed on the window is half the width and height of the window:

```py
zoom = 2

wnd_w, wnd_h = window.get_size()
zoom_size = (round(wnd_w/zoom), round(wnd_h/zoom))
```

Define the rectangular zoom area. The center point of the area is the position where to zoom to. (e.g the cursor position):

```py
zoom_area = pygame.Rect(0, 0, *zoom_size)
zoom_area.center = (pos_x, pos_y)
```

Create a new [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_clip) with the size of the zoom area and copy the region of the window to the surface, by using [`,blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit), where the `area` parameter is set to the zoom region:

```py
zoom_surf = pygame.Surface(zoom_area.size)
zoom_surf.blit(screen, (0, 0), zoom_area)
```

Scale `zoom_surf` by either [`pygame.transform.scale()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale) or [`pygame.transform.smoothscale()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.smoothscale):

```py
zoom_surf = pygame.transform.scale(zoom_surf, (wnd_w, wnd_h))
```

Now `zoom_surf` has the same size as the window. `.blit` the surface to the window:

```py
window.blit(zoom_surf, (0, 0))
```

## Scale and zoom window

See [Display, display position, resize, coordinate system and scroll - Scale and zoom window](pygame_display_resize_and_scroll.md)

- [Zooming in and out of a PyGame window with all objects still in place](https://stackoverflow.com/questions/64936805/zooming-in-and-out-of-a-pygame-window-with-all-objects-still-in-place/64937795#64937795)  
  ![Zooming in and out of a PyGame window with all objects still in place](https://i.stack.imgur.com/qYHGr.gif)

  :scroll: **[Minimal example - Display zoom](../../examples/minimal_examples/pygame_minimal_display_zoom.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-colliderect](https://replit.com/@Rabbid76/PyGame-colliderect#main.py)**

### Zoom collision and hitboxes

- [Pygame sprite hitboxes don't follow as screen scrolls/zooms](https://stackoverflow.com/questions/74215365/pygame-sprite-hitboxes-dont-follow-as-screen-scrolls-zooms/74218352#74218352)  
  ![Pygame sprite hitboxes don't follow as screen scrolls/zooms](https://i.stack.imgur.com/seGNf.gif)

## Spin effect through scaling

Related Stack Overflow questions:

- [“Spin” coin image in python, pygame clicker game](https://stackoverflow.com/questions/65173270/spin-coin-image-in-python-pygame-clicker-game/65173486#65173486)  
  ![“Spin” coin image in python, pygame clicker game](https://i.stack.imgur.com/4nsFE.gif)

  :scroll: **[Minimal example - Spin](../../examples/minimal_examples/pygame_minimal_scale_spin.py)**
