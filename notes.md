[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

# Code snippets at repl.it

![replt-it-40](https://i.stack.imgur.com/rp0yV.png)
![replt-it-32](https://i.stack.imgur.com/5jD0C.png)

[repl.it](https://repl.it/repls/folder/PyGame%20Examples)

## Template

```py
# GitHub:
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_event_and_application_loop.md
#
# Stack Overflow:
# https://stackoverflow.com/questions/63540062/pygame-unresponsive-display/63540113#63540113
```

```lang-none
<kbd>[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-MinimalApplicationLoop](https://repl.it/@Rabbid76/PyGame-MinimalApplicationLoop#main.py)</kbd>
```

```lang-none
<kbd>[![][1] repl.it/@Rabbid76/PyGame-MinimalApplicationLoop](https://repl.it/@Rabbid76/PyGame-MinimalApplicationLoop#main.py)</kbd>

  [1]: https://i.stack.imgur.com/5jD0C.png
```

# Investigate answered questions

up to answered Nov 1 by Rabbid76

[PyGame votes](https://stackoverflow.com/questions/tagged/pygame?tab=Votes)

## add answers

next:

[Pygame water ripple effect](https://stackoverflow.com/questions/7648072/pygame-water-ripple-effect)  
[Pygame water physics not working as intended](https://stackoverflow.com/questions/62499733/pygame-water-physics-not-working-as-intended)  

[Does pyGame do 3d?](https://stackoverflow.com/questions/4865636/does-pygame-do-3d)  
[Difference between pygame.display.update and pygame.display.flip](https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip)  
[Basic networking with Pygame](https://stackoverflow.com/questions/9961752/basic-networking-with-pygame)  
[What fonts can I use with pygame.font.Font?](https://stackoverflow.com/questions/38001898/what-fonts-can-i-use-with-pygame-font-font)  
[How can I crop an image with Pygame?](https://stackoverflow.com/questions/6239769/how-can-i-crop-an-image-with-pygame)  
[How to Change the Name of a Pygame window?](https://stackoverflow.com/questions/40566585/how-to-change-the-name-of-a-pygame-window)  
[Any way to speed up Python and Pygame?](https://stackoverflow.com/questions/6395923/any-way-to-speed-up-python-and-pygame)  

interesting

[Intersection between bezier curve and a line segment](https://stackoverflow.com/questions/1813719/intersection-between-bezier-curve-and-a-line-segment)  

## Questions about size, and resizing

[Allowing resizing window pyGame](https://stackoverflow.com/questions/11603222/allowing-resizing-window-pygame)
[How to get the resolution of a monitor in Pygame?](https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame)  

## Not answered questions

[How to make parallax scrolling work properly with a camera that stops at edges pygame](https://stackoverflow.com/questions/63712333/how-to-make-parallax-scrolling-work-properly-with-a-camera-that-stops-at-edges-p)

## Fix examples

- pygame_minimal_intersect_circle_rectangle_4.py: fix intersection of edge with circle (increase rectangle 100x100)

## Investigate

[How to make keyboard Input into unicode/japanese characters?](https://stackoverflow.com/questions/64543224/how-to-make-keyboard-input-into-unicode-japanese-characters)
[Update during resize in Pygame](https://stackoverflow.com/questions/64543449/update-during-resize-in-pygame)

## pages

- random movement
- grid
- memory
- maze
- snake  
  related questions: [how to solve bug on snake wall teleportation](https://stackoverflow.com/questions/64624092/how-to-solve-bug-on-snake-wall-teleportation/64624385#64624385) and many more

- pong

## Questions

### Move and stay in window

Add question: How do i keep my player in the window.

Answer: 1. use `clmap_ip`; 2. Use modulo (%) operator

### How to create rectangle centered around a point

Why is there no `pygame.Rect(0, 0, w, t).get_rect(center = (x, y))`

`rect = pygame.Rect(x, y, 0, 0).inflate(x, h)`

## Random enemies

1. Spawn enemies (represented by a red dot) at random locations one after the other at certain intervals The enemies should not intersect and keep a minimum distance to each other.

1. Implement a swarm movement.

## Web

[is it possible to run pygame or pyglet in a browser?](https://stackoverflow.com/questions/8452927/is-it-possible-to-run-pygame-or-pyglet-in-a-browser)

## URL

[Convert Image from Request to Pygame Surface](https://stackoverflow.com/questions/57023015/convert-image-from-request-to-pygame-surface)

## Memory game

Simple 4x4 memory ga,e

## Rubik's

PyGame CPU Rubik's  
PyGame OpenGL Rubik's

## Leap Motion

[Leap Motion](https://www.ultraleap.com/)

## Color

[`pygame.Color`](https://www.pygame.org/docs/ref/color.html) object

## Pong

Sophisticated circle and rectangle intersection

[Sometimes the ball doesn't bounce off the paddle in pong game](https://stackoverflow.com/questions/62864205/sometimes-the-ball-doesnt-bounce-off-the-paddle-in-pong-game)

(update question title)

Compute relative movement of sphere and rectangle. Find intersection on the way.

## PyGame object library

Shapes class like circle, ellipse, triangle, polygon etc. based on `pygame.Rectangle`. _Sprite_ class (`SpriteShape`) which can represent a shape class. Operator which can compute the intersections of the shapes.

## Platform game

Intersect with lines instead of rectangles. Optionally lines can have an intersecting and a non intersecting side (normal vector). The intersection with blocks can be determined by the intersection with 1, 3 or 4 lines, where the intersection just works if the object comes from the "outside" the block and not from "inside" the bolck.  
