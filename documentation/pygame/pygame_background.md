[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Background

## Checkered background

Related Stack Overflow questions:

- [How To Create A Checkered Background Using Pygame Surfarrays?](https://stackoverflow.com/questions/73277963/how-to-create-a-checkered-background-using-pygame-surfarrays/73278096#73278096)  
  ![How To Create A Checkered Background Using Pygame Surfarrays?](https://i.sstatic.net/YYTQ3.png)

  📁 **[Minimal example - Checkered background](../../examples/minimal_examples/pygame_minimal_checkered_background_1.py)**

  📁 **[Minimal example - Checkered background (NumPy)](../../examples/minimal_examples/pygame_minimal_checkered_background_2.py)**

## Scale background

- [How do i properly rescale an image on PyGame without it being badly cropped?](https://stackoverflow.com/questions/55319967/how-do-i-properly-rescale-an-image-on-pygame-without-it-being-badly-cropped/55321552#55321552)

- [How to scale an image by window size?](https://stackoverflow.com/questions/68424287/how-to-scale-an-image-by-window-size/68424354#68424354)  
  ![How to scale an image by window size?](https://i.sstatic.net/KIjG8.png)  

- [How to scale images to screen size in Pygame](https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame/73384976#73384976)

  📁 **[Minimal example - Scale background](../../examples/minimal_examples/pygame_minimal_display_scale_background_1.py)**

  📁 **[Minimal example - Scale background, keep aspect ratio](../../examples/minimal_examples/pygame_minimal_display_scale_background_2.py)**

## Scroll background

Related Stack Overflow questions:

- [Making the background move sideways in pygame](https://stackoverflow.com/questions/55050166/making-the-background-move-sideways-in-pygame/55068602#55068602)

  📁 **[Minimal example - Scroll background vertical](../../examples/minimal_examples/pygame_minimal_display_scroll_background_1.py)**

- [How to scroll the background surface in PyGame?](https://stackoverflow.com/questions/55319181/how-to-scroll-the-background-surface-in-pygame/55321731#55321731)  
  ![How to scroll the background surface in PyGame?](https://i.sstatic.net/QosjL.gif)

  📁 **[Minimal example - Scroll background vertical](../../examples/minimal_examples/pygame_minimal_display_scroll_background_2.py)**

- [How to move the background image with keys in pygame?](https://stackoverflow.com/questions/61039508/how-to-move-the-background-image-with-keys-in-pygame/61039821#61039821)
- [Pygame : Two layered scrolling background, can you help me?](https://stackoverflow.com/questions/55454487/pygame-two-layered-scrolling-background-can-you-help-me/55460386#55460386)

- [How to move the player across a one background image?](https://stackoverflow.com/questions/67736156/how-to-move-the-player-across-a-one-background-image/67741682#67741682)  
  ![How to move the player across a one background image?](https://i.sstatic.net/Mb09D.gif)

  📁 **[Minimal example - Scroll background with player](../../examples/minimal_examples/pygame_minimal_display_scroll_background_3.py)**

- [How to continuously move an image smoothly in Pygame?](https://stackoverflow.com/questions/67944873/how-to-continuously-move-an-image-smoothly-in-pygame/67946424#67946424)  
  ![How to continuously move an image smoothly in Pygame?](https://i.sstatic.net/7Rexy.gif)

- [How to move the player across a one background image?](https://stackoverflow.com/questions/67736156/how-to-move-the-player-across-a-one-background-image?noredirect=1#comment119731761_67736156)  
  ![How to move the player across a one background image?](https://i.sstatic.net/Mb09D.gif)

If you want to have a continuously repeating background, then you've to draw the background twice:

```lang.none
        +==================+
   +----||---------+------||------+
   |    ||         |      ||      |
   |    ||    1    |   2  ||      |
   |    ||         |      ||      |
   +----||---------+------||------+
        +==================+
```

You've to know the size of the screen. The size of the height background image should match the height of the screen. The width of the background can be different, but should be at least the with of the window (else the background has to be drawn more than 2 times).

```py
bg_w, gb_h = size
bg =  pygame.transform.smoothscale(pygame.image.load('background.image'), (bg_w, bg_h))
```

The background can be imagined as a endless row of tiles.
If you want to draw the background at an certain position `pos_x`, then you have to calculate the position of the tile relative to the screen by the modulo (`%`) operator. The position of the 2nd tile is shifted by the width of the background (`bg_w`):

```py
x_rel = pos_x % bg_w
x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w
```

Finally the background has to be _blit_ twice, to fill the entire screen:

```py
screen.blit(bg, (x_rel, 0))
screen.blit(bg, (x_part2, 0))
```

## Parallax background

Related Stack Overflow questions:

- [Issue while creating a parallax background in pygame](https://stackoverflow.com/questions/76931511/issue-while-creating-a-parallax-background-in-pygame/76931586#76931586)

- [How to make parallax scrolling work properly with a camera that stops at edges pygame](https://stackoverflow.com/questions/63712333/how-to-make-parallax-scrolling-work-properly-with-a-camera-that-stops-at-edges-p/74002486#74002486)
  ![How to make parallax scrolling work properly with a camera that stops at edges pygame](https://i.sstatic.net/9Ogyf.png)

  📁 **[Minimal example - Parallax background](../../examples/minimal_examples/pygame_minimal_parallax_background.py)**

Background scrolling is achieved by moving the background image. The image is drawn into the window with an offset and must be drawn twice:

```py
def draw_background(surf, bg_image, bg_x, bg_y):
    surf.blit(bg_image, (bg_x - surf.get_width(), bg_y))
    surf.blit(bg_image, (bg_x, bg_y))
```

For a background parallax effect, you need several background layers that you must move at different speeds. The back layers must be moved more slowly than the front layers. e.g.:

```py
bg_layer_1_x = (bg_layer_1_x - move_x) % 600
bg_layer_2_x = (bg_layer_2_x - move_x*0.75) % 600
bg_layer_3_x = (bg_layer_3_x - move_x*0.5) % 600
```

![How to make parallax scrolling work properly with a camera that stops at edges pygame](https://i.sstatic.net/SB6cp.gif)
