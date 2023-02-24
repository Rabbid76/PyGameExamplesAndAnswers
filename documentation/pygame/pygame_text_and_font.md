[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"A long descriptive name is better than a short enigmatic name. A long descriptive name is better than a long descriptive comment."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Text and font

## Bugs

Related Stack Overflow questions:

- [Blitting text with pygame2.1 not working correctly](https://stackoverflow.com/questions/70445036/blitting-text-with-pygame2-1-not-working-correctly/70447991#70447991)  

## Font

Related Stack Overflow questions:

- [pygame - How to display text with font & color?](https://stackoverflow.com/questions/10077644/pygame-how-to-display-text-with-font-color/64487335#64487335)
- [How to display text in pygame?](https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame)  
- [How to scale the font size in pygame based on display resolution?](https://stackoverflow.com/questions/56855775/how-to-scale-the-font-size-in-pygame-based-on-display-resolution/56857032#56857032)
- [I need to add text to my rectangles, how would I do this?](https://stackoverflow.com/questions/55511081/i-need-to-add-text-to-my-rectangles-how-would-i-do-this/55521100#55521100)
- [How to display some text in pygame?](https://stackoverflow.com/questions/58695609/how-to-display-some-text-in-pygame/58695757#58695757)
- [Pygame smooth fonts](https://stackoverflow.com/questions/20088670/pygame-smooth-fonts/65406337#65406337)  
- [TypeError: Invalid foreground RGBA argument](https://stackoverflow.com/questions/57294067/typeerror-invalid-foreground-rgba-argument/67608006#67608006)  

[Minimal `pygame.font` module example](../../examples/minimal_examples/pygame_minimal_text_font.py)

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-Text](https://replit.com/@Rabbid76/PyGame-Text#main.py)**

[Minimal `pygame.freetype` module example](../../examples/minimal_examples/pygame_minimal_text_freetype.py)

![inimal `pygame.freetype` module example](https://i.stack.imgur.com/QnNaX.png)

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-FreeTypeText](https://replit.com/@Rabbid76/PyGame-FreeTypeText#main.py)**

![Minimal `pygame.freetype` module example](https://i.stack.imgur.com/umMZi.png)

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

## Find font

Related Stack Overflow questions:

- [I can't use the available fonts in pygame](https://stackoverflow.com/questions/72514320/i-cant-use-the-available-fonts-in-pygame/72514363#72514363)

Use [`pygame.font.SysFont`](https://www.pygame.org/docs/ref/font.html#pygame.font.SysFont) instead of [`pygame.font.Font`](https://www.pygame.org/docs/ref/font.html#pygame.font.Font):

```py
font = pygame.font.SysFont('comicsansms', size)
```

Or use [`pygame.font.match_font()`](https://www.pygame.org/docs/ref/font.html) to find the path to a specific font file:

```py
comicsansms_file = pygame.font.match_font('comicsansms')
font = pygame.font.Font(comicsansms_file, size)
```

## Bold

Related Stack Overflow questions:

- [Make a Single Word Within a String Bold](https://stackoverflow.com/questions/72409725/make-a-single-word-within-a-string-bold/72409816#72409816)
- [Make a Single Word Within a String Bold](https://i.stack.imgur.com/Gs2ok.png)

  :scroll: **[Minimal example - Bold text](../../examples/minimal_examples/pygame_minimal_text_bold.py)**  
  :scroll: **[Minimal example - Bold text freetype](../../examples/minimal_examples/pygame_minimal_text_bold_2.py)**

To draw a"bold" text the "bold" version of the font must be used. "bold" isn't a flag or attribute, it's just a different font.
Use [`pygame.font.match_font()`](https://www.pygame.org/docs/ref/font.html) to find the path to a specific font file.  
With the [`pygame.freetype`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) modle the text can be rendered with different styles like `STYLE_DEFAULT` and `STYLE_STRONG`. However, the text can only be rendered with one style at a time. 

### Unicode

Related Stack Overflow questions:

- [Displaying unicode symbols using pygame](https://stackoverflow.com/questions/63398332/displaying-unicode-symbols-using-pygame/63398488#63398488)  
- [how to make PNG canvas see-through in pygame when blitting image](https://stackoverflow.com/questions/64358747/how-to-make-png-canvas-see-through-in-pygame-when-blitting-image/64360467#64360467)  
  ![how to make PNG canvas see-through in pygame when blitting image](https://i.stack.imgur.com/fBEEV.png)

  :scroll: **[Minimal example - Unicode](../../examples/minimal_examples/pygame_minimal_text_unicode.py)**

  ![Displaying unicode symbols using pygame](https://i.stack.imgur.com/tZ2EM.png)

- [How to load colorful emojis in pygame?](https://stackoverflow.com/questions/71092136/how-to-load-colorful-emojis-in-pygame/71092137#71092137)  

  :scroll: **[Minimal example - Unicode](../../examples/minimal_examples/pygame_minimal_text_emoji.py)**

I want to use Pygame's [freetype](https://www.pygame.org/docs/ref/freetype.html) module to load a colorful emoji via its unicode. Unfortunately I only get a monochrome image with the outline of the emoji:

![How to load colorful emojis in pygame?](https://i.stack.imgur.com/uXJzF.png)

```py
import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((200, 200))

seguisy80 = pygame.freetype.SysFont("segoeuisymbol", 100)
emoji, rect = seguisy80.render('😃', "black")
rect.center = window.get_rect().center

run = True
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill("lightgray")
    window.blit(emoji, rect)
    pygame.display.flip()

pygame.quit()
```

How can I modify this code to get a full RGBA color image of an emoji?

Unfortunately, colored font loading is not natively supported in Pygame. However, there is a workaround.
First you need a colored emoji font. For example, you can download one here: [Apple Color Emoji for Linux](https://github.com/samuelngs/apple-emoji-linux#installing-prebuilt-applecoloremoji-font).

Load this font using [https://freetype.org/](https://freetype-py.readthedocs.io/en/latest/). Install [`freetype-py`](https://pypi.org/project/freetype-py/):

```py
pip3 install freetype-py 
```

For Windows users, it should be mentioned that the installed package does not support the font and results in an "unimplemented feature" exception.
Download the package from [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#freetypepy) and install it. e.g.:

```py
pip3 install freetype_py-2.2.0-cp310-cp310-win_amd64.whl
```

Now you're prepared and can load an emoji from the font.Emojis and their Unicode can be found here: [Emoticons (Unicode block)](https://en.wikipedia.org/wiki/Emoticons_(Unicode_block)).
Copy the emoji or use the unicode and load the glyph:

```py
import freetype

face = freetype.Face("AppleColorEmoji.ttf")
face.set_char_size(int(face.available_sizes[-1].size)) 
    
face.load_char('😀', freetype.FT_LOAD_COLOR) # or face.load_char('\U0001F603', freetype.FT_LOAD_COLOR)
```

The loaded glyph now needs to be turned into a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html). To do this, use [NumPy](https://numpy.org/).
How this works in detail is explained in the answer to the question: [How do I convert an OpenCV (cv2) image (BGR and BGRA) to a pygame.Surface object](https://stackoverflow.com/questions/64183409/how-do-i-convert-an-opencv-cv2-image-bgr-and-bgra-to-a-pygame-surface-object/64183410#64183410).

```py
import numpy as np

ft_bitmap = face.glyph.bitmap
bitmap = np.array(ft_bitmap.buffer, dtype=np.uint8).reshape((ft_bitmap.rows, ft_bitmap.width, 4))
bitmap[:, :, [0, 2]] = bitmap[:, :, [2, 0]]
emoji = pygame.image.frombuffer(bitmap.flatten(), (ft_bitmap.width, ft_bitmap.rows), 'RGBA')
```

![How to load colorful emojis in pygame?](https://i.stack.imgur.com/0lMMh.png)

```py
import pygame
import freetype
import numpy as np

class Emojis:
    def __init__(self):
        self. face = freetype.Face("AppleColorEmoji.ttf")
        self.face.set_char_size(int(self.face.available_sizes[-1].size)) 
    def create_surface(self, unicode):
        self.face.load_char(unicode, freetype.FT_LOAD_COLOR)
        ft_bitmap = self.face.glyph.bitmap
        bitmap = np.array(ft_bitmap.buffer, dtype=np.uint8).reshape((ft_bitmap.rows, ft_bitmap.width, 4))
        bitmap[:, :, [0, 2]] = bitmap[:, :, [2, 0]]
        return pygame.image.frombuffer(bitmap.flatten(), (ft_bitmap.width, ft_bitmap.rows), 'RGBA')

pygame.init()
window = pygame.display.set_mode((200, 200))
emojis = Emojis()

emoji = emojis.create_surface('😃')
#emoji = emojis.create_surface('\U0001F603')
rect = emoji.get_rect(center = window.get_rect().center)

run = True
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill("lightgray")
    window.blit(emoji, rect)
    pygame.display.flip()

pygame.quit()
```

## Align text and text size

Related Stack Overflow questions:

- [How to Center Text in Pygame](https://stackoverflow.com/questions/23982907/pygame-how-to-center-text/64660744#64660744)
- [How to center text inside a shape?](https://stackoverflow.com/questions/68446707/how-to-center-text-inside-a-shape/68446734#68446734)
- [How to get text width in pygame?](https://stackoverflow.com/questions/65273980/how-to-get-text-width-in-pygame/65274103#65274103)  

- [Pygame: Centering text system font text](https://stackoverflow.com/questions/65278123/pygame-centering-text-system-font-text/65278233#65278233)  
  ![Pygame: Centering text system font text](https://i.stack.imgur.com/KnYWY.png)

  :scroll: **[Minimal example - Freetype centered](../../examples/minimal_examples/pygame_minimal_text_freetype_centered.py)**

- [Python Pygame Font x coordinate](https://stackoverflow.com/questions/67514758/python-pygame-font-x-coordinate/67514998#67514998)  
  ![Python Pygame Font x coordinate](https://i.stack.imgur.com/1fbjS.gif)

- [Pygame Python Font Size](https://stackoverflow.com/questions/67518357/pygame-python-font-size/67518454#67518454)  
  [Pygame Python font](https://stackoverflow.com/questions/67529507/pygame-python-font/67530490#67530490)  
  ![Pygame Python font](https://i.stack.imgur.com/h1Btd.png)

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

## Table

Related Stack Overflow questions:v

- [display sqlite database as a table in paygames](https://stackoverflow.com/questions/68881160/display-sqlite-database-as-a-table-in-paygames/68881263#68881263)

## Blinking text

Related Stack Overflow questions:

- [How to make a text blink in PyGame?](https://stackoverflow.com/questions/68019153/how-to-make-a-text-blink-in-pygame/68019222#68019222)  
  ![How to make a text blink in PyGame?](https://i.stack.imgur.com/HbfMp.gif)

## Text

Related Stack Overflow questions:

- [Padding for text using pygame SysFont](https://stackoverflow.com/questions/70127121/padding-for-text-using-pygame-sysfont/70127411#70127411)  
  ![Padding for text using pygame SysFont](https://i.stack.imgur.com/iflrG.png)  

- [How to add a text speech in Pygame](https://stackoverflow.com/questions/60997970/how-to-add-a-text-speech-in-pygame/60998091#60998091)  
  ![How to add a text speech in Pygame](https://i.stack.imgur.com/9Ymts.gif)

- [Have an outline of text in Pygame](https://stackoverflow.com/questions/60987711/have-an-outline-of-text-in-pygame/60988595#60988595)  
  ![Have an outline of text in Pygame](https://i.stack.imgur.com/wAmCl.gif)

  :scroll: **[minimal example - Outline](../../examples/minimal_examples/pygame_minimal_text_outline.py)**

- [How to save an image with the outline text using pygame?](https://stackoverflow.com/questions/66154735/how-to-save-an-image-with-the-outline-text-using-pygame/66157210#66157210)  
  ![How to save an image with the outline text using pygame?](https://i.stack.imgur.com/LTDG4.png)  
  ![How to save an image with the outline text using pygame?](https://i.stack.imgur.com/sSd7Y.png)  

- [Text with a Drop-shadow](https://stackoverflow.com/questions/52960057/pygame-text-with-a-drop-shadow/73927438#73927438)
  ![Text with a Drop-shadow](https://i.stack.imgur.com/8D4mY.png)

  :scroll: **[minimal example - Drop shadow](../../examples/minimal_examples/pygame_minimal_text_drop_shadow.py)**

- [How to add a blinking cursor in pygame?](https://stackoverflow.com/questions/68176808/how-to-add-a-blinking-cursor-in-pygame/68181209#68181209)  
  ![How to add a blinking cursor in pygame?](https://i.stack.imgur.com/9OEc6.gif)  

- [How to create a text input box with pygame?](https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame/64613666#64613666)  
  [How to make a string's content appears on screen as we type on keyboard?](https://stackoverflow.com/questions/60455692/how-to-make-a-strings-content-appears-on-screen-as-we-type-on-keyboard/60456556#60456556)  
  [How to allow the user to type only under certain conditions in pygame?](https://stackoverflow.com/questions/64254687/how-to-allow-the-user-to-type-only-under-certain-conditions-in-pygame/64255822#64255822)  
  ![How to create a text input box with pygame?](https://i.stack.imgur.com/2X5Se.gif)
  ![How to create a text input box with pygame?](https://i.stack.imgur.com/FNJeM.gif)

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TextInput](https://replit.com/@Rabbid76/PyGame-TextInput#main.py)**

- [Paragraph input in pygame](https://stackoverflow.com/questions/71021541/paragraph-input-in-pygame/71022505#71022505)  
  ![Paragraph input in pygame](https://i.stack.imgur.com/ucFXl.gif)

  :scroll: **[minimal example - Drop shadow](../../examples/minimal_examples/pygame_minimal_text_paragraph_input.py)**

- [Rendering text with multiple lines in pygame](https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame/64598520#64598520)  
  [Python/Pygame make text in Pygame wrap when in leaves the window](https://stackoverflow.com/questions/64273966/python-pygame-make-text-in-pygame-wrap-when-in-leaves-the-window)  
  ![text](https://i.stack.imgur.com/Zx2mI.png)![text](https://i.stack.imgur.com/FUqLc.png)

- [How can I make Pygame wait a few milliseconds before every loop in a for loop without stopping other stuff?](https://stackoverflow.com/questions/64090872/how-can-i-make-pygame-wait-a-few-milliseconds-before-every-loop-in-a-for-loop-wi/64090993#64090993)  
  ![How can I make Pygame wait a few milliseconds before every loop in a for loop without stopping other stuff?](https://i.stack.imgur.com/eHAAr.gif)

Use the `KEYDOWN` event to get the input from the keyboard (see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)). The key that was pressed can be obtained from the `key` attribute of the [`pygame.event.Event`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object. `unicode` contains a single character string that is the fully translated character. Add the character to the text when a key is pressed.  
Two special keys need to be dealt with. If **RETURN** is pressed, the input is finished. If **BACKSPACE** is pressed, the last character of the input text must be removed:

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

![How to create a text input box with pygame?](https://i.stack.imgur.com/FNJeM.gif)

There is no automatic solution. You have to implement the text wrap by yourself and draw the text line by line respectively word by word.  
Fortunately PyGame wiki provides a function that for this task. See PyGame wiki [Simple Text Wrapping for pygame](https://www.pygame.org/wiki/TextWrap).

I've extended the function and added an additional argument, which provides _left_ or _right_ aligned text, _centerd_ text or even _block_ mode:

:scroll: **[Minimal example - Word wrap](../../examples/minimal_examples/pygame_minimal_text_linebreak.py)**  
:scroll: **[Minimal example - Word wrap](../../examples/minimal_examples/pygame_minimal_text_box_wrap.py)**  

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TextWrap](https://replit.com/@Rabbid76/PyGame-TextWrap#main.py)**

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

Creating a font object is very time consuming because the font file has to be read and interpreted.

## Transparent text

Related Stack Overflow questions:

- [How to render transparent text with alpha channel in PyGame?](https://stackoverflow.com/questions/20620109/how-to-render-transparent-text-with-alpha-channel-in-pygame/64552616#64552616)  
- [How to separately change the opacity of a text on a button pygame?](https://stackoverflow.com/questions/68128389/how-to-separately-change-the-opacity-of-a-text-on-a-button-pygame/68128949#68128949)  

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

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TransparentText](https://replit.com/@Rabbid76/PyGame-TransparentText#main.py)**

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

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TransparentFreeTypeText](https://replit.com/@Rabbid76/PyGame-TransparentFreeTypeText#main.py)**

![Python - Pygame - rendering translucent text](https://i.stack.imgur.com/AqOrH.png)

:scroll: **[minimal example - Render transparent text with transparent background](../../examples/minimal_examples/pygame_minimal_text_font_trasparent_background.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-TextTransparentBackground](https://replit.com/@Rabbid76/PyGame-TextTransparentBackground#main.py)**

![Python - Pygame - rendering text with transparent background](https://i.stack.imgur.com/dW5OU.png)

## Anti-Aliasing

Related Stack Overflow questions:

- [What is anti-aliasing in rendering an image in python?](https://stackoverflow.com/questions/66274137/what-is-anti-aliasing-in-rendering-an-image-in-python/66275189#66275189)  
  ![What is anti-aliasing in rendering an image in python?](https://i.stack.imgur.com/VCWBI.png)
  ![What is anti-aliasing in rendering an image in python?](https://i.stack.imgur.com/95Yj2.png)

## Devanagari/Arabic/Persian text

Related Stack Overflow questions:

- [How to fix Arabic/Persian text and font in pygame?](https://stackoverflow.com/questions/65218972/how-to-fix-arabic-persian-text-and-font-in-pygame)
- [Devanagari text rendering improperly in PyGame](https://stackoverflow.com/questions/44254171/devanagari-text-rendering-improperly-in-pygame)

## Ascii image

Related Stack Overflow questions:

- [How to display image and text at the same time in python (like SanctuaryRPG)?](https://stackoverflow.com/questions/67711739/how-to-display-image-and-text-at-the-same-time-in-python-like-sanctuaryrpg/67712339#67712339)
  ![How to display image and text at the same time in python (like SanctuaryRPG)?](https://i.stack.imgur.com/VucC8.png)

  :scroll: **[minimal example - Render ASCII text image](../../examples/minimal_examples/pygame_minimal_text_ascii_image.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-AsciiTextImage](https://replit.com/@Rabbid76/PyGame-AsciiTextIamge#main.py)**

## Typewriter

Related Stack Overflow questions:

- **[Typewriter Effect Pygame](https://stackoverflow.com/questions/41101662/typewriter-effect-pygame/70235527#70235527)**  
- [Pygame Rendering Text 1 by 1 Causes Lag In Game How Do I Fix This?](https://stackoverflow.com/questions/67273848/pygame-rendering-text-1-by-1-causes-lag-in-game-how-do-i-fix-this/67273892#67273892)  
  ![Typewriter Effect Pygame](https://i.stack.imgur.com/UenHN.gif)

  :scroll: **[minimal example - Typewriter](../../examples/minimal_examples/pygame_minimal_text_typewriter.py)**

    **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-Typewriter](https://replit.com/@Rabbid76/PyGame-Typewriter#main.py)**

## Scroll Text

Related Stack Overflow questions:

- [Pygame when adding new text it appears on bottom and rest of text goes up](https://stackoverflow.com/questions/70102350/pygame-when-adding-new-text-it-appears-on-bottom-and-rest-of-text-goes-up/70128422#70128422)  
  ![Pygame when adding new text it appears on bottom and rest of text goes up](https://i.stack.imgur.com/Rl00d.gif)

  :scroll: **[Minimal example - Text scroll](../../examples/minimal_examples/pygame_minimal_text_scroll.py)**

- [Make a rect object scrollable](https://stackoverflow.com/questions/67288788/make-a-rect-object-scrollable/67289087?noredirect=1)  
  ![Make a rect object scrollable](https://i.stack.imgur.com/Dezqy.png)

- [Displaying text onto pygame window from file using readline()](https://stackoverflow.com/questions/74671176/displaying-text-onto-pygame-window-from-file-using-readline)  
  ![Displaying text onto pygame window from file using readline()](https://i.stack.imgur.com/k2m8S.gif)
