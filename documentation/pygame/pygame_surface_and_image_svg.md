[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"The first principle is that you must not fool yourself and you are the easiest person to fool."  
Richard P. Feynman

---

# Surface and image, load SVG

[Scalable  Vector Graphics (SVG)](https://de.wikipedia.org/wiki/Scalable_Vector_Graphics)

Related Stack Overflow questions:

- [SVG rendering in a PyGame application. Prior to Pygame 2.0, Pygame did not support SVG. Then how did you load it?](https://stackoverflow.com/questions/120584/svg-rendering-in-a-pygame-application-prior-to-pygame-2-0-pygame-did-not-suppo/64598021#64598021)  
  ![SVG rendering in a PyGame application. Prior to Pygame 2.0, Pygame did not support SVG. Then how did you load it?](https://i.stack.imgur.com/LOMwY.png)  
- [Display SVG (as string) on Python Pygame](https://stackoverflow.com/questions/65649933/display-svg-as-string-on-python-pygame/65651155#65651155)  
- [How can you draw more detailed/smoother images in pygame?](https://stackoverflow.com/questions/65492782/how-can-you-draw-more-detailed-smoother-images-in-pygame/65492828#65492828)  
- [Upscale an SVG image in python without losing its quality](https://stackoverflow.com/questions/69508937/upscale-an-svg-image-in-python-without-losing-its-quality/69509545#69509545)  
  ![Upscale an SVG image in python without losing its quality](https://i.stack.imgur.com/2VxvP.png)

**Since 2.0.2, SDL Image supports SVG ([Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)) files (see [SDL_image 2.0](https://www.libsdl.org/projects/SDL_image)). Therefore, with pygame version 2.0.1, SVG files can be loaded into a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object with  [`pygame.image.load()`](http://www.pygame.org/docs/ref/image.html)**:

SFV File:

```py
surface = pygame.image.load('my.svg')
```

:scroll: **[Minimal example - Load Scalable Vector Graphics (SVG) file in PyGame](../../examples/minimal_examples/pygame_minimal_surface_load_svg_1.py)**

SVG binary string

```py
pygame_surface = pygame.image.load(io.BytesIO(svg_string.encode()))
```

:scroll: **[Minimal example - Load Scalable Vector Graphics (SVG) string in PyGame](../../examples/minimal_examples/pygame_minimal_surface_load_svg_2.py)**

Scale SVG:

```py
def load_and_scale_svg(filename, scale):
    svg_string = open(filename, "rt").read()
    start = svg_string.find('<svg')    
    if start > 0:
        svg_string = svg_string[:start+4] + f' transform="scale({scale})"' + svg_string[start+4:]
    return pygame.image.load(io.BytesIO(svg_string.encode()))

pygame_surface = load_and_scale_svg('my.svg', 0.5)
```

:scroll: **[Minimal example - Load and scale Scalable Vector Graphics (SVG) file in PyGame](../../examples/minimal_examples/pygame_minimal_surface_load_svg_3.py)**

## Legacy SVG loading

Before Pygame 2, you had to implement [Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) loading with other libraries. Below are some ideas on how to do this.

A very simple solution is to use [CairoSVG](https://cairosvg.org/). With the function `cairosvg.svg2png`, an [Vector Graphics (SVG)](https://de.wikipedia.org/wiki/Scalable_Vector_Graphics) files can be directly converted to an [Portable Network Graphics (PNG)] file

Install [CairoSVG](https://pypi.org/project/CairoSVG/).

```lang-none
pip install CairoSVG
```

Write a function that converts a SVF file to a PNG ([`ByteIO`](https://docs.python.org/3/library/io.html)) and creates a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object may look as follows:

```py
import cairosvg
import io

def load_svg(filename):
    new_bites = cairosvg.svg2png(url = filename)
    byte_io = io.BytesIO(new_bites)
    return pygame.image.load(byte_io)
```

:scroll: **[Minimal example - Load Scalable Vector Graphics (SVG) in PyGame _Surface_ (cairosvg)](../../examples/minimal_examples/pygame_minimal_surface_load_svg_legacy_3.py)**

An alternative is to use _svglib_. However, there seems to be a problem with transparent backgrounds. There is an issue about this topic [How to make the png background transparent? #171](https://github.com/deeplook/svglib/issues/171).  

Install [svglib](https://pypi.org/project/svglib/).

```lang-none
pip install svglib
```

A function that parses and rasterizes an SVG file and creates a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object may look as follows:

```py
def load_svg(filename):
    drawing = svg2rlg(filename)
    str = drawing.asString("png")
    byte_io = io.BytesIO(str)
    return pygame.image.load(byte_io)
```

:scroll: **[Minimal example - Load Scalable Vector Graphics (SVG) in PyGame _Surface_ (svglib)](../../examples/minimal_examples/pygame_minimal_surface_load_svg_legacy_2.py)**

Anther simple solution is to use _pynanosvg_. The downside of this solution is that _nanosvg_ is no longer actively supported and does not work with Python 3.9. [pynanosvg](https://github.com/ethanhs/pynanosvg) can be used to load and rasterize [Vector Graphics (SVG)](https://de.wikipedia.org/wiki/Scalable_Vector_Graphics) files. Install [Cython](https://cython.org/) and [pynanosvg](https://github.com/ethanhs/pynanosvg):

```lang-none
pip install Cython
pip install pynanosvg
```

The SVG file can be read, rasterized and loaded into a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object with the following function:

```py
def load_svg(filename, scale=None, size=None, clip_from=None, fit_to=None, foramt='RGBA'):
    svg = Parser.parse_file(filename)
    scale = min((fit_to[0] / svg.width, fit_to[1] / svg.height)
                if fit_to else ([scale if scale else 1] * 2))
    width, height = size if size else (svg.width, svg.height)
    surf_size = round(width * scale), round(height * scale)
    buffer = Rasterizer().rasterize(svg, *surf_size, scale, *(clip_from if clip_from else 0, 0))
    return  pygame.image.frombuffer(buffer, surf_size, foramt)
```

:scroll: **[Minimal example - Load Scalable Vector Graphics (SVG) to PyGame _Surface_ (pynanosvg)](../../examples/minimal_examples/pygame_minimal_surface_load_svg_legacy_1.py)**
