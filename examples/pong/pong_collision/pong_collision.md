
# StackOverflow Question

[Sometimes the ball doesn't bounce off the paddle in pong game](https://stackoverflow.com/questions/62864205/sometimes-the-ball-doesnt-bounce-off-the-paddle-in-pong-game)

# Possibly duplicates

[How to fix collision of a ball with a rect object in pygame](https://stackoverflow.com/questions/62850745/how-to-fix-collision-of-a-ball-with-a-rect-object-in-pygame/62850903#62850903)  
[How to stop a ball from “phasing” through the paddle?](https://stackoverflow.com/questions/62763984/how-to-stop-a-ball-from-phasing-through-the-paddle/62764506#62764506)  

# Sometimes the ball doesn't bounce off the paddle in pong game

I have a simple pong game that mostly works well. But sometimes it occurs the the ball doesn't bounce of the paddle. The ball wobbles and slides along the paddle and the paddle seems to magnetically pull the ball as shown in the gif:

![](https://i.imgur.com/tF3EwGX.gif)

Every time when the rectangle which surrounds the ball, collides the the paddle rectangle, the the direction of the ball is changed:

```py
if ball.colliderect(paddleLeft):
    move_x *=-1
if ball.colliderect(paddleRight):
    move_x *=-1
```

What causes the behavior?

The issue can be reproduced with the following complete, minimal and verifiable example. The position of the ball is set so that the wrong behavior occurs immediately if the right paddle is not moved:

```py
import pygame

pygame.init()
width, height = 600, 400
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

radius = 10
move_x, move_y = 3, 3
ball = pygame.Rect(width//2+125, 20, radius*2, radius)
paddleHeight = 80
paddleLeft = pygame.Rect(20, (height-paddleHeight)//2, 10, paddleHeight)
paddleRight = pygame.Rect(width-30, (height-paddleHeight)//2, 10, paddleHeight)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddleLeft.top > 0: paddleLeft.y -= 5
    if keys[pygame.K_s] and paddleLeft.bottom < height: paddleLeft.y += 5
    if keys[pygame.K_UP] and paddleRight.top > 0: paddleRight.y -= 5
    if keys[pygame.K_DOWN] and paddleRight.bottom < height: paddleRight.y += 5

    ball.x += move_x
    ball.y += move_y
    if ball.left <= 0 or ball.right >= width: move_x *=-1
    if ball.top <= 0 or ball.bottom >= height: move_y *=-1

    if ball.colliderect(paddleLeft):
        move_x *=-1
    if ball.colliderect(paddleRight):
        move_x *=-1

    window.fill(0)
    pygame.draw.rect(window, (255, 255, 255), paddleLeft)
    pygame.draw.rect(window, (255, 255, 255), paddleRight)
    pygame.draw.circle(window, (255, 255, 255), ball.center, radius)
    pygame.display.flip()
```

---

# Answer

The behavior occurs, when the ball doesn't hit the paddle at the front, but at the top or bottom. Actually the collision between the paddle and the ball is detected and the direction is changed. But the ball penetrated so deep into the paddle that the ball cannot leave the collision area with the paddle with it's next step. This causes that a collision is detected again in the next frame and the direction of the ball is changed again. Now the ball moves in the same direction as before the first collision. This process continues until the ball _leaves_ the paddle at the bottom. This causes a zig zag movement along the front side of the paddle.  

![](https://i.imgur.com/w2DrOft.gif)

There are different solution. One option is not to reverse the direction, but to set the direction to the left when the right paddle is hit a nd to set the direction to the right when the left paddle is hit:

```py
if ball.colliderect(paddleLeft):
    move_x = abs(move_x)
if ball.colliderect(paddleRight):
    move_x = -abs(move_x) 
```

![](https://i.imgur.com/6duDp6g.gif)

Another option is to adjust the position to the ball. If the right paddle is hit, the right side of the ball must be placed to the left of the paddle. If the left paddle is hit, then the left side of the ball must be placed to the right of the paddle:

```py
if ball.colliderect(paddleLeft):
    move_x *= -1
    ball.left = paddleLeft.right
if ball.colliderect(paddleRight):
    move_x *= -1
    ball.right = paddleRight.left
```

![](https://i.imgur.com/gDbt3JH.gif)