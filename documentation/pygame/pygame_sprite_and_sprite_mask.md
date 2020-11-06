
[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Sprite, Group and Sprite mask

## Sprite

Related Stack Overflow questions:

- [Why is my PyGame Sprite, in a Group, not drawn - AttributeError: 'Group' object has no attribute 'blitme'](https://stackoverflow.com/questions/64076676/python-game-attributeerror-group-object-has-no-attribute-blitme)
- [Created multiple instances of the same image using a loop, can I move each instance of the image independently?](https://stackoverflow.com/questions/56415073/created-multiple-instances-of-the-same-image-using-a-loop-can-i-move-each-insta/56415305#56415305)
- [How can I deepcopy a pygame sprite group?](https://stackoverflow.com/questions/57500397/how-can-i-deepcopy-a-pygame-sprite-group)

[`pygame.sprite.Group.draw()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw) and [`pygame.sprite.Group.update()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update) are methods which are provided by `pygame.sprite.Group`. The former delegates the to the `update` mehtod of the contained [`pygame.sprite.Sprite`s](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) - you have to implement the method. The later uses the `image` and `rect` attributes of the contained `pygame.sprite.Sprite`s to draw the objects - you have to ensure that the `pygame.sprite.Sprite`s have the required attributes.

If `chased` is a [`pygame.sprite.Group`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) object, then you can get a list of [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) objects by the method [`sprites()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.sprites):

```py
enemy = min([e for e in chased.sprites()], 
            key=lambda e: pow(e.x-entity.x, 2) + pow(e.y-entity.y, 2))
```

## Sprite Groups

Related Stack Overflow questions:

- [Can I create and handle a pygame sprite not in a group the same way as if it's in a group?](https://stackoverflow.com/questions/63487180/can-i-create-and-handle-a-pygame-sprite-not-in-a-group-the-same-way-as-if-its-i/63487306#63487306)
- [How to have each sprite in a group A chasing the closest sprite in group B?](https://stackoverflow.com/questions/63927331/how-to-have-each-sprite-in-a-group-a-chasing-the-closest-sprite-in-group-b/63927397#63927397)

## Destroy (kill) Sprite objects

- [end the pygame when player mises the target more than three times](https://stackoverflow.com/questions/59985408/end-the-pygame-when-player-mises-the-target-more-than-three-times/59992840#59992840)
- [Found a strange hitbox bug in pygame. If the player dies in my game, the hitbox stays which creates some problems](https://stackoverflow.com/questions/60356181/found-a-strange-hitbox-bug-in-pygame-if-the-player-dies-in-my-game-the-hitbox/60356271#60356271)
- [How to determine why objects pass through each other in Colliderect](https://stackoverflow.com/questions/61453075/how-to-determine-why-objects-pass-through-each-other-in-colliderect/61453207#61453207)

You can get a list of [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) objects by the method [`sprites()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.sprites):

```py
enemy = min([e for e in chased.sprites()], key=lambda e: pow(e.x-entity.x, 2) + pow(e.y-entity.y, 2))
```

## Sprite collide

Related Stack Overflow questions:

- [Collisions still aren't getting detected in pygame](https://stackoverflow.com/questions/63465025/collisions-still-arent-getting-detected-in-pygame/63465289#63465289)
- [How do you assign a “rect” attribute to a pygame.sprite.rect rectangle in Pygame?](https://stackoverflow.com/questions/61370439/how-do-you-assign-a-rect-attribute-to-a-pygame-sprite-rect-rectangle-in-pygame/61371148#61371148)
- [pygame-'pygame.Rect' object has no attribute 'rect'](https://stackoverflow.com/questions/62325191/pygame-pygame-rect-object-has-no-attribute-rect/62325482#62325482)
- [Collisions still aren't getting detected in pygame](https://stackoverflow.com/questions/63465025/collisions-still-arent-getting-detected-in-pygame/63465289#63465289)  
  ![Collisions still aren't getting detected in pygame](https://i.stack.imgur.com/OkZC7.gif)

### Sprite collide with Sprite

- [How do I register collisions with objects from the same class without an unwanted object from another class in my group?](https://stackoverflow.com/questions/63060249/how-do-i-register-collisions-with-objects-from-the-same-class-without-an-unwante/63062808#63062808)

### Sprite collide with Group

Related Stack Overflow questions:

- [Pygame - getting a sprite to cycle through images in a class, and assign a hitbox](https://stackoverflow.com/questions/59904989/pygame-getting-a-sprite-to-cycle-through-images-in-a-class-and-assign-a-hitbo/59908083#59908083)
- [Tank collides with walls in pygame](https://stackoverflow.com/questions/61125022/tank-collides-with-walls-in-pygame/61125257#61125257)

### Group collide with Group

Related Stack Overflow questions:

- [pygame.sprite.groupcollide() does not work when trying to implement collision in pygame](https://stackoverflow.com/questions/63997798/pygame-sprite-groupcollide-does-not-work-when-trying-to-implement-collision-in/63998275#63998275)

### Circular sprite collision

Related Stack Overflow questions:

- [Curvy snake collision with itself](https://stackoverflow.com/questions/63168090/curvy-snake-collision-with-itself/63180315#63180315)

## Sprite mask

Related Stack Overflow questions:

- **[How can I made a collision mask?](https://stackoverflow.com/questions/56043600/how-can-i-made-a-collision-mask/56045037#56045037)**
- **[Pygame mask collision](https://stackoverflow.com/questions/60077813/pygame-mask-collision/60078039#60078039)**  
  [![Pygame mask collision](https://i.stack.imgur.com/fiLMi.gif)](https://stackoverflow.com/questions/60077813/pygame-mask-collision/60078039#60078039)

  :scroll: **[Minimal example - Find the intersection of rotating sprites](../../examples/minimal_examples/pygame_minimal_sprite_mask_intersect.py)**

  <kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-SpriteMask](https://repl.it/@Rabbid76/PyGame-SpriteMask#main.py)</kbd>

[`pygame.sprite.collide_mask()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_mask) use the `.rect` and `.mask` attribute of the sprite object for the collision detection.

See the documentation of [`pygame.sprite.collide_mask()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_mask):

>Collision detection between two sprites, using masks.
>
>```py
>collide_mask(SpriteLeft, SpriteRight) -> point
>```
>
>**Tests for collision between two sprites**, by testing if their bitmasks overlap. If the sprites have a "mask" attribute, that is used as the mask, otherwise a mask is created from the sprite image. Intended to be passed as a collided callback function to the *collide functions. Sprites must have a "rect" and an optional "mask" attribute.

## Layers

Related Stack Overflow questions:

- [Pygame sprite disappearing with layeredUpdates at a certain Y coordinate](https://stackoverflow.com/questions/61562822/pygame-sprite-disappearing-with-layeredupdates-at-a-certain-y-coordinate/61607539#61607539)

## Animation, timing and Sprite sheet

Related Stack Overflow questions:

- [Play animation upon collision with enemy](https://stackoverflow.com/questions/61964552/play-animation-upon-collision-with-enemy/61968944#61968944)
- [trying to get sprite to disappear from screen after certain amount of time](https://stackoverflow.com/questions/62614228/trying-to-get-sprite-to-disappear-from-screen-after-certain-amount-of-time/62614388#62614388)
- [Animated sprite from few images](https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images/64668964#64668964)

For an animated _Sprite_ a list of images ([`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) objects) must be generated. A different picture of the list is displayed in each frame, just like in the pictures of a movie. This gives the appearance of an animated object.  
One way to get a list of images is to load an animated [_GIF_ (Graphics Interchange Format)](https://de.wikipedia.org/wiki/Graphics_Interchange_Format). Unfortunately, PyGame doesn't offer a function to load the frames of an animated GIF. However, there are several Stack Overflow answers that address this issue:

- [How can I load an animated GIF and get all of the individual frames in PyGame?](https://stackoverflow.com/questions/29571399/how-can-i-load-an-animated-gif-and-get-all-of-the-individual-frames-in-pygame)
- [How do I make a sprite as a gif in pygame?](https://stackoverflow.com/questions/64179680/how-do-i-make-a-sprite-as-a-gif-in-pygame/64182074#64182074)
- [Pygame and Numpy Animations](https://stackoverflow.com/questions/54415196/pygame-and-numpy-animations)

One way is to use the popular [Pillow](https://pillow.readthedocs.io/en/stable/) library ([_pip install Pillow_](https://pypi.org/project/Pillow/)). The following function loads the frames of an animated _GIF_ and generates a list of `pygame.Surface` objects:

```py
from PIL import Image, ImageSequence
```

```py
def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames
```

Create a [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) class that maintains a list of images. Implement an update method that selects a different image in each frame.  
Pass the list of images to the class constructor. Add an `index` attribute that indicates  the index of the current image in the list. Increase the index in the `Update` method. Reset the index if it is greater than or equal to the length of the image list (or use the modulo (`%`) operator). Get the current image from the list by subscription:

```py
class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0
    def update(self):
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0
        self.image = self.images[self.image_index]
```

:scroll: **[Minimal example - Animated sprites](../../examples/minimal_examples/pygame_minimal_sprite_animated_gif_pil.py)**

<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-SpriteAnimation](https://repl.it/@Rabbid76/PyGame-SpriteAnimation#main.py)</kbd>

![Animated sprite from few images](https://i.stack.imgur.com/SzKwL.gif)

## Rotate Sprite

Related Stack Overflow questions:

- [How can you rotate an image around an off center pivot in PyGame](https://stackoverflow.com/questions/59909942/how-can-you-rotate-an-image-around-an-off-center-pivot-in-pygame/59909946#59909946/59909946#59909946)  
  ![How can you rotate an image around an off center pivot in PyGame](https://i.stack.imgur.com/BmG1u.gif)

  :scroll: **[Minimal example - Rotate Sprite around off center pivot](../../examples/surface_rotate/pygame_sprite_rotate_pivot_boomerang.py)**

  <kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-RotateSpriteAroundOffCenterPivot](https://repl.it/@Rabbid76/PyGame-RotateSpriteAroundOffCenterPivot#main.py)</kbd>

## Click Sprite

Related Stack Overflow questions:

- [Pygame mouse clicking detection](https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684)  
  ![Pygame mouse clicking detection](https://i.stack.imgur.com/mW6vv.gif)

  :scroll: **[minimal example - Detect click on sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_click.py)**

  <kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseClick](https://repl.it/@Rabbid76/PyGame-MouseClick#main.py)</kbd>

Use the `rect` attribute of the [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) object and the [`collidepoint`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint) method to see if the _Sprite_ was clicked.
Pass the list of events to the [`update`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update) method of the [`pygame.sprite.Group`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) so that you can process the events in the _Sprite_ class:

```py
class SpriteObject(pygame.sprite.Sprite):
    # [...]

    def update(self, event_list):

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # [...]

my_sprite = SpriteObject()
group = pygame.sprite.Group(my_sprite)

# [...]

run = True
while run:
    event_list = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    group.update(event_list)

    # [...]
```

## Sprite on mouse hover

Related Stack Overflow questions:

- [Pygame mouse clicking detection](https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684)  
  ![Pygame mouse clicking detection](https://i.stack.imgur.com/UJVKi.gif)

  :scroll: **[minimal example - Detect Sprite on hover](../../examples/minimal_examples/pygame_minimal_sprite_mouse_hover.py)**

  <kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseHover](https://repl.it/@Rabbid76/PyGame-MouseHover#main.py)</kbd>

Detect  evaluate the mouse states in the `Update` method of the [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) object:

```py
class SpriteObject(pygame.sprite.Sprite):
    # [...]

    def update(self, event_list):

        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        if  self.rect.collidepoint(mouse_pos) and any(mouse_buttons):
            # [...]

my_sprite = SpriteObject()
group = pygame.sprite.Group(my_sprite)

# [...]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    group.update(event_list)

    # [...]
```

## Drag Sprite

Related Stack Overflow questions:

- [Creating multiple sprites with different update()'s from the same sprite class in Pygame](https://stackoverflow.com/questions/64419223/creating-multiple-sprites-with-different-updates-from-the-same-sprite-class-i/64456959#64456959)  
  ![Creating multiple sprites with different update()'s from the same sprite class in Pygame](https://i.stack.imgur.com/BaFzb.gif)

  :scroll: **[Minimal example - Drag Sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_drag.py)**

  <kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseDrag](https://repl.it/@Rabbid76/PyGame-MouseDrag#main.py)</kbd>

## Circular sprite

Related Stack Overflow questions:

- [how to create a circular sprite in pygame](https://stackoverflow.com/questions/61429734/how-to-create-a-circular-sprite-in-pygame/61429811#61429811)

## Copy (duplicate) sprites

Related Stack Overflow questions:

- [Duplicating a sprite](https://stackoverflow.com/questions/64377099/duplicating-a-sprite/64377800#64377800)

In general, you need to implement the `duplicate` method and construct a new instance of the _Sprite_ object in the method.

Another solution is to use the Python [`copy`](https://docs.python.org/3/library/copy.html) module. `deepcopy` can create a deep copy of an object. Unfortunately this cannot be used for [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) objects, as the`image` attribute is a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html), which cannot be copied deeply. Therefore, a `deepcopy` of a _Sprite_ will cause an error.  
Unless you have nor any other attribute that needs to be copied deeply, you can make a shallow `copy` of the _Sprite_. The `rect` attribute is a [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) object. The copy of the _Sprite_ needs its own rectangle, so you have to generate a new rectangle instance. Fortunately a `pygame.Rect` object can be copied by [`pygame.Rect.copy`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.copy):

```py
import copy
```

```py
new_d = copy.copy(d)
new_d.rect = d.rect.copy()
```

## Text input

Related Stack Overflow questions:

- [How to create a text input box with pygame?](https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame)  
  ![How to create a text input box with pygame?](https://i.stack.imgur.com/XDz5b.gif)

  :scroll: **[minimal example - Text input box](../../examples/minimal_examples/pygame_minimal_sprite_text_input_box.py)**
