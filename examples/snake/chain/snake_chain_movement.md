# How do I chain the movement of a snake's body?

I want to implement a snake game. The snake meanders through the playground. Every time when the snake _eats_ some food, then length of the snake increase by 1.
The elements of the snakes body of the snake follow its head like a chain.

How do I accomplish, that the body parts follow the snake's head on its path, when the snake's head moves ahead?

---

# Answer

In general you have to distinguish between 2 different types of _snake_. In the first case, the snake moves in a grid and every time when the snake moves, it strides ahead one field in the grid. In the other type, the snakes position is not in a raster and not snapped on the fields of the grid, the position is free and the snake slides smoothly through the fields.  
In former each element of the body is snapped to the fields of the grid, as the head is. The other is more trick, because the position of a body element depends on the size of the element and the dynamic, previous positions of the snakes head.

---

First the _snake_, which is snapped to a grid.

The elements of the snake can be stored in a list of tuples.  Each tuple contains the column and row of the snakes element in the grid. The changes to the items in the list directly follow the movement of the snake. If the snake moves, a the new position is add to the head of the list and the tail of the list is removed.  

For instance we have a snake with the following elements:

```py
body = [(3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]
```

When the snakes head moves form `(3, 3)` to (`3, 2`), then the new head position is add to the head of the list (`body.insert(0, (3, 2)`):

```py
body = [(3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]
```

Finally the tail of the ist is removed (`del body[-1]`):

```py
body = [(3, 2), (3, 3), (3, 4), (4, 4), (5, 4)]
```

![](https://i.imgur.com/1EoDFcU.png)

Example:

![](https://i.imgur.com/aglb1HN.gif)

```py
import pygame
import random

pygame.init()
COLUMNS, ROWS, SIZE = 10, 10, 20
screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))
clock  = pygame.time.Clock()
font = pygame.font.SysFont(None, 18)

background = pygame.Surface((COLUMNS*SIZE, ROWS*SIZE))
background.fill((255, 255, 255))
for i in range(2, COLUMNS-1):
    pygame.draw.line(background, (128, 128, 128), (i*SIZE-1, SIZE), (i*SIZE-1, (ROWS-1)*SIZE), 2)
for i in range(2, ROWS-1):
    pygame.draw.line(background, (128, 128, 128), (SIZE, i*SIZE-1), ((COLUMNS-1)*SIZE, i*SIZE-1), 2)
for i in range(COLUMNS-2):
    label = font.render(str(i), True, (0, 0, 0), (255, 255, 255))
    background.blit(label, (i*SIZE + 26, 5))
    background.blit(label, (6, i*SIZE + 25))

length = 1
body = [(3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]

run = True
while run:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for i in reversed(range(len(body))):
        pos = body[i]
        color = (255, 128, 0) if i== 0 else (128, 128, 128) if i == len(body)-1 else (0, 128, 0)
        pygame.draw.rect(screen, color, ((pos[0]+1)*SIZE, (pos[1]+1)*SIZE, SIZE, SIZE), 6)

    pn = ((body[0][0]+1)*SIZE + SIZE//2), ((body[0][1]+1)*SIZE + SIZE//2)
    ph = ((body[1][0]+1)*SIZE + SIZE//2), ((body[1][1]+1)*SIZE + SIZE//2)
    pt = ((body[-1][0]+1)*SIZE + SIZE//2), ((body[-1][1]+1)*SIZE + SIZE//2)

    pygame.draw.line(screen, (255, 0, 0), (pt[0]-SIZE, pt[1]-SIZE), (pt[0]+SIZE, pt[1]+SIZE), 3)
    pygame.draw.line(screen, (255, 0, 0), (pt[0]-SIZE, pt[1]+SIZE), (pt[0]+SIZE, pt[1]-SIZE), 3)

    pygame.draw.circle(screen, (255, 0, 0), ph, 5)
    pygame.draw.line(screen, (255, 0, 0), pn, ph, 3)
    pygame.draw.polygon(screen, (255, 0, 0), [(pn[0]-5, pn[1]+3), (pn[0]+5, pn[1]+3), (pn[0], pn[1]-7)])

    pygame.display.flip()
``` 

---

Now the _snake_ with completely free positioning.

We have to track all the positions which the snake's head has visited in a list. We have to place the elements of the snakes body on the positions in the list like the pearls of a chain.

![](https://i.imgur.com/N6QIt6a.png)

The key is, to compute the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between the last element of the body in the chain and the following positions on the track.
When an new point with a distance that is large enough is found, then an new pearl (element) is add to the chain (body).

```py
dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
if math.sqrt(dx*dx + dy*dy) >= distance:
    body.append(pos)
```

The following function has 3 arguments. `track` is the list of the head positions. `no_pearls` is then number of elements of the shakes body and `distance` is the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between the elements. The function creates and returns a list of the snakes body positions.

```py
def create_body(track, no_pearls, distance):
    body = [(track[0])]
    track_i = 1
    for i in range(1, no_pearls):
        while track_i < len(track):
            pos = track[track_i]
            track_i += 1
            dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
            if math.sqrt(dx*dx + dy*dy) >= distance:
                body.append(pos)
                break
    while len(body) < no_pearls:
        body.append(track[-1])
    del track[track_i:]
    return body
```

Example:

![](https://i.imgur.com/QrA5rTb.gif)

```py
import pygame
import random
import math

pygame.init()
COLUMNS, ROWS, SIZE = 10, 10, 20
WIDTH, HEIGHT = COLUMNS*SIZE, ROWS*SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock  = pygame.time.Clock()

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((255, 255, 255))
for i in range(1, COLUMNS):
    pygame.draw.line(background, (128, 128, 128), (i*SIZE-1, 0), (i*SIZE-1, ROWS*SIZE), 2)
for i in range(1, ROWS):
    pygame.draw.line(background, (128, 128, 128), (0, i*SIZE-1), (COLUMNS*SIZE, i*SIZE-1), 2)

def hit(pos_a, pos_b, distance):
    dx, dy = pos_a[0]-pos_b[0], pos_a[1]-pos_b[1]
    return math.sqrt(dx*dx + dy*dy) < distance

def random_pos(body):
    pos = None
    while True:
        pos = random.randint(SIZE//2, WIDTH-SIZE//2), random.randint(SIZE//2, HEIGHT-SIZE//2)
        if not any([hit(pos, bpos, 20) for bpos in body]):
            break    
    return pos

def create_body(track, no_pearls, distance):
    body = [(track[0])]
    track_i = 1
    for i in range(1, no_pearls):
        while track_i < len(track):
            pos = track[track_i]
            track_i += 1
            dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
            if math.sqrt(dx*dx + dy*dy) >= distance:
                body.append(pos)
                break
    while len(body) < no_pearls:
        body.append(track[-1])
    del track[track_i:]
    return body

length = 1
track = [(WIDTH//2, HEIGHT//2)]
dir = (1, 0)
food = random_pos(track)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: dir = (-1, 0)
            elif event.key == pygame.K_RIGHT: dir = (1, 0)
            elif event.key == pygame.K_UP: dir = (0, -1)
            elif event.key == pygame.K_DOWN: dir = (0, 1)

    track.insert(0, track[0][:])    
    track[0] = (track[0][0] + dir[0]) % WIDTH, (track[0][1] + dir[1]) % HEIGHT

    body = create_body(track, length, 20)

    if hit(body[0], food, 20):
        food = random_pos(body)
        length += 1 
        
    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, (255, 0, 255), food, SIZE//2)
    for i, pos in enumerate(body):
        color = (255, 0, 0) if i==0 else (0, 192, 0) if (i%2)==0 else (255, 128, 0)
        pygame.draw.circle(screen, color, pos, SIZE//2)
    pygame.display.flip()
```