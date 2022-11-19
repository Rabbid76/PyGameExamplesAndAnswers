[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Programmers must avoid leaving false clues that obscure the meaning of code."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Blending and transparency

## Blending

Related Stack Overflow questions:

- [Why is alpha blending not working properly?](https://stackoverflow.com/questions/54342525/why-is-alpha-blending-not-working-properly-pygame/54348618#54348618)  
  ![Why is alpha blending not working properly?](https://i.stack.imgur.com/OiIzC.gif)

  :scroll: **[Minimal example - Blend surfaces](../../examples/minimal_examples/pygame_minimal_blend_surface.py)**

- [PyGame Negative Color / Surface](https://stackoverflow.com/questions/63665826/pygame-negative-color-surface/63665904#63665904)

- [How can I remove the black of some of the tile textures](https://stackoverflow.com/questions/54428774/how-can-i-remove-the-black-of-some-of-the-tile-textures/54429784#54429784)  

- [How to get the Difference blending mode?](https://stackoverflow.com/questions/67737854/how-to-get-the-difference-blending-mode/67737939#67737939)  
  ![How to get the Difference blending mode?](https://i.stack.imgur.com/KH59V.png)

  :scroll: **[Minimal example - Difference blend mode](../../examples/minimal_examples/pygame_minimal_blend_surface_difference_mode.py)**

The blending mode can be changed by setting the optional _special_flags_ argument of [`pygame.Surface.blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit):

> `blit(source, dest, area=None, special_flags=0) -> Rect`  
> [...]  
> New in pygame 1.8: Optional special_flags: `BLEND_ADD`, `BLEND_SUB`, `BLEND_MULT`, `BLEND_MIN`, `BLEND_MAX`.  
> New in pygame 1.8.1: Optional special_flags: `BLEND_RGBA_ADD`, `BLEND_RGBA_SUB`, `BLEND_RGBA_MULT`, `BLEND_RGBA_MIN`, `BLEND_RGBA_MAX`, `BLEND_RGB_ADD`, `BLEND_RGB_SUB`, `BLEND_RGB_MULT`, `BLEND_RGB_MIN`, `BLEND_RGB_MAX`.  
> New in pygame 1.9.2: Optional special_flags: `BLEND_PREMULTIPLIED`  
> New in pygame 2.0.0: Optional special_flags: `BLEND_ALPHA_SDL2` [...]

e.g.:

```py
screen.blit(image, (x, y), special_flags = pygame.BLEND_RGBA_SUB)
```

Unfortunately, Pygame doesn't have a blending mode that gives the absolute difference of 2 images. However it can be achieved with

`MAX(SUB(image1, imgage2), SUB(image2, image1))`

```py
image1 = pygame.image.load('image2.png')
image2 = pygame.image.load('image1.png')
temp_image = image1.copy() 
temp_image.blit(image2, (0, 0), special_flags = pygame.BLEND_RGBA_SUB)
final_image = image2.copy() 
final_image.blit(image1, (0, 0), special_flags = pygame.BLEND_RGBA_SUB)
final_image.blit(temp_image, (0, 0), special_flags = pygame.BLEND_RGBA_MAX)
```

![blend mode difference](https://i.stack.imgur.com/KH59V.png)

### Transparency

Related Stack Overflow questions:

- [How to make transparent pygame.draw.circle](https://stackoverflow.com/questions/59293057/how-to-make-transparent-pygame-draw-circle/59294087#59294087)  
  ![How to make transparent pygame.draw.circle](https://i.stack.imgur.com/nOoJj.png)  

- [python pygame set color transparency](https://stackoverflow.com/questions/59613548/python-pygame-set-color-transparency/59613903#59613903)  
  ![python pygame set color transparency](https://i.stack.imgur.com/VLpmO.png)  

- [How to fade in a text or an image with PyGame](https://stackoverflow.com/questions/54593653/how-to-fade-in-a-text-or-an-image-with-pygame/54594196#54594196)  
  ![How to fade in a text or an image with PyGame](https://i.stack.imgur.com/2mkKD.gif)

  :scroll: **[Minimal example - Blend text](../../examples/minimal_examples/pygame_minimal_blend_text.py)**

  ![How to fade in a text or an image with PyGame](https://i.stack.imgur.com/2mkKD.gif)  

- [Pygame: Frame ghosting?](https://stackoverflow.com/questions/20862695/pygame-frame-ghosting/73964785#73964785)  
  ![Pygame: Frame ghosting?](https://i.stack.imgur.com/odiIG.gif)

  :scroll: **[Minimal example - Blend frames](../../examples/minimal_examples/pygame_minimal_blend_text.py)**

### Change color of an image

#### Change the color of the full image area

Change the brightness, hue, or transparency of an entire image.

Related Stack Overflow questions:

- [How can I change the brightness of an image in pygame?](https://stackoverflow.com/questions/57962130/how-can-i-change-the-brightness-of-an-image-in-pygame/57962590#57962590)  

#### Tint a grayscale image

Related Stack Overflow questions:

remove "duplicate"

- **[Is it possible to change sprite colours in Pygame?](https://stackoverflow.com/questions/56209634/is-it-possible-to-change-sprite-colours-in-pygame/56210460#56210460)**  
  ![Is it possible to change sprite colours in Pygame?](https://i.stack.imgur.com/jTwph.gif)

  :scroll: **[Minimal example - Tint a grayscale image 2](../../examples/minimal_examples/pygame_minimal_blend_surface_tint_grayscale_2.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-4](https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-4#main.py)**

- [Changing colour of a surface without overwriting transparency](https://stackoverflow.com/questions/64190277/changing-colour-of-a-surface-without-overwriting-transparency/64193109#64193109/64193109#64193109)  
  ![Changing colour of a surface without overwriting transparency](https://i.stack.imgur.com/oldLt.gif)

  :scroll: **[Minimal example - Tint a grayscale image 1](../../examples/minimal_examples/pygame_minimal_blend_surface_tint_grayscale_1.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ChangeColorOfSpriteArea](https://replit.com/@Rabbid76/PyGame-ChangeColorOfSpriteArea#main.py)**

- [How to tint a png image with an alpha channel?](https://stackoverflow.com/questions/54633756/how-to-tint-a-png-image-with-an-alpha-channel/54635608#54635608)  

- [How to fill shape white](https://stackoverflow.com/questions/71276881/how-to-fill-shape-white/71276921#71276921)  
  ![How to fill shape white](https://i.stack.imgur.com/TWG3R.png)

#### Change the color of a surface area (mask)

Related Stack Overflow questions:

- **[Trying to make sections of sprite change colour, but whole sprite changes instead](https://stackoverflow.com/questions/58385570/trying-to-make-sections-of-sprite-change-colour-but-whole-sprite-changes-instea/58402923#58402923/58402923#58402923)**  
  ![Trying to make sections of sprite change colour, but whole sprite changes instead](https://i.stack.imgur.com/qotun.png)

  :scroll: **[Minimal example - Change color of Surface 1](../../examples/minimal_examples/pygame_minimal_blend_surface_change_color_1.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ChangeColorOfSurfaceArea](https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea#main.py)**

- [Changing ememy's color to show that it is asking damage?](https://stackoverflow.com/questions/63734429/changing-ememys-color-to-show-that-it-is-aking-damage/63745242#63745242)  
  ![Changing ememy's color to show that it is asking damage?](https://i.stack.imgur.com/CjV0r.gif)

  :scroll: **[Minimal example - Change color of Surface 2](../../examples/minimal_examples/pygame_minimal_blend_surface_change_color_2.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-2](https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-2#main.py)**

If you want to brighten an image, thenA I recommend to add a constant color to the surface. This can be achieved by [`.fill()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill), wby the use of the  special parameter `BLEND_RGB_ADD`. If the fill color is black (0, 0, 0) then the image won't change at all. If the fill color is white (255, 255, 255), then the entire image will become white. e.g.:  

```py
image = pygame.image.load(my_imagename)
brighten = 128
image.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD)
```

If you want to increase the transparency of the image, then yo can "blend" the image with a transparent color, by the use of the special flag `BLEND_RGBA_MULT` . Of course you've to ensure that the image format provides an alpha channel (e.g. [`.convert_alpha()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha)):

```py
image = pygame.image.load(my_imagename).convert_alpha()
transparency = 128
image.fill((255, 255, 255, transparency), special_flags=pygame.BLEND_RGBA_MULT)
```

If you want to change the color of a sprite, you actually need an image

![image](../../resource/icon/avatar64.png)

and a mask image. The mask image has just 2 color, black and white. The white areas of the mask define the areas in the image whose color needs to be changed:

![mask](../../resource/icon/avatar64mask.png)

The following function uses a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object `image`,  `pygame.Surface` object `maskImage` and a color (`newColor`), to create a new Surface. In the new Surface the color of the regions which are defined by `maskImage`, is changed to `newColor`:

```py
def changColor(image, maskImage, newColor):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(newColor)

    masked = maskImage.copy()
    masked.set_colorkey((0, 0, 0))
    masked.blit(colouredImage, (0, 0), None, pygame.BLEND_RGBA_MULT)

    finalImage = image.copy()
    finalImage.blit(masked, (0, 0), None)

    return finalImage
```

:scroll: **[Minimal example - Change color of Surface 3](../../examples/minimal_examples/pygame_minimal_blend_surface_change_color_3.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-3](https://replit.com/@Rabbid76/PyGame-ChangeColorOfSurfaceArea-3#main.py)**

![Trying to make sections of sprite change colour, but whole sprite changes instead](https://i.stack.imgur.com/F45EC.png)

## Intersection area

- [Fill the area of intersection of two Circles in PyGame](https://stackoverflow.com/questions/63058731/fill-the-area-of-intersection-of-two-circles-in-pygame/63060020#63060020)  
  ![Fill the area of intersection of two Circles in PyGame](https://i.stack.imgur.com/2ef0w.png)
  ![Fill the area of intersection of two Circles in PyGame](https://i.stack.imgur.com/zzHTY.png)

Create 2 [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) objects with per pixel alpha (`pygame.SRCALPHA`):

```py
surf1 = pygame.Surface((500, 500), pygame.SRCALPHA)
surf2 = pygame.Surface((500, 500), pygame.SRCALPHA)
```

Define the center point and radius of the 2 circles:

```py
pos1, rad1 = (250, 200), 100
pos2, rad2 = (250, 250), 80
```

Draw the circles on the 2 surfaces, with the same color:

```py
pygame.draw.circle(surf1, (255, 0, 0, 255), pos1, rad1)
pygame.draw.circle(surf2, (255, 0, 0, 255), pos2, rad2)
```

Blend one surface on the other, using the blend mode `pygame.BLEND_RGBA_MIN`:  

```py
surf1.blit(surf2, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
```

At this point `surf1` contains the intersection area of the 2 circles.

![Fill the area of intersection of two Circles in PyGame](https://i.stack.imgur.com/2ef0w.png)

To get the outer section, another step is required. Blend `surf1` on `surf2`, using the blend mode `pygame.BLEND_RGBA_MIN`:

```py
surf2.blit(surf1, (0, 0), special_flags = pygame.BLEND_RGBA_SUB)
```

Now `surf2` contains the the part of  _circle B_ which is left if _circle A_ is subtracted:

![Fill the area of intersection of two Circles in PyGame](https://i.stack.imgur.com/zzHTY.png)

---

[PyGame Negative Color / Surface](https://stackoverflow.com/questions/63665826/pygame-negative-color-surface/63665904#63665904)

You can use [`pygame.Surface.blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) with the *special_flag* argument `BLEND_SUB` for this.  
Create a completely white image with the same size and *subtract* the original image:

```py
neg = pygame.Surface(image.get_size())
neg.fill((255, 255, 255))
neg.blit(image, (0, 0), special_flags=pygame.BLEND_SUB)
```

:scroll: **[Minimal example - Fill the area of intersection](../../examples/minimal_examples/pygame_minimal_blend_intersection_area.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-CircleIntersection](https://replit.com/@Rabbid76/PyGame-CircleIntersection#main.py)**

 ![Fill the area of intersection of two Circles in PyGame](https://i.stack.imgur.com/2ef0w.png)
 ![Fill the area of intersection of two Circles in PyGame](https://i.stack.imgur.com/zzHTY.png)
