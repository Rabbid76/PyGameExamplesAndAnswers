[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"The first principle is that you must not fool yourself and you are the easiest person to fool."  
Richard P. Feynman

---

# Surface and image

Related Stack Overflow questions:

- [How to draw images and sprites in pygame?](https://stackoverflow.com/questions/8873219/how-to-draw-images-and-sprites-in-pygame/64630591#64630591)  
- **[Replace a rectangle with an Image in Pygame](https://stackoverflow.com/questions/69634473/replace-a-rectangle-with-an-image-in-pygame/69634652#69634652)**  
  ![Replace a rectangle with an Image in Pygame](https://i.sstatic.net/dWhMB.gif)
- [Import a player icon and replace a block](https://stackoverflow.com/questions/74963599/import-a-player-icon-and-replace-a-block/74964284#74964284)  
  ![Import a player icon and replace a block](https://i.sstatic.net/w04pH.gif)  
- [What is the difference between pygame.draw.rect and screen_surface.blit()?](https://stackoverflow.com/questions/65964467/what-is-the-difference-between-pygame-draw-rect-and-screen-surface-blit/65965806#65965806)  
- [What is the difference between pygame sprite and surface?](https://stackoverflow.com/questions/66665946/what-is-the-difference-between-pygame-sprite-and-surface/66667420#66667420)  

## Surface rectangle

Related Stack Overflow questions:

- **[Why is my collision test always returning 'true' and why is the position of the rectangle of the image always wrong (0, 0)?](https://stackoverflow.com/questions/57730329/pygame-collide-rect-function-always-returning-true/57730378#57730378)**
  
- [Pygame Surface Positioning](https://stackoverflow.com/questions/61155292/pygame-surface-positioning/61155335#61155335)

- **[How to center an image in the middle of the window in pygame?](https://stackoverflow.com/questions/70530062/how-to-center-an-image-in-the-middle-of-the-window-in-pygame/70530198#70530198)**

- [Is there a way to place number on the center of the screen in pygame?](https://stackoverflow.com/questions/62728473/is-there-a-way-to-place-number-on-the-center-of-the-screen-in-pygame/62728692#62728692)
- [How to Center Text in Pygame](https://stackoverflow.com/questions/23982907/pygame-how-to-center-text/64660744#64660744)

[`pygame.Surface.get_rect()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect) returns a rectangle with the size of the _Surface_ object, that always starts at (0, 0) since a _Surface_ object has no position. A _Surface_ is `blit` at a position on the screen. The position of the rectangle can be specified by a keyword argument. For example, the center of the rectangle can be specified with the keyword argument `center`. These keyword argument are applied to the attributes of the [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) before it is returned (see [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) for a full list of the keyword arguments).

[`pygame.Surface.get_rect.get_rect()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect) returns a rectangle with the size of the _Surface_ object, but it returns a rectangle that always starts at (0, 0) since a _Surface_ object has no position.  
The _Surface_ is placed at a position on the display with the `blit` function.  

You've to set the location of the rectangle, either by a keyword argument, e.g:

```py
self.rect = self.image.get_rect(topleft = (self.x, self.y))
```

or an assignment to a virtual attribute (see [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html)), e.g:

```py
self.rect = self.image.get_rect()
self.rect.topleft = (self.x, self.y)
```

## Surface relativity

Related Stack Overflow questions:

- [texts are not shown on pygame screen](https://stackoverflow.com/questions/68734429/texts-are-not-shown-on-pygame-screen/68736231#68736231)  
  [texts are not shown on pygame screen](https://i.sstatic.net/Cn2YY.png)

## Surface format and performance

Related Stack Overflow questions:

- [Any way to speed up Python and Pygame?](https://stackoverflow.com/questions/6395923/any-way-to-speed-up-python-and-pygame/73992545#73992545)  
- [Runtime question - loading and bliting images](https://stackoverflow.com/questions/70530804/runtime-question-loading-and-bliting-images/70530926#70530926)  
- [Lag when win.blit() background pygame](https://stackoverflow.com/questions/59312019/lag-when-win-blit-background-pygame/59318946#59318946)
- [Why does my game made with Pygame suddenly lag for a few seconds?](https://stackoverflow.com/questions/60222282/why-does-my-game-made-with-pygame-suddenly-lag-for-a-few-seconds/60222744#60222744)
- [How Can I Improve My Terrain Generator Performance I Get 40 FPS](https://stackoverflow.com/questions/66509002/how-can-i-improve-my-terrain-generator-performance-i-get-40-fps/66510253#66510253)
- [What is the pygame window class?](https://stackoverflow.com/questions/66877518/what-is-the-pygame-window-class/66877658#66877658)

Ensure that the image _Surface_ has the same format as the display _Surface_. Use [`convert()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert) (or [`convert_alpha()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha)) to create a _Surface_ that has the same pixel format. This improves performance when the image is `blit` on  the display, because the formats are compatible and `blit` does not need to perform an implicit transformation.

```py
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png').convert()
```

Note, if the surface has a different format than the display, then `blit` has to convert the format on the fly in every frame.

## Draw an image

Related Stack Overflow questions:

- [How to Display Sprites in Pygame?](https://stackoverflow.com/questions/59348409/how-to-display-sprites-in-pygame/65368394#65368394)
- [A Python Programming Road Block Type Error: 'pygame.Surface' object is not callable How to Fix](https://stackoverflow.com/questions/50630244/a-python-programming-road-block-type-error-pygame-surface-object-is-not-calla/65493234#65493234)  
- [pygame : Trying to use the “area” tag in Surface.blit()](https://stackoverflow.com/questions/66641379/pygame-trying-to-use-the-area-tag-in-surface-blit/66641661#66641661)

## Subsurface and pixel array

### Subsurface

Related Stack Overflow questions:

- [ How to blit from the x and y coordinates of an image in Pygame?](https://stackoverflow.com/questions/65828379/how-to-blit-from-the-x-and-y-coordinates-of-an-image-in-pygame/65828456#65828456)  
- [How can I crop an image with Pygame?](https://stackoverflow.com/questions/6239769/how-can-i-crop-an-image-with-pygame/65627793#65627793)  
- [How to save all pixels that were in the place of a rect in pygame?](https://stackoverflow.com/questions/65858276/how-to-save-all-pixels-that-were-in-the-place-of-a-rect-in-pygame/65858324#65858324)  
- [How do I draw part of the sprite image using pygame spritegroups?](https://stackoverflow.com/questions/67454504/how-do-i-draw-part-of-the-sprite-image-using-pygame-spritegroups/67454693#67454693)  

There are 2 possibilities.

The [`blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) method allows to specify a rectangular sub-area of the source _Surface:

> [...] An optional area rectangle can be passed as well. This represents a smaller portion of the source Surface to draw. [...]

In this way you can `blit` an area of the source surface directly onto a target:

```py
cropped_region = (x, y, width, height)
traget.blit(source_surf, (posx, posy), cropped_region)
```

Alternatively, you can define a subsurface that is directly linked to the source surface with the [`subsurface`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface) method: 

> Returns a new Surface that shares its pixels with its new parent. The new Surface is considered a child of the original. Modifications to either Surface pixels will effect each other.

As soon as a subsurface has been created, it can be used as a normal surface at any time:

```py
cropped_region = (x, y, width, height)
cropped_subsurf = source_surf.subsurface(cropped_region)
``` 

```py
traget.blit(cropped_subsurf, (posx, posy))
```

### Pixel array

Related Stack Overflow questions:

- [Speed up double for loop PyGame draw](https://stackoverflow.com/questions/61856330/speed-up-double-for-loop-pygame-draw/61856399#61856399)  
- [pixel image to tile map](https://stackoverflow.com/questions/29133065/pixel-image-to-tile-map/65966555#65966555)  
- [Get RGB pixel data of a section of a screen as an array in pygame](https://stackoverflow.com/questions/68414745/get-rgb-pixel-data-of-a-section-of-a-screen-as-an-array-in-pygame/68414812#68414812)  

## Transparent surface and color key

Related Stack Overflow questions:

- [How do I blit a PNG with some transparency onto a surface in Pygame?](https://stackoverflow.com/questions/1634208/how-do-i-blit-a-png-with-some-transparency-onto-a-surface-in-pygame/64630678#64630678)  
  ![How do I blit a PNG with some transparency onto a surface in Pygame?](https://i.sstatic.net/a62px.png)

  📁 **[Minimal example - Load transparent image](../../examples/minimal_examples/pygame_minimal_surface_load_2.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-LoadTransparentImage](https://replit.com/@Rabbid76/PyGame-LoadTransparentImage#main.py)**

- [How do you blit/draw a sprite in Pygame with lower opacity?](https://stackoverflow.com/questions/65259552/how-do-you-blit-draw-a-sprite-in-pygame-with-lower-opacity)

- [Pygame Surface.set_at is setting alpha to 255?](https://stackoverflow.com/questions/65906914/pygame-surface-set-at-is-setting-alpha-to-255/65906942#65906942)

### Make a uniform colored background transparent

Related Stack Overflow questions:

- [How can I make an Image with a transparent Backround in Pygame?](https://stackoverflow.com/questions/62623341/how-can-i-make-an-image-with-a-transparent-backround-in-pygame/62623422#62623422)
- [How to convert the background color of image to match the color of Pygame window?](https://stackoverflow.com/questions/63976450/how-to-convert-the-background-color-of-image-to-match-the-color-of-pygame-window/63976738#63976738)  
  ![How to convert the background color of image to match the color of Pygame window?](https://i.sstatic.net/56y1w.png)
- [How do I make the screen ignore the background color of some image?](https://stackoverflow.com/questions/55648488/how-do-i-make-the-screen-ignore-the-background-color-of-some-image/55654549#55654549)
- [pygame image background does not match main background](https://stackoverflow.com/questions/62689244/pygame-image-background-does-not-match-main-background/62689442#62689442)
- [Pygame image transparency confusion](https://stackoverflow.com/questions/64704789/pygame-image-transparency-confusion/64704923#64704923)

Most likely, your image is not transparent at all. The transparency is stored in the alpha value. Compared to JPG and BMP, the PNG and GIF formats offer an alpha value per pixel. Converting an image to PNG or GIF format does not make an image transparent. You need to paint or download a transparent image.

The pygame documentation notes that:

> The returned Surface will contain the same color format, colorkey and alpha transparency as the file it came from. You will often want to call [`convert()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert) with no arguments, to create a copy that will draw more quickly on the screen.  
> For alpha transparency, like in .png images, use the [`convert_alpha()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha) method after loading so that the image has per pixel transparency.

Hence if your image provides per pixel alpha, it is recommended that you call `convert_alpha()`, but this is not required.

If your image has not transparent pixel, but a uniform colored background, set a transparent color key with [`set_colorkey()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_colorkey)

The color key specifies the color that is treated as transparent. For example, if you have an image with a black background that should be transparent, set a black color key:

```py
my_surface.set_colorkey((0, 0, 0))
```

### Create transparent Surface

Related Stack Overflow questions:

- [How to make a surface with a transparent background in pygame](https://stackoverflow.com/questions/328061/how-to-make-a-surface-with-a-transparent-background-in-pygame/64512639#64512639)  

You have 3 possibilities:

- Set a transparent color key with [`set_colorkey()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_colorkey)

  The color key specifies the color that is treated as transparent. For example, if you have an image with a black background that should be transparent, set a black color key:

  ```py
  my_surface.set_colorkey((0, 0, 0))
  ```

- You can enable additional functions when creating a new surface. Set the [`SRCALPHA`](https://www.pygame.org/docs/ref/surface.html) flag to create a surface with an image format that includes a per-pixel alpha. The initial value of the pixels is (0, 0, 0, 0):

  ```py
  my_surface = pygame.Surface((width, height), pygame.SRCALPHA)
  ```

- Use [`convert_alpha()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha) to create a copy of the _Surface_ with an image format that provides alpha per pixel.

  However, if you create a new surface and use `convert_alpha()`, the alpha channels are initially set to maximum. The initial value of the pixels is (0, 0, 0, 255). You need to fill the entire surface with a transparent color before you can draw anything on it:

  ```py
  my_surface = pygame.Surface((width, height))
  my_surface = my_surface.convert_alpha()
  my_surface.fill((0, 0, 0, 0))
  ```

You don't need to change the background color of the image to the background color of the window, but make the background of the image transparent.

Set the transparent color key by [`pygame.Surface.set_colorkey`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_colorkey):

> Set the current color key for the Surface. When blitting this Surface onto a destination, any pixels that have the same color as the colorkey will be transparent.

The white artifacts you can see in the picture are caused because the [JPG](https://en.wikipedia.org/wiki/JPEG) format is a compressed format.  
The compression is not lossless. This means the colors around the weapon are not  exactly white (255, 255, 255). The color appear to be white for the human eye, but actually the color channels have a value lass than 255, but near to 255.  

You can try to correct this manually. Ensure that format of the image has an alpha channel by [`pygame.Surface.convert_alpha()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha). Identify all the pixel, which have a red green and blue color channel above a certain threshold (e.g. 230). Change the color channels and the alpha channel of those pixels to (0, 0, 0, 0):

```py
img = pygame.image.load(IMAGE).convert_alpha()

threshold = 230
for x in range(img.get_width()):
    for y in range(img.get_height()):
        color = img.get_at((x, y))
        if color.r > threshold and color.g > threshold and color.b > threshold:
            img.set_at((x, y), (0, 0, 0, 0))
```

Of course you are in danger to change pixels which you don't want to change to. If the weapon would have some very "bright" areas, then this areas my become transparent, too.

Note, an issue like this can be avoided by using a different image format like [BMP](https://en.wikipedia.org/wiki/BMP_file_format) or [PNG](https://de.wikipedia.org/wiki/Portable_Network_Graphics).  
With this formats the pixel can be stored lossless.
You can try to "photo shop" the image. Manually change the pixel around the weapon and store the image with a different format.

## Negative image

Related Stack Overflow questions:

- [PyGame Negative Color / Surface](https://stackoverflow.com/questions/63665826/pygame-negative-color-surface/63665904#63665904)

## Floating point

Related Stack Overflow questions:

- [How to fix this DeprecationWarning](https://stackoverflow.com/questions/59336922/how-to-fix-this-deprecationwarning/59336966#59336966)
- [Using a function closes pygame window](https://stackoverflow.com/questions/60474292/using-a-function-closes-pygame-window/60474405#60474405)
- [Invalid destination position for blit error](https://stackoverflow.com/questions/63582946/invalid-destination-position-for-blit-error/63583200#63583200)

## Load image

Related Stack Overflow questions:

- [What is a good way to draw images using pygame?](https://stackoverflow.com/questions/8873219/what-is-a-good-way-to-draw-images-using-pygame/64630591#64630591)
- [How do I blit a PNG with some transparency onto a surface in Pygame?](https://stackoverflow.com/questions/1634208/how-do-i-blit-a-png-with-some-transparency-onto-a-surface-in-pygame/64630678#64630678)

Images are represented by ["pygame.Surface"](https://www.pygame.org/docs/ref/surface.html) objects. A _Surface_ can be created from an image with [`pygame.image.load`](https://www.pygame.org/docs/ref/image.html):

```py
my_image_surface = pygame.load.image('my_image.jpg')
```

However, the pygame documentation notes that:

> The returned Surface will contain the same color format, colorkey and alpha transparency as the file it came from. You will often want to call [`convert()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert) with no arguments, to create a copy that will draw more quickly on the screen.  
> For alpha transparency, like in .png images, use the [`convert_alpha()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha) method after loading so that the image has per pixel transparency.

Use the appropriate conversion method for best performance:

```py
image_surface = pygame.load.image('my_image.jpg').convert()
```

```py
alpha_image_surface = pygame.load.image('my_icon.png').convert_alpha()
```

A _Surface_ can be drawn on or blended with another _Surface_ using the [`blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) method. The first argument to blit is the _Surface_ that should be drawn. The second argument is either a tuple (_x_, _y_) representing the upper left corner or a rectangle. With a rectangle, only the upper left corner of the rectangle is taken into account. It should be mentioned that the window respectively display is also represented by a _Surface_. Therefore, drawing a _Surface_ in the window is the same as drawing a _Surface_ on a _Surface_:

```py
window_surface.blit(image_surface, (x, y))
```

```py
window_surface.blit(image_surface,
    image_surface.get_rect(center = window_surface.get_rect().center))
```

📁 **[Minimal example - Load image](../../examples/minimal_examples/pygame_minimal_surface_load_1.py)**

![What is a good way to draw images using pygame?](https://i.sstatic.net/FZ2OT.png)

📁 **[Minimal example - Load transparent image](../../examples/minimal_examples/pygame_minimal_surface_load_2.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-LoadTransparentImage](https://replit.com/@Rabbid76/PyGame-LoadTransparentImage#main.py)**

![How do I blit a PNG with some transparency onto a surface in Pygame?](https://i.sstatic.net/a62px.png)

### Load multiple images

Related Stack Overflow questions:

- [How do you load all images at a time in pygame?](https://stackoverflow.com/questions/67141356/how-do-you-load-all-images-at-a-time-in-pygame/67141422#67141422)

  📁 **[Minimal example - Load all images from directory](../../examples/minimal_examples/pygame_minimal_surface_load_all_From_directory.py)**

Get a list of all the files in the directory (see [os](https://docs.python.org/3/library/os.html)) and create a dictionary with the loaded files:

```py
path = 'Desktop/Files/Dungeon Minigame/'
filenames = [f for f in os.listdir(path) if f.endswith('.png')]
images = {}
for name in filenames:
    imagename = os.path.splitext(name)[0] 
    images[imagename] = pygame.image.load(os.path.join(path, name)).convert_alpha()
```

You can access the images in the dictionary by its name:

```py
screen.blit(images['background'], (0, 0))
```

Alternatively you can add variables to global namespace, using `globals()`:

```py
path = 'Desktop/Files/Dungeon Minigame/'
filenames = [f for f in os.listdir(path) if f.endswith('.png')]
for name in filenames:
    imagename = os.path.splitext(name)[0] 
    globals()[imagename] =  pygame.image.load(os.path.join(path, name)).convert_alpha()
```

```py
screen.blit(background, (0, 0))
```

### Image load performance (lagging)

Related Stack Overflow questions:

- [Pygame is running slow](https://stackoverflow.com/questions/61134825/pygame-is-running-slow/61134941#61134941)
- [Why my pygame game with a tiled map is lagging?](https://stackoverflow.com/questions/62136440/why-my-pygame-game-with-a-tiled-map-is-lagging/62137296#62137296)  
- [How could I optimise this simple python pygame code](https://stackoverflow.com/questions/65384623/how-could-i-optimise-this-simple-python-pygame-code/65384691#65384691)  
- [Image position not updating / updates slower while moving mouse](https://stackoverflow.com/questions/57846536/image-position-not-updating-updates-slower-while-moving-mouse/65626207#65626207)  

### Load Pillow image

Related Stack Overflow questions:

- [PIL and pygame.image](https://stackoverflow.com/questions/25202092/pil-and-pygame-image/64182629#64182629)

```py
def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
```

📁 **[Minimal example - Load PIL image to PyGame _Surface_](../../examples/minimal_examples/pygame_minimal_surface_load_from_pil.py)**

### Load SVG

[Scalable  Vector Graphics (SVG)](https://de.wikipedia.org/wiki/Scalable_Vector_Graphics)

**Since 2.0.2, SDL Image supports SVG ([Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)) files (see [SDL_image 2.0](https://www.libsdl.org/projects/SDL_image)). Therefore, with pygame version 2.0.1, SVG files can be loaded into a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object with  [`pygame.image.load()`](http://www.pygame.org/docs/ref/image.html)**:

```py
surface = pygame.image.load('my.svg')
```

Before Pygame 2, you had to implement [Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) loading with other libraries. Below are some ideas on how to do this.

See [Surface and image, load SVG](pygame_surface_and_image_svg.md)

### Animate Sprite

Related Stack Overflow questions:

- [how to create an illusion of animations in pygame](https://stackoverflow.com/questions/71229981/how-to-create-an-illusion-of-animations-in-pygame/71232110#71232110)  
- [Playing multiple animations at the same time in pygame](https://stackoverflow.com/questions/74744198/playing-multiple-animations-at-the-same-time-in-pygame/74744315#74744315)  
  ![Playing multiple animations at the same time in pygame](https://i.sstatic.net/MVOaZ.gif)

### Load Sprite Sheet

[Spritesheet](https://www.pygame.org/wiki/Spritesheet).

Related Stack Overflow questions:

- **[How do I create animated sprites using Sprite Sheets in Pygame?](https://stackoverflow.com/questions/55200501/how-do-i-create-animated-sprites-using-sprite-sheets-in-pygame/55200625#55200625)**  
  ![How do I create animated sprites using Sprite Sheets in Pygame?](https://i.sstatic.net/Ekuju.gif)

📁 **[Minimal example - Load Sprite Sheet](../../examples/minimal_examples/pygame_minimal_surface_load_sprite_sheet.py)**

- [Invalid destination position for blit error, not seeing how](https://stackoverflow.com/questions/55199591/invalid-destination-position-for-blit-error-not-seeing-how/55199736#55199736)

### Load animated GIF

- [Animated sprite from few images](https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images/64668964#64668964)  
  ![Animated sprite from few images](https://i.sstatic.net/SzKwL.gif)

- [How can I load an animated GIF and get all of the individual frames in PyGame?](https://stackoverflow.com/questions/29571399/how-can-i-load-an-animated-gif-and-get-all-of-the-individual-frames-in-pygame)
- [How do I make a sprite as a gif in pygame?](https://stackoverflow.com/questions/64179680/how-do-i-make-a-sprite-as-a-gif-in-pygame/64182074#64182074)

- [PyGame OR Moviepy - Show a video with transparency](https://stackoverflow.com/questions/66829740/pygame-or-moviepy-show-a-video-with-transparency?noredirect=1#comment118133434_66829740)  
  ![PyGame OR Moviepy - Show a video with transparency](https://i.sstatic.net/yUxaz.gif)

[PyGame](https://www.pygame.org/news) respectively the [`pygame.image`](https://www.pygame.org/docs/ref/image.html) module can only handle non-animated [GIFs](https://en.wikipedia.org/wiki/GIF).  
But on the PyGame homepage is introduced the [GIFImage](https://www.pygame.org/project-GIFImage-1039-.html) library:

> This library adds GIF animation playback to pygame.

Another option is to use a library to load the GIF frame by frame to a list.

For instance use the [Pillow](https://pillow.readthedocs.io/en/stable/) library ([_pip install Pillow_](https://pypi.org/project/Pillow/)).

Write a function, that can convert a PIL image to a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) and use the PIL library to load a GIF frame by frame:  
(see also [Extracting The Frames Of An Animated GIF Using Pillow](https://pythontic.com/image-processing/pillow/extract%20frames%20from%20animated%20gif) and [PIL and pygame.image](https://stackoverflow.com/questions/25202092/pil-and-pygame-image))  

```py
from PIL import Image, ImageSequence
```

```py
def pilImageToSurface(pilImage):
    mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
    return pygame.image.fromstring(data, size, mode).convert_alpha()

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    if pilImage.format == 'GIF' and pilImage.is_animated:
        for frame in ImageSequence.Iterator(pilImage):
            pygameImage = pilImageToSurface(frame.convert('RGBA'))
            frames.append(pygameImage)
    else:
        frames.append(pilImageToSurface(pilImage))
    return frames
```

Or use [OpenCV](https://opencv.org/)/[_opencv-python_](https://pypi.org/project/opencv-python/) library and [`VideoCapture`](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)

Write a function, that can convert a cv2 [`pygame.image`](https://www.pygame.org/docs/ref/image.html) image to a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) a nd use the library to load a GIF frame by frame:  
(see also [Read GIF files in Python](https://www.facebook.com/MLandDS/posts/read-gif-files-in-pythonimport-cv2from-pil-import-imagegif-cv2videocapturemy_fil/2397352997206918/) and [How do I convert an OpenCV (cv2) image (BGR and BGRA) to a pygame.Surface object](https://stackoverflow.com/questions/64183409/how-do-i-convert-an-opencv-cv2-image-bgr-and-bgra-to-a-pygame-surface-object/64183410#64183410))  

```py
import cv2
```

```py
def cv2ImageToSurface(cv2Image):
    size = cv2Image.shape[1::-1]
    format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
    cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.tostring(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()

def loadGIF(filename):
    gif = cv2.VideoCapture(filename)
    frames = []
    while True:
        ret, cv2Image = gif.read()
        if not ret:
            break
        pygameImage = cv2ImageToSurface(cv2Image)
        frames.append(pygameImage)
    return frames
```

📁 **[Minimal example - Load animated GIF PyGame _Surface_ list using cv2](../../examples/minimal_examples/pygame_minimal_surface_load_frames_gif_cv2.py)**

📁 **[Minimal example - Load animated GIF PyGame _Surface_ list using PLI](../../examples/minimal_examples/pygame_minimal_surface_load_frames_gif_pil.py)**

![How can I load an animated GIF and get all of the individual frames in PyGame?](https://i.sstatic.net/geYjP.gif)

## Store Image (Save image)

Related Stack Overflow questions:

- [Save created image to file system python and pygame](https://stackoverflow.com/questions/68804453/save-created-image-to-file-system-python-and-pygame/68805404#68805404)  
- [How to output pygame.image.save to a variable instead of a file?](https://stackoverflow.com/questions/65405520/how-to-output-pygame-image-save-to-a-variable-instead-of-a-file/65405567#65405567)  
- [Is there any way to convert the screen of a pygame gui into an image somehow?](https://stackoverflow.com/questions/60880169/is-there-any-way-to-convert-the-screen-of-a-pygame-gui-into-an-image-somehow/65543336#65543336)  

- [pygame, saving a image with low opacity](https://stackoverflow.com/questions/73802557/pygame-saving-a-image-with-low-opacity/73802685#73802685)  

The image format must be one that supports an alpha channel (e.g. PNG):

```py
pygame.image.save(the_img, "my_image.png")
```

If you have a Surface with a color key ([`set_colorkey`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_colorkey)), you have to change the pixel format of the image including per pixel alphas with [`pygame.Surface.convert_alpha`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha):

```py
pygame.image.save(the_img.convert_alpha(), the_name)
```

If you have a surface with a global alpha value ([`set_alpha`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_alpha)), you need to `blit` the Surface on a transparent Surface (`pygame.SRCALPHA`) of the same size and store that transparent Surface (this also works for a Surface with a color key):

```py
the_img.set_colorkey((0, 0, 0))
the_img_alpha = pygame.Surface(the_img.get_size(), pygame.SRCALPHA)
the_img_alpha.blit(the_img, (0, 0))

pygame.image.save(the_img_alpha, the_name)
```

📁 **[Minimal example - Scroll](../../examples/minimal_examples/pygame_minimal_save_transparent_surface.py)**

## Surface lock

Related Stack Overflow questions:

- [How do I save a section of a pygame screen and blit it to another location?](https://stackoverflow.com/questions/56420746/how-do-i-save-a-section-of-a-pygame-screen-and-blit-it-to-another-location/56421239#56421239)

## Transformation

Related Stack Overflow questions:

- [Pygame rotozoom rescaling the image out of bounds](https://stackoverflow.com/questions/65899193/pygame-rotozoom-rescaling-the-image-out-of-bounds/65899347#65899347)

### Flip

Related Stack Overflow questions:

- [How to Flip Image in Pygame](https://stackoverflow.com/questions/65834797/how-to-flip-image-in-pygame)  

### Scale

See [Scale and zoom](pygame_surface_scale_and_zoom.md)

### Rotate

See [Rotate surface](pygame_surface_rotate.md)

### Scroll

Related Stack Overflow questions:

- [Adjust image of rect](https://stackoverflow.com/questions/66443304/adjust-image-of-rect/66443370#66443370)  
  ![Adjust image of rect](https://i.sstatic.net/r0wY5.gif)

  📁 **[Minimal example - Scroll](../../examples/minimal_examples/pygame_minimal_surface_scroll_1.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-SCroll](https://replit.com/@Rabbid76/PyGame-Scroll#main.py)**

### Blur

- [How to blur the edges of a surface in Pygame?](https://stackoverflow.com/questions/77117250/how-to-blur-the-edges-of-a-surface-in-pygame/77117325#77117325)  
  ![How to blur the edges of a surface in Pygame?](https://i.sstatic.net/0COhi.png)

  📁 **[Minimal example - BLur edge](../../examples/minimal_examples/pygame_minimal_blur_and_blit.py)**
