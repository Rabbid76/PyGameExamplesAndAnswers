[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)
---

# Text and font

## Font

Related Stack Overflow questions:

- [Python display text with font & color?](https://stackoverflow.com/questions/10077644/python-display-text-with-font-color/64487335#64487335)
- [How to scale the font size in pygame based on display resolution?](https://stackoverflow.com/questions/56855775/how-to-scale-the-font-size-in-pygame-based-on-display-resolution/56857032#56857032)
- [I need to add text to my rectangles, how would I do this?](https://stackoverflow.com/questions/55511081/i-need-to-add-text-to-my-rectangles-how-would-i-do-this/55521100#55521100)
- [How to display some text in pygame?](https://stackoverflow.com/questions/58695609/how-to-display-some-text-in-pygame/58695757#58695757)

[Minimal `pygame.font` module example](../../examples/minimal_examples/pygame_minimal_text_font.py)

[Minimal `pygame.freetype` module example](../../examples/minimal_examples/pygame_minimal_text_freetype.py)

There are 2 possibilities. In either case PyGame has to be initialized by [`pygame.init`](https://www.pygame.org/docs/ref/pygame.html).

```py
import pygame
pygame.init()
```

Use either the [`pygame.font`](https://www.pygame.org/docs/ref/font.html#pygame.font) module and create a [`pygame.font.SysFont`](https://www.pygame.org/docs/ref/font.html#pygame.font.SysFont) or [`pygame.font.Font`](https://www.pygame.org/docs/ref/font.html#pygame.font.Font) object. [`render()`](https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render) a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) with the text and [`blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) the _Surface_ to the screen:

```py
my_font = pygame.font.SysFont(None, 50)
text_surface = myfont.render("Hello world!", True, (255, 0, 0))
screen.blit(text_surface, (10, 10))
```

Or use the [`pygame.freetype`](https://www.pygame.org/docs/ref/freetype.html) module.  Create a [`pygame.freetype.SysFont()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.SysFont) or [`pygame.freetype.Font`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) object. [`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render) a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) with the text or directly [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to) the text to the screen:

```py
my_ft_font = pygame.freetype.SysFont('Times New Roman', 50)
my_ft_font.render_to(screen, (10, 10), "Hello world!", (255, 0, 0))
```

### Unicode

Related Stack Overflow questions:

- [Displaying unicode symbols using pygame](https://stackoverflow.com/questions/63398332/displaying-unicode-symbols-using-pygame/63398488#63398488)  
  ![Displaying unicode symbols using pygame](https://i.stack.imgur.com/tZ2EM.png)
- [how to make PNG canvas see-through in pygame when blitting image](https://stackoverflow.com/questions/64358747/how-to-make-png-canvas-see-through-in-pygame-when-blitting-image/64360467#64360467)  
  ![how to make PNG canvas see-through in pygame when blitting image](https://i.stack.imgur.com/fBEEV.png)

:scroll: **[Minimal example - Unicode](../../examples/minimal_examples/pygame_minimal_text_unicode.py)**

![Displaying unicode symbols using pygame](https://i.stack.imgur.com/tZ2EM.png)

## Align text

Related Stack Overflow questions:

- [python library pygame: centering text](https://stackoverflow.com/questions/23982907/python-library-pygame-centering-text)  

[`pygame.Surface.get_rect.get_rect()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect) returns a rectangle with the size of the _Surface_ object, that always starts at (0, 0) since a _Surface_ object has no position. The position of the rectangle can be specified by a keyword argument. For example, the center of the rectangle can be specified with the keyword argument `center`. These keyword argument are applied to the attributes of the [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) before it is returned (see [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) for a full list of the keyword arguments).

Get the text rectangle and place the center of the text rectangle on the center of the window rectangle:

```py
text_rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
```

You can even get the center of the window from the display _Surface_ :

```py
text_rect = text.get_rect(center = screen.get_rect().center)
```

Or with the use of [`pygame.display.get_surface()`](https://www.pygame.org/docs/ref/display.html):

```py
text_rect = text.get_rect(center = pygame.display.get_surface().get_rect().center)
```

A _Surface_ can be drawn on another _Surface_ using the [`blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) method. The second argument is either a tuple (_x_, _y_) representing the upper left corner or a rectangle. With a rectangle, only the upper left corner of the rectangle is taken into account. Therefore you can pass the text rectangle directly to `blit`:

```py
screen.blit(text, text_rect)
```

:scroll: **[minimal example - Render centered text](../../examples/minimal_examples/pygame_minimal_textpygame_minimal_text_font_font_trasnparent.py)**

![python library pygame: centering text](https://i.stack.imgur.com/tWcUe.png)

## Text

Related Stack Overflow questions:

- [How to add a text speech in Pygame](https://stackoverflow.com/questions/60997970/how-to-add-a-text-speech-in-pygame/60998091#60998091)  
  ![How to add a text speech in Pygame](https://i.stack.imgur.com/9Ymts.gif)

- [Have an outline of text in Pygame](https://stackoverflow.com/questions/60987711/have-an-outline-of-text-in-pygame/60988595#60988595)  
  ![Have an outline of text in Pygame](https://i.stack.imgur.com/wAmCl.gif)

  :scroll: **[minimal example - Outline](../../examples/minimal_examples/pygame_minimal_text_outline.py)**

- [How to create a text input box with pygame?](https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame)  
  [How to make a string's content appears on screen as we type on keyboard?](https://stackoverflow.com/questions/60455692/how-to-make-a-strings-content-appears-on-screen-as-we-type-on-keyboard/60456556#60456556)  
  [How to allow the user to type only under certain conditions in pygame?](https://stackoverflow.com/questions/64254687/how-to-allow-the-user-to-type-only-under-certain-conditions-in-pygame)  
  ![How to create a text input box with pygame?](https://i.stack.imgur.com/2X5Se.gif)
  ![How to create a text input box with pygame?](https://i.stack.imgur.com/XDz5b.gif)
  
- [Rendering text with multiple lines in pygame](https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame/64598520#64598520)  
  [Python/Pygame make text in Pygame wrap when in leaves the window](https://stackoverflow.com/questions/64273966/python-pygame-make-text-in-pygame-wrap-when-in-leaves-the-window)  
  ![text](https://i.stack.imgur.com/Zx2mI.png)![text](https://i.stack.imgur.com/FUqLc.png)

- [How can I make Pygame wait a few milliseconds before every loop in a for loop without stopping other stuff?](https://stackoverflow.com/questions/64090872/how-can-i-make-pygame-wait-a-few-milliseconds-before-every-loop-in-a-for-loop-wi/64090993#64090993)  
  ![How can I make Pygame wait a few milliseconds before every loop in a for loop without stopping other stuff?](https://i.stack.imgur.com/eHAAr.gif)

Use the `KEYDOWN` event to get the input from the keyboard (see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)). The key that was pressed can be obtained from the `key` attribute of the [`pygame.event.Event`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object. `unicode` contains a single character string that is the fully translated character. Add the character to the text when a key is pressed.  
Two special keys need to be dealt with. If <kbd>RETURN</kbd> is pressed, the input is finished. If <kbd>BACKSPACE</kbd> is pressed, the last character of the input text must be removed:

```py
if event.type == pygame.KEYDOWN and input_active:
    if event.key == pygame.K_RETURN:
        input_active = False
    elif event.key == pygame.K_BACKSPACE:
        text =  text[:-1]
    else:
        text += event.unicode
```

:scroll: **[minimal example - Text input](../../examples/minimal_examples/pygame_minimal_text_input.py)**

![How to create a text input box with pygame?](https://i.stack.imgur.com/2X5Se.gif)

Use the algorithm in a [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) class. Handle the event in the `update` method.Determine whether the mouse clicks in the text entry field with [`collidepoint`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint) (see [How to detect when a rectangular object, image or sprite is clicked](https://stackoverflow.com/questions/58917346/how-to-detect-when-a-sprite-is-clicked/58935218#58935218)) and activate the text input box:

```py
class TextInputBox(pygame.sprite.Sprite):
    # [...]

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()
```

Pass the list of events to the `update` method of the _Group_ that contains the _Sprite_:

```py
event_list = pygame.event.get()
for event in event_list:
    if event.type == pygame.QUIT:
        run = False
group.update(event_list)
```

:scroll: **[minimal example - Text input box](../../examples/minimal_examples/pygame_minimal_sprite_text_input_box.py)**

![How to create a text input box with pygame?](https://i.stack.imgur.com/XDz5b.gif)

There is no automatic solution. You have to implement the text wrap by yourself and draw the text line by line respectively word by word.  
Fortunately PyGame wiki provides a function that for this task. See PyGame wiki [Simple Text Wrapping for pygame](https://www.pygame.org/wiki/TextWrap).

I've extended the function and added an additional argument, which provides _left_ or _right_ aligned text, _centerd_ text or even _block_ mode:

:scroll: **[Minimal example - Word wrap](../../examples/minimal_examples/pygame_minimal_text_box_wrap.py)**

![text](https://i.stack.imgur.com/Zx2mI.png)
![text](https://i.stack.imgur.com/FUqLc.png)

```py
textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=False, bkg=None):
    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width() 
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""
```

## Performance issues an lag

Related Stack Overflow questions:

- [Rendering text in pygame causes lag](https://stackoverflow.com/questions/60469344/rendering-text-in-pygame-causes-lag/60469401#60469401)
- [How to render/blit text in pygame for good performance](https://stackoverflow.com/questions/64563528/how-to-render-blit-text-in-pygame-for-good-performance/64563594#64563594)

## Transparent text

Related Stack Overflow questions:

- [Python - Pygame - rendering translucent text](https://stackoverflow.com/questions/20620109/how-to-render-transparent-text-with-alpha-channel-in-pygame/20622680#20622680)

When using the [`pygame.font`](https://www.pygame.org/docs/ref/font.html#pygame.font) module, the alpha channel of the text color is not taken into account when rendering a text, but see [`pygame.font.Font.render`](https://www.pygame.org/docs/ref/font.html#pygame.font.SysFont):

> Antialiased images are rendered to 24-bit RGB images. If the background is transparent a pixel alpha will be included.

and [`pygame.Surface.set_alpha`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_alpha)

> Changed in pygame 2.0: per-surface alpha can be combined with per-pixel alpha.

Hence it is completely sufficient to set the transparency after rendering the text with `set_alpha`. This even works for anti-aliased text:

```py
font = pygame.font.SysFont(None, 150)

text_surf = font.render('test text', True, (255, 0, 0))
text_surf.set_alpha(127)

window.blit(text_surf, (x, y))
```

:scroll: **[minimal example - Render transparent text with font module](../../examples/minimal_examples/pygame_minimal_text_font_trasparent.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TransparentText](https://repl.it/@Rabbid76/PyGame-TransparentText#main.py)</kbd>

![Python - Pygame - rendering translucent text](https://i.stack.imgur.com/nFzbT.png)

By using the [`pygame.freetype`](https://www.pygame.org/docs/ref/freetype.html) module, you can use a transparent color directly when creating a text surface:

```py
ft_font = pygame.freetype.SysFont('Times New Roman', 150)

text_surf2, text_rect2 = ft_font.render('test text', (255, 0, 0, 128))

window.blit(text_surf2, (x, y))
```

Or if you are rendering the text directly onto a surface:

```py
ft_font = pygame.freetype.SysFont('Times New Roman', 150)

ft_font.render_to(window, (x, y), 'test text', (255, 0, 0, 128))
```

:scroll: **[minimal example - Render transparent text with freetype module](../../examples/minimal_examples/pygame_minimal_text_freetype_transparent.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TransparentFreeTypeText](https://repl.it/@Rabbid76/PyGame-TransparentFreeTypeText#main.py)</kbd>

![Python - Pygame - rendering translucent text](https://i.stack.imgur.com/AqOrH.png)
