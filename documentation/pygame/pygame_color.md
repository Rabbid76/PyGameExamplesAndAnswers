[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Color

- [How do I invert a pygame color?](https://stackoverflow.com/questions/65041283/how-do-i-invert-a-pygame-color/65041334#65041334)

## HSV/HSL

Related Stack Overflow questions:

- [HSV to RGB Color Conversion](https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion)

The [`pygame.Color`](https://www.pygame.org/docs/ref/color.html#pygame.Color) object can be used to convert between the RGB and [HSL/HSV](HSL and HSV) color schemes.

The [`hsva`](https://www.pygame.org/docs/ref/color.html#pygame.Color.hsva) property:

> Gets or sets the HSVA representation of the Color. The HSVA components are in the ranges H = [0, 360], S = [0, 100], V = [0, 100], A = [0, 100].

```py
hsva = pygame.Color((red, green, blue, alpha)).hsva
```

```py
color = pygame.Color(0)
color.hsva = (hue, saturation, value, alpha)
rgba = (color.r, color.g, color.b, color.a)
```

The [`hsla`](https://www.pygame.org/docs/ref/color.html#pygame.Color.hsla) property:

> Gets or sets the HSLA representation of the Color. The HSLA components are in the ranges H = [0, 360], S = [0, 100], V = [0, 100], A = [0, 100].

```py
hsla = pygame.Color((red, green, blue, alpha)).hsla
```

```py
color = pygame.Color(0)
color.hsla = (hue, saturation, lightness, alpha)
rgba = (color.r, color.g, color.b, color.a)
```

:scroll: **[Minimal example - Set HSLA color](../../examples/minimal_examples/pygame_minimal_color_hsv_hsl.py)**

![HSV to RGB Color Conversion](https://i.stack.imgur.com/U314N.png)

## Gradient

- [How would I make a heatmap in pygame on a grid](https://stackoverflow.com/questions/55617119/how-would-i-make-a-heatmap-in-pygame-on-a-grid/55618024#55618024)  
  ![How would I make a heatmap in pygame on a grid](https://i.stack.imgur.com/4c4gB.gif)

  :scroll: **[Minimal example - Heatmap](../../examples/minimal_examples/pygame_minimal_color_gradient_1.py)**

- [Shifting the color value based on percentage from green to red using PyGame](https://stackoverflow.com/questions/65904437/shifting-the-color-value-based-on-percentage-from-green-to-red-using-pygame/65904561#65904561)  
  ![Shifting the color value based on percentage from green to red using PyGame](https://i.stack.imgur.com/Psxup.png)  
Shifting the color value based on percentage from green to red using PyGame

## Lerp

Related Stack Overflow questions:

- [Blending two pygame.Color objects together](https://stackoverflow.com/questions/69426379/blending-two-pygame-color-objects-together/69426709#69426709)  
  ![Blending two pygame.Color objects together](https://i.stack.imgur.com/ZhU7U.png)

  :scroll: **[Minimal example - Lerp two colors](../../examples/minimal_examples/pygame_minimal_color_lerp_1.py)**

- [How to fade from one colour to another in pygame?](https://stackoverflow.com/questions/51973441/how-to-fade-from-one-colour-to-another-in-pygame/68702388#68702388)  
  ![How to fade from one colour to another in pygame?](https://i.stack.imgur.com/VEAII.gif)

  :scroll: **[Minimal example - Lerp list of colors](../../examples/minimal_examples/pygame_minimal_color_lerp_2.py)**

Pygame provides the [`pygame.Color`](https://www.pygame.org/docs/ref/color.html#pygame.Color) object. The object can construct a color from various arguments (e.g. RGBA color channels, hexadecimal numbers, strings, ...).  
It also offers the handy method [`lerp`](https://www.pygame.org/docs/ref/color.html#pygame.Color.lerp), that can interpolate 2 colors: 

> Returns a Color which is a linear interpolation between self and the given Color in RGBA space

The [`pygame.Color`](https://www.pygame.org/docs/ref/color.html#pygame.Color.lerp) object and the [`lerp`](https://www.pygame.org/docs/ref/color.html#pygame.Color.lerp) method can be used to interpolate a color form a list of colors:

```py
def lerp_color(colors, value):
    fract, index = math.modf(value)
    color1 = pygame.Color(colors[int(index) % len(colors)])
    color2 = pygame.Color(colors[int(index + 1) % len(colors)])
    return color1.lerp(color2, fract)
``` 