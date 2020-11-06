[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Zoom surface

Related Stack Overflow questions:

- [pygame.transform.scale does not work on the “game” surface](https://stackoverflow.com/questions/56407891/pygame-transform-scale-does-not-work-on-the-game-surface/56408482#56408482)
- [Manipulating rect image size in pygame](https://stackoverflow.com/questions/59919826/manipulating-rect-image-size-in-pygame/59919909#59919909)  
  ![Manipulating rect image size in pygame](https://i.stack.imgur.com/soWSp.gif)

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