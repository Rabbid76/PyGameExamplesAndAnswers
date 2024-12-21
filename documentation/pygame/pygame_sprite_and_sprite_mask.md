
[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"It is not enough for code to work."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Sprite, Group and Sprite mask

## Sprite

Related Stack Overflow questions:

- [What is the difference between pygame sprite and surface?](https://stackoverflow.com/questions/66665946/what-is-the-difference-between-pygame-sprite-and-surface/66667420#66667420)
- [Created multiple instances of the same image using a loop, can I move each instance of the image independently?](https://stackoverflow.com/questions/56415073/created-multiple-instances-of-the-same-image-using-a-loop-can-i-move-each-insta/56415305#56415305)
- [How can I deepcopy a pygame sprite group?](https://stackoverflow.com/questions/57500397/how-can-i-deepcopy-a-pygame-sprite-group)

- **[How to use sprites in PyGame?](https://stackoverflow.com/questions/73924256/how-to-use-sprites-in-pygame/73924281#73924281)**  
- [Making and using pygame sprites for donkey kong style game](https://stackoverflow.com/questions/68566126/making-and-using-pygame-sprites-for-donkey-kong-style-game/68600795#68600795)**

  📁 **[Minimal example - Minimal sprite image](../../examples/minimal_examples/pygame_minimal_sprite_image.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-Sprite](https://replit.com/@Rabbid76/PyGame-Sprite#main.py)**

- [Why We Have to Use self.rect and self.image to Determine Rect and Surf on Sprites?](https://stackoverflow.com/questions/68454667/why-we-have-to-use-self-rect-and-self-image-to-determine-rect-and-surf-on-sprite/68456266#68456266)

  📁 **[Minimal example - Minimal sprite update](../../examples/minimal_examples/pygame_minimal_sprite_update.py)**

A [`pygame.sprite.Sprite`](http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) encapsulates an [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object and an [`pygame.Rect`](https://www.pygame.org/docs/ref/rect.html) object. It should have and an `image` and a `rect` attribute. `image` stores the sprite and `rect` stores the position and size of the sprite.

[`pygame.sprite.Group.draw()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw) and [`pygame.sprite.Group.update()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update) are methods which are provided by `pygame.sprite.Group`.

The latter delegates to the `update` method of the contained [`pygame.sprite.Sprite`s](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) — you have to implement the method. See [`pygame.sprite.Group.update()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update):

> Calls the `update()` method on all Sprites in the Group. [...]

The former uses the `image` and `rect` attributes of the contained `pygame.sprite.Sprite`s to draw the objects — you have to ensure that the `pygame.sprite.Sprite`s have the required attributes. See [`pygame.sprite.Group.draw()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw):

> Draws the contained Sprites to the Surface argument. This uses the `Sprite.image` attribute for the source surface, and `Sprite.rect`. [...]

The _Sprites_ in the _Groups_ can be removed and thus destroyed by calling [`pygame.sprite.Sprite.kill`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite). When the object is no longer referenced, it is destroyed:

> The Sprite is removed from all the Groups that contain it. This won't change anything about the state of the Sprite. It is possible to continue to use the Sprite after this method has been called, including adding it to Groups.

If `chased` is a [`pygame.sprite.Group`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) object, then you can get a list of [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) objects by the method [`sprites()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.sprites):

```py
enemy = min([e for e in chased.sprites()], 
            key=lambda e: pow(e.x-entity.x, 2) + pow(e.y-entity.y, 2))
```

### Text spritewhot

Related Stack Overflow questions:

- [pygame. How to render the text like a all_sprites.update() but all_texts.update()?](https://stackoverflow.com/questions/74158381/pygame-how-to-render-the-text-like-a-all-sprites-update-but-all-texts-update/74158474#74158474)  
  ![pygame. How to render the text like a all_sprites.update() but all_texts.update()?](https://i.sstatic.net/yfYDi.png)

📁 **[Minimal example - Text sprite](../../examples/minimal_examples/pygame_minimal_sprite_text.py)**

## Sprite Groups

Related Stack Overflow questions:

- **[What does pygame.sprite.Group() do](https://stackoverflow.com/questions/68765971/what-does-pygame-sprite-group-do/68767767#68767767)**  

  📁 **[Minimal example - Minimal sprite group](../../examples/minimal_examples/pygame_minimal_sprite_group.py)**

- [Why We Have to Use self.rect and self.image to Determine Rect and Surf on Sprites?](https://stackoverflow.com/questions/68454667/why-we-have-to-use-self-rect-and-self-image-to-determine-rect-and-surf-on-sprite/68456266#68456266)  
- [Why do group lists in pygame have to have “update” functions, and not any other?](https://stackoverflow.com/questions/64835155/why-do-group-lists-in-pygame-have-to-have-update-functions-and-not-any-other/64835175#64835175)
- [Why is my PyGame Sprite, in a Group, not drawn - AttributeError: 'Group' object has no attribute 'blitme'](https://stackoverflow.com/questions/64076676/why-is-my-pygame-sprite-in-a-group-not-drawn-attributeerror-group-object/64076741#64076741)
- [Can I create and handle a pygame sprite not in a group the same way as if it's in a group?](https://stackoverflow.com/questions/63487180/can-i-create-and-handle-a-pygame-sprite-not-in-a-group-the-same-way-as-if-its-i/63487306#63487306)
- [How to have each sprite in a group A chasing the closest sprite in group B?](https://stackoverflow.com/questions/63927331/how-to-have-each-sprite-in-a-group-a-chasing-the-closest-sprite-in-group-b/63927397#63927397)
- [How to remove image, then blit it again?](https://stackoverflow.com/questions/65757826/how-to-remove-image-then-blit-it-again/65758502#65758502)  
- [How to reference and manipulate a single entity in a sprite group in pygame?](https://stackoverflow.com/questions/43855064/how-to-reference-and-manipulate-a-single-entity-in-a-sprite-group-in-pygame/65420633#65420633)  

A [`pygame.sprite.Group`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) is iterable. Hence you can go through the elements in a `for`-loop:

```py
for sprite in sprite_group:
    # [...]
```

Alternatively, you can use the [`sprites()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.sprites) method:

> Return a list of all the Sprites this group contains.

Get a list of _Sprites_ and access them by subscription:

```py
sprite_list = sprite_group.sprites()
sprite_1 = sprite_list[0]
```

### Extend `pygame.sprite.Group.draw` with `special_flags`

```py
class MyGroup(pygame.sprite.Group):
    def __init__(self, *args):
        super().__init__(*args) 
    def draw(self, surface, special_flags=0):
        for sprite in self:
            surface.blit(sprite.image, sprite.rect, special_flags = special_flags)
```

### Layers and layered Group

Related Stack Overflow questions:

- [Pygame sprite disappearing with layeredUpdates at a certain Y coordinate](https://stackoverflow.com/questions/61562822/pygame-sprite-disappearing-with-layeredupdates-at-a-certain-y-coordinate/61607539#61607539)

- [pygame.sprite.LayeredUpdates.move_to_front() does not work](https://stackoverflow.com/questions/69365433/pygame-sprite-layeredupdates-move-to-front-does-not-work/69365563#69365563)
  ![pygame.sprite.LayeredUpdates.move_to_front() does not work](https://i.sstatic.net/18mlv.gif)

## Render update Group

Related Stack Overflow questions:

- [Background image change glitches](https://stackoverflow.com/questions/70271511/background-image-change-glitches/70281354#70281354)

  📁 **[Minimal example - Minimal sprite group - render update](../../examples/minimal_examples/pygame_minimal_sprite_group_render_update_1.py)**

## Destroy (kill) Sprite objects

- [end the pygame when player mises the target more than three times](https://stackoverflow.com/questions/59985408/end-the-pygame-when-player-mises-the-target-more-than-three-times/59992840#59992840)
- [Found a strange hitbox bug in pygame. If the player dies in my game, the hitbox stays which creates some problems](https://stackoverflow.com/questions/60356181/found-a-strange-hitbox-bug-in-pygame-if-the-player-dies-in-my-game-the-hitbox/60356271#60356271)
- [How to determine why objects pass through each other in Colliderect](https://stackoverflow.com/questions/61453075/how-to-determine-why-objects-pass-through-each-other-in-colliderect/61453207#61453207)  
- [When I use pygame.sprite.spritecollide(), why does only the bullets disappear?](https://stackoverflow.com/questions/66752240/when-i-use-pygame-sprite-spritecollide-why-does-only-the-bullets-disappear/66752276#66752276)  

You can get a list of [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) objects by the method [`sprites()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.sprites):

```py
enemy = min([e for e in chased.sprites()], key=lambda e: pow(e.x-entity.x, 2) + pow(e.y-entity.y, 2))
```

- [Why is self.kill() not removing the object from the group?](https://stackoverflow.com/questions/73378230/why-is-self-kill-not-removing-the-object-from-the-group?noredirect=1#comment129587586_73378230)

  📁 **[Minimal example - sprite group kill issue](../../examples/minimal_examples/pygame_minimal_sprite_group_render_kill_issue.py)**

## Sprite collide

Related Stack Overflow questions:

- **[How do you program collision in classes?](https://stackoverflow.com/questions/69331228/how-do-you-program-collision-in-classes/69332148#69332148)**
  ![How do you program collision in classes?](https://i.sstatic.net/7eoyB.gif)
- [Collisions still aren't getting detected in pygame](https://stackoverflow.com/questions/63465025/collisions-still-arent-getting-detected-in-pygame/63465289#63465289)
- [How do you assign a “rect” attribute to a pygame.sprite.rect rectangle in Pygame?](https://stackoverflow.com/questions/61370439/how-do-you-assign-a-rect-attribute-to-a-pygame-sprite-rect-rectangle-in-pygame/61371148#61371148)
- [pygame-'pygame.Rect' object has no attribute 'rect'](https://stackoverflow.com/questions/62325191/pygame-pygame-rect-object-has-no-attribute-rect/62325482#62325482)
- [Collisions still aren't getting detected in pygame](https://stackoverflow.com/questions/63465025/collisions-still-arent-getting-detected-in-pygame/63465289#63465289)  
  ![Collisions still aren't getting detected in pygame](https://i.sstatic.net/OkZC7.gif)

📁 **[Minimal example - Minimal sprite collide](../../examples/minimal_examples/pygame_minimal_sprite_collide.py)**

📁 **[Minimal example - Minimal sprite collide (class)](../../examples/minimal_examples/pygame_minimal_intersect_spritecollide_class.py)**

### Sprite collide with Sprite

Related Stack Overflow questions:

- [How do I register collisions with objects from the same class without an unwanted object from another class in my group?](https://stackoverflow.com/questions/63060249/how-do-i-register-collisions-with-objects-from-the-same-class-without-an-unwante/63062808#63062808)

#### User defined collide function

Related Stack Overflow questions:

- [How to make entities take damage with color collision in pygame?](https://stackoverflow.com/questions/65645443/how-to-make-entities-take-damage-with-color-collision-in-pygame/65645826#65645826)  
  ![[How to make entities take damage with color collision in pygame?](https://i.sstatic.net/ObuMK.gif)  

  📁 **[Minimal example - User defined collision function](../../examples/minimal_examples/pygame_minimal_intersect_spritecollide_userdefined_callback.py)**

### Sprite collide with Group

Related Stack Overflow questions:

- [Pygame - getting a sprite to cycle through images in a class, and assign a hitbox](https://stackoverflow.com/questions/59904989/pygame-getting-a-sprite-to-cycle-through-images-in-a-class-and-assign-a-hitbo/59908083#59908083)
- [Tank collides with walls in pygame](https://stackoverflow.com/questions/61125022/tank-collides-with-walls-in-pygame/61125257#61125257)

### Group collide with Group

Related Stack Overflow questions:

- [How to verify collision between two sprites in the same pygame.sprite.Group()?](https://stackoverflow.com/questions/70440940/how-to-verify-collision-between-two-sprites-in-the-same-pygame-sprite-group/70440991#70440991)  
- [Permanently delete sprite from memory Pygame](https://stackoverflow.com/questions/67313034/permanently-delete-sprite-from-memory-pygame/67313844#67313844)  
- [pygame.sprite.groupcollide() does not work when trying to implement collision in pygame](https://stackoverflow.com/questions/63997798/pygame-sprite-groupcollide-does-not-work-when-trying-to-implement-collision-in/63998275#63998275)  
- [How to use groupcollide?](https://stackoverflow.com/questions/67890545/how-to-use-groupcollide/67890672#67890672)  

### Circular sprite collision

Related Stack Overflow questions:

- [Curvy snake collision with itself](https://stackoverflow.com/questions/63168090/curvy-snake-collision-with-itself/63180315#63180315)

### Sprite collide with frame, window border and restrict to rectangle

Related Stack Overflow questions:

- [How to make my sprite bounce off the boundaries in pygame](https://stackoverflow.com/questions/64839823/how-to-make-my-sprite-bounce-off-the-boundaries-in-pygame/64842460?noredirect=1)


## Bounding rectangle

Related Stack Overflow questions:

- [How to pin an image in the center of sprite rect](https://stackoverflow.com/questions/74973872/how-to-pin-an-image-in-the-center-of-sprite-rect/74973887#74973887)  
  ![How to pin an image in the center of sprite rect](https://i.sstatic.net/ac49b.png)  

## Sprite mask

Related Stack Overflow questions:

- **[Can't figure out how to check mask collision between two sprites](https://stackoverflow.com/questions/71535185/cant-figure-out-how-to-check-mask-collision-between-two-sprites/71536155#71536155)**  
  ![Can't figure out how to check mask collision between two sprites](https://i.sstatic.net/Z2vmv.gif)

  📁 **[Minimal example - Find the mask intersection of sprites](../../examples/minimal_examples/pygame_minimal_sprite_mask_intersect_2.py)**

- **[How can I made a collision mask?](https://stackoverflow.com/questions/56043600/how-can-i-made-a-collision-mask/56045037#56045037)**
- **[Pygame mask collision](https://stackoverflow.com/questions/60077813/pygame-mask-collision/60078039#60078039)**  
  [![Pygame mask collision](https://i.sstatic.net/fiLMi.gif)](https://stackoverflow.com/questions/60077813/pygame-mask-collision/60078039#60078039)

  📁 **[Minimal example - Find the intersection of rotating sprites](../../examples/minimal_examples/pygame_minimal_sprite_mask_intersect.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-SpriteMask](https://replit.com/@Rabbid76/PyGame-SpriteMask#main.py)**

- **[Make a line as a sprite with its own collision in Pygame](https://stackoverflow.com/questions/34456195/make-a-line-as-a-sprite-with-its-own-collision-in-pygame/65324946#65324946)**  
  ![Make a line as a sprite with its own collision in Pygame](https://i.sstatic.net/tMq2i.gif)

  📁 **[Minimal example - Find the intersection of sprites a nd line](../../examples/minimal_examples/pygame_minimal_sprite_mask_intersect_surface_line.py)**

[`pygame.sprite.collide_mask()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_mask) use the `.rect` and `.mask` attribute of the sprite object for the collision detection.

See the documentation of [`pygame.sprite.collide_mask()`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_mask):

>Collision detection between two sprites, using masks.
>
>```py
>collide_mask(SpriteLeft, SpriteRight) -> point
>```
>
>**Tests for collision between two sprites**, by testing if their bitmasks overlap. If the sprites have a "mask" attribute, that is used as the mask, otherwise a mask is created from the sprite image. Intended to be passed as a collided callback function to the *collide functions. Sprites must have a "rect" and an optional "mask" attribute.

## Sprite chang color of area

Related Stack Overflow questions:

- [Changing colour of a surface without overwriting transparency](https://stackoverflow.com/questions/64190277/changing-colour-of-a-surface-without-overwriting-transparency/64193109#64193109)  
  ![Changing colour of a surface without overwriting transparency](https://i.sstatic.net/oldLt.gif)

  📁 **[Minimal example - Chang the color of an area of a Sprite](../../examples/minimal_examples/pygame_minimal_blend_surface_tint_grayscale_1.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-ChangeColorOfSpriteArea](https://replit.com/@Rabbid76/PyGame-ChangeColorOfSpriteArea#main.py)**

## Animation, timing and Sprite sheet

Related Stack Overflow questions:

- [How do I create animated sprites using Sprite Sheets in Pygame?](https://stackoverflow.com/questions/55200501/pygame-window-crashing-and-sprite-sheet-issue/55200625#55200625)  
  ![How do I create animated sprites using Sprite Sheets in Pygame?](https://i.sstatic.net/Ekuju.gif)
- [Play animation upon collision with enemy](https://stackoverflow.com/questions/61964552/play-animation-upon-collision-with-enemy/61968944#61968944)
- [trying to get sprite to disappear from screen after certain amount of time](https://stackoverflow.com/questions/62614228/trying-to-get-sprite-to-disappear-from-screen-after-certain-amount-of-time/62614388#62614388)
- [Animated sprite from few images](https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images/64668964#64668964)
c
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

📁 **[Minimal example - Animated sprites](../../examples/minimal_examples/pygame_minimal_sprite_animated_gif_pil.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-SpriteAnimation](https://replit.com/@Rabbid76/PyGame-SpriteAnimation#main.py)**

![Animated sprite from few images](https://i.sstatic.net/SzKwL.gif)

## Rotate Sprite

Related Stack Overflow questions:

- [How can you rotate an image around an off center pivot in PyGame](https://stackoverflow.com/questions/59909942/how-can-you-rotate-an-image-around-an-off-center-pivot-in-pygame/59909946#59909946/59909946#59909946)  
  ![How can you rotate an image around an off center pivot in PyGame](https://i.sstatic.net/BmG1u.gif)

  📁 **[Minimal example - Rotate Sprite around off center pivot](../../examples/surface_rotate/pygame_sprite_rotate_pivot_boomerang.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-RotateSpriteAroundOffCenterPivot](https://replit.com/@Rabbid76/PyGame-RotateSpriteAroundOffCenterPivot#main.py)**

### Follow mouse

Related Stack Overflow questions:

- [How do I rotate a sprite towards the mouse and move it?](https://stackoverflow.com/questions/64805267/in-the-pygame-module-no-matter-what-i-change-the-coordinates-of-player-to-it-w/64806308#64806308)

  📁 **[Minimal example - Rotate Sprite to mouse](../../examples/minimal_examples/pygame_minimal_sprite_rotate_to_mouse.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-SpriteRotateToMouse](https://replit.com/@Rabbid76/PyGame-SpriteRotateToMouse#main.py)**

  ![How do I rotate a sprite towards the mouse and move it?](https://i.sstatic.net/DYZHI.gif)

  📁 **[Minimal example - Sprite follows mouse](../../examples/minimal_examples/pygame_minimal_sprite_follow_mouse.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-SpriteFollowMouse](https://replit.com/@Rabbid76/PyGame-SpriteFollowMouse#main.py)**

  ![How do I rotate a sprite towards the mouse and move it?](https://i.sstatic.net/7ONS1.gif)

## Click Sprite

Related Stack Overflow questions:

- [Pygame mouse clicking detection](https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection/64533684#64533684)  
  ![Pygame mouse clicking detection](https://i.sstatic.net/mW6vv.gif)

  📁 **[minimal example - Detect click on sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_click.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseClick](https://replit.com/@Rabbid76/PyGame-MouseClick#main.py)**

- [How can I add an image or icon to a button rectangle in Pygame?](https://stackoverflow.com/questions/64990710/how-can-i-add-an-image-or-icon-to-a-button-rectangle-in-pygame/64990819#64990819)  
  ![How can I add an image or icon to a button rectangle in Pygame?](https://i.sstatic.net/DnQdC.gif)

  📁 **[minimal example - Detect click on sprite 2](../../examples/minimal_examples/pygame_minimal_sprite_mouse_click_2.py)**

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
  ![Pygame mouse clicking detection](https://i.sstatic.net/UJVKi.gif)

  📁 **[minimal example - Detect Sprite on hover](../../examples/minimal_examples/pygame_minimal_sprite_mouse_hover.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseHover](https://replit.com/@Rabbid76/PyGame-MouseHover#main.py)**

- [How do I add a border to a sprite when the mouse hovers over it, and delete it after the mouse stops?0](https://stackoverflow.com/questions/70384004/how-do-i-add-a-border-to-a-sprite-when-the-mouse-hovers-over-it-and-delete-it-a/70384279#70384279)  
  ![How do I add a border to a sprite when the mouse hovers over it, and delete it after the mouse stops?](https://i.sstatic.net/DQdGr.gif)

  📁 **[minimal example - Hover and delete](../../examples/minimal_examples/pygame_minimal_sprite_mouse_hover_3.py)**

- [How can I add an image or icon to a button rectangle in Pygame?](https://stackoverflow.com/questions/64990710/how-can-i-add-an-image-or-icon-to-a-button-rectangle-in-pygame/64990819#64990819)  
  ![How can I add an image or icon to a button rectangle in Pygame?](https://i.sstatic.net/UEIde.gif)

  📁 **[minimal exame_minample - Detect Sprite on hover 2_2](../../examples/minimal_examples/pygimal_sprite_mouse_hover.py)**

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

- [Drag multiple sprites with different “update ()” methods from the same Sprite class in Pygame](https://stackoverflow.com/questions/64419223/drag-multiple-sprites-with-different-update-methods-from-the-same-sprite-cl/64456959#64456959)  
  ![Drag multiple sprites with different “update ()” methods from the same Sprite class in Pygame](https://i.sstatic.net/BaFzb.gif)

  📁 **[Minimal example - Drag Sprite](../../examples/minimal_examples/pygame_minimal_sprite_mouse_drag.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-MouseDrag](https://replit.com/@Rabbid76/PyGame-MouseDrag#main.py)**

- [How to draw a chessboard with Pygame and move the pieces on the board??](https://stackoverflow.com/questions/66467383/how-to-draw-a-chessboard-with-pygame-and-move-the-pieces-on-the-board/66514748#66514748)  
  ![How to draw a chessboard with Pygame and move the pieces on the board??](https://i.sstatic.net/i0a0N.gif)

  📁 **[Minimal example - Drag chess pieces](../../examples/minimal_examples/pygame_minimal_mouse_drag_chess.py)**

## Circular sprite

Related Stack Overflow questions:

- [how to create a circular sprite in pygame](https://stackoverflow.com/questions/61429734/how-to-create-a-circular-sprite-in-pygame/61429811#61429811)  
- [OOP Pygame Circle](https://stackoverflow.com/questions/65499220/oop-pygame-circle/65499257#65499257)  

## Health Bar

Related Stack Overflow questions:

- [How to put a health bar over the sprite in pygame](https://stackoverflow.com/questions/64867475/how-to-put-a-health-bar-over-the-sprite-in-pygame/64878954#64878954)  
  ![How to put a health bar over the sprite in pygame](https://i.sstatic.net/eapda.gif)

  📁 **[Minimal example - Drag Sprite](../../examples/minimal_examples/pygame_minimal_sprite_health_bar.py)**

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-HealthBar](https://replit.com/@Rabbid76/PyGame-HealthBar#main.py)**
  
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

- [How to create a text input box with pygame?](https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame/64613666#64613666)  
  ![How to create a text input box with pygame?](https://i.sstatic.net/FNJeM.gif)

  **[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-SpriteTextInput](https://replit.com/@Rabbid76/PyGame-SpriteTextInput#main.py)**

  📁 **[minimal example - Text input box](../../examples/minimal_examples/pygame_minimal_sprite_text_input_box.py)**

### Radio button

Related Stack Overflow questions:

- [How do I implement option buttons and change the button color in PyGame?](https://stackoverflow.com/questions/65059267/how-do-i-implement-option-buttons-and-change-the-button-color-in-pygame/65059852#65059852)  
  ![How do I implement option buttons and change the button color in PyGame?](https://i.sstatic.net/pPyUV.gif)

📁 **[Minimal example - Radio button](../../examples/minimal_examples/pygame_minimal_sprite_mouse_radiobutton.py)**

**[![](https://i.sstatic.net/5jD0C.png) repl.it/@Rabbid76/PyGame-RadioButton](https://replit.com/@Rabbid76/PyGame-RadioButton#main.py)**
