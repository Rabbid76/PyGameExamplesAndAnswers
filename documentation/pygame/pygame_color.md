[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Color

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