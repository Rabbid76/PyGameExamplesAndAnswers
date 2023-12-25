[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"You keep on learning and learning, and pretty soon you learn something no one has learned before"
Richard P. Feynman

---

# Clipping

## Set clipping region

Related to [`set_clip()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_clip)

Related Stack Overflow questions:

- [Is there a way to restrict the title crawl to certain portion of screen?](https://stackoverflow.com/questions/60508313/is-there-a-way-to-restrict-the-title-crawl-to-certain-portion-of-screen)

## Circular clipping region

Related Stack Overflow questions:

- [how to make circular surface in PyGame](https://stackoverflow.com/questions/64075338/how-to-make-circular-surface-in-pygame/64075812#64075812)  
  ![how to make circular surface in PyGame](https://i.stack.imgur.com/koG1J.png)

  :scroll: **[Minimal example - Clip circular 1](../../examples/minimal_examples/pygame_minimal_clip_circular_1.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ClipCircularRegion-1](https://replit.com/@Rabbid76/PyGame-ClipCircularRegion-1#main.py)**

- [How do I focus light or how do I only draw certain circular parts of the window in pygame?](https://stackoverflow.com/questions/61657481/how-do-i-focus-light-or-how-do-i-only-draw-certain-circular-parts-of-the-window/61658124#61658124)  
  ![How do I focus light or how do I only draw certain circular parts of the window in pygame?](https://i.stack.imgur.com/pbiAC.gif)
  
  :scroll: **[Minimal example - Clip circular 2](../../examples/minimal_examples/pygame_minimal_clip_circular_2.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ClipCircularRegion-2](https://replit.com/@Rabbid76/PyGame-ClipCircularRegion-2#main.py)**

  ![How do I focus light or how do I only draw certain circular parts of the window in pygame?](https://i.stack.imgur.com/Pt2IY.gif)

  :scroll: **[Minimal example - Clip circular 3](../../examples/minimal_examples/pygame_minimal_clip_circular_3.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ClipCircularRegion-3](https://replit.com/@Rabbid76/PyGame-ClipCircularRegion-3#main.py)**

- [How do I display a large black rectangle with a moveable transparent circle in pygame?](https://stackoverflow.com/questions/57393670/how-do-i-display-a-large-black-rectangle-with-a-moveable-transparent-circle-in-p/57612836#57612836)  
  ![How do I display a large black rectangle with a moveable transparent circle in pygame?](https://i.stack.imgur.com/JLkq4.gif)

  :scroll: **[Minimal example - Clip circular 4](../../examples/minimal_examples/pygame_minimal_clip_circular_4.py)**

- [Can I use an image on a moving object within Pygame as opposed to to a color?](https://stackoverflow.com/questions/65851274/can-i-use-an-image-on-a-moving-object-within-pygame-as-opposed-to-to-a-color/65851431#65851431)  
  ![Can I use an image on a moving object within Pygame as opposed to to a color?](https://i.stack.imgur.com/kIAeK.gif)  

  :scroll: **[Minimal example - Clip circular 5](../../examples/minimal_examples/pygame_minimal_clip_circular_5.py)**

- [How do you clip a circle (or any non-Rect) from an image in pygame?](https://stackoverflow.com/questions/74970507/how-do-you-clip-a-circle-or-any-non-rect-from-an-image-in-pygame/74970625#74970625)  

## Polygon clipping

:scroll: **[Minimal example - Clip polygon](../../examples/minimal_examples/pygame_minimal_clip_polygon_1.py)**

## Clipping with masks

Related Stack Overflow questions:

- [How do I modify this code to add a striped pattern to the star?](https://stackoverflow.com/questions/76633186/how-do-i-modify-this-code-to-add-a-striped-pattern-to-the-star/76634395#76634395)  
  ![How do I modify this code to add a striped pattern to the star?](https://i.stack.imgur.com/eWygj.png)  

- [Trianglular picture in pygame](https://stackoverflow.com/questions/77714070/trianglular-picture-in-pygame/77714179#77714179)

![Clipping with masks](https://i.stack.imgur.com/HkRcD.png)

:scroll: **[Minimal example - Clipping with masks](../../examples/minimal_examples/pygame_minimal_clip_mask.py)**

Convert a [`pygame.mask.Mask`](https://www.pygame.org/docs/ref/mask.html#pygame.mask.Mask) to a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) with [`pygame.mask.Mask.to_surface`](https://www.pygame.org/docs/ref/mask.html#pygame.mask.Mask.to_surface). Use `setsurface` to specify the source image and the `unsetcolor` argument to specify the transparent background:

```py
def clip_surface(surf, mask):
    return mask.to_surface(setsurface = surf.convert_alpha(), unsetcolor = (0, 0, 0, 0))
```
