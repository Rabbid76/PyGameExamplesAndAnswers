# Integrating sprite snippet into maze program]
# https://stackoverflow.com/questions/55833941/adding-collision-to-maze-walls/55837809#55837809
# 
# GitHub - PyGameExamplesAndAnswers - Maze
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_maze.md

import random
import pygame

pygame.init()
window = pygame.display.set_mode((701, 701))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, rows, cols, tilesize):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((200, 20, 20))
        self.random_position(cols, rows, tilesize)

    def random_position(self, cols, rows, tilesize):
        x = random.randint(0, rows-1) * tilesize + tilesize // 2
        y = random.randint(0, cols-1) * tilesize + tilesize // 2
        self.pos = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center = self.pos)

    def update(self, events, dt):
        pressed = pygame.key.get_pressed()
        move = pygame.Vector2((0, 0))

        # calculate maximum movement and current cell position  
        testdist = dt // 5 + 3
        cellx = self.rect.centerx // tilesize
        celly = self.rect.centery // tilesize
        minx = (self.rect.left-1) // tilesize
        maxx = (self.rect.right+1) // tilesize
        miny = (self.rect.top-1) // tilesize
        maxy = (self.rect.bottom+1) // tilesize

       # test move up
        if minx == maxx and pressed[pygame.K_UP]:
            nexty = (self.rect.top-testdist) // tilesize
            if celly == nexty or (nexty >= 0 and not grid[celly][cellx].walls[0]):
                move += (0, -1)

        # test move right
        elif miny == maxy and pressed[pygame.K_RIGHT]:
            nextx = (self.rect.right+testdist) // tilesize
            if cellx == nextx or (nextx < cols and not grid[celly][cellx].walls[1]):
                move += (1, 0)
               
        # test move down
        elif minx == maxx and pressed[pygame.K_DOWN]:
            nexty = (self.rect.bottom+testdist) // tilesize
            if celly == nexty or (nexty < rows and not grid[celly][cellx].walls[2]):
                move += (0, 1)            

        # test move left
        elif miny == maxy and pressed[pygame.K_LEFT]:
            nextx = (self.rect.left-testdist) // tilesize
            if cellx == nextx or (nextx >= 0 and not grid[celly][cellx].walls[3]):
                move += (-1, 0)
        
        self.pos = self.pos + move*(dt/5)
        self.rect.center = self.pos        

class Cell():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x * tilesize, y * tilesize, tilesize, tilesize)
        self.walls = [True, True, True, True] # top , right , bottom , left
        self.visited = False
        self.current = False

    def draw(self):
        if self.current:
            pygame.draw.rect(window, (255, 0, 0), self.rect)
        elif self.visited:
            pygame.draw.rect(window, (255, 255, 255), self.rect)
            if self.walls[0]:
                pygame.draw.line(window, (0, 0, 0, 0), self.rect.topleft, self.rect.topright, 1)
            if self.walls[1]:
                pygame.draw.line(window, (0, 0, 0, 0), self.rect.topright, self.rect.bottomright, 1)
            if self.walls[2]:
                pygame.draw.line(window, (0, 0, 0, 0), self.rect.bottomleft, self.rect.bottomright, 1)
            if self.walls[3]:
                pygame.draw.line(window, (0, 0, 0, 0), self.rect.topleft, self.rect.bottomleft, 1)

def checkNeighbors(cell):
    i, j = cell.rect.x // tilesize, cell.rect.y // tilesize
    neighbors = []
    for ni, nj in [(i, j-1), (i+1, j), (i, j+1), (i-1, j)]:
        if 0 <= ni < cols and 0 <= nj < rows and not grid[nj][ni].visited:
            neighbors.append(grid[nj][ni])
    return neighbors[random.randrange(0, len(neighbors))] if neighbors else None

def removeWalls(current_cell,next_cell):
    x = current_cell.rect.x // tilesize - next_cell.rect.x // tilesize
    y = current_cell.rect.y // tilesize - next_cell.rect.y // tilesize
    if x == -1: # right of current
        current_cell.walls[1] = False
        next_cell.walls[3] = False
    elif x == 1: # left of current
        current_cell.walls[3] = False
        next_cell.walls[1] = False
    elif y == -1: # bottom of current
        current_cell.walls[2] = False
        next_cell.walls[0] = False
    elif y == 1: # top of current
        current_cell.walls[0] = False
        next_cell.walls[2] = False

def new_grid():
    grid = []
    for y in range(rows):
        grid.append([])
        for x in range(cols):
            grid[y].append(Cell(x,y))
    return grid, grid[0][0]

tilesize = 25
cols = int(window.get_width() / tilesize)
rows = int(window.get_height() / tilesize)
stack = []
player = Player(cols, rows, tilesize)
sprites = pygame.sprite.Group()
sprites.add(player)

grid, current_cell = new_grid()

run = True
play = False 
while run:
    dt = clock.tick(60 if play else 300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if play == True:
        
        pygame.draw.rect(window, (255, 164, 164), player.rect)
        sprites.update(None, dt)
        sprites.draw(window)

        if pygame.Rect(0, 0, tilesize, tilesize).colliderect(player.rect):
            grid, current_cell = new_grid()
            player.random_position(cols, rows, tilesize)
            window.fill(0)
            play = False

    else:
        current_cell.visited = True
        current_cell.current = True

        next_cell = checkNeighbors(current_cell)
        if next_cell != None:
            stack.append(current_cell)
            removeWalls(current_cell,next_cell)
            current_cell.current = False
            current_cell = next_cell
        elif len(stack) > 0:
            current_cell.current = False
            current_cell = stack.pop()
        else:
            play = True

        for y in range(rows):
            for x in range(cols):
                grid[y][x].draw()

    pygame.display.flip()

pygame.quit()
exit()
