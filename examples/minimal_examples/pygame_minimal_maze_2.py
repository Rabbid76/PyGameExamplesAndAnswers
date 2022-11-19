# Pygame Maze Game not creating levels correctly
# https://stackoverflow.com/questions/59436266/pygame-maze-game-not-creating-levels-correctly/59436430#59436430
# 
# GitHub - PyGameExamplesAndAnswers - Maze
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_maze.md

import pygame
import random

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.south = True
        self.west = True
        self.visited = 0
    def clear_visit(self):
        self.visited = 0

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.generation_finished = True
        self.maze = [[Cell(x, y) for y in range(rows)] for x in range(cols)]

    def generate(self, start_cell = None, stack = None):
        if not self.generation_finished:
            return
        if start_cell == None:
            start_cell = self.maze[0][0]
        if stack == None:
            stack = []
        if len(stack) == 0:
            stack.append(start_cell)

        self.check_finished()
        cur_cell = stack[-1]
        neighbors = self.get_neighbors(cur_cell)
        random.shuffle(neighbors)

        for neighbor in neighbors:
            if neighbor.visited == 0:
                neighbor.visited = 1
                stack.append(neighbor)
                self.knock_wall(cur_cell, neighbor)
                self.generate(start_cell, stack)

    def clear_visit(self):
        [self.maze[x][y].clear_visit() for y in range(self.rows) for x in range(self.cols)]

    def get_neighbors(self, cell):
        return [self.maze[cell.x+n[0]][cell.y+n[1]] for n in [(0, -1), (0, 1), (1, 0), (-1, 0)] if 0 <= cell.x+n[0] < self.cols and 0 <= cell.y+n[1] < self.rows]

    def knock_wall(self, cell, neighbor):
        if cell.x == neighbor.x and cell.y + 1 == neighbor.y:
            cell.south = False
        elif cell.x == neighbor.x and cell.y - 1 == neighbor.y:
            neighbor.south = False
        elif cell.x + 1 == neighbor.x and cell.y == neighbor.y:
            cell.west = False
        elif cell.x - 1== neighbor.x and cell.y == neighbor.y:
            neighbor.west = False

    def can_pass(self, cell, neighbor):
        if cell.x == neighbor.x and cell.y + 1 == neighbor.y:
            return not cell.south
        elif cell.x == neighbor.x and cell.y - 1 == neighbor.y:
            return not neighbor.south
        elif cell.x + 1 == neighbor.x and cell.y == neighbor.y:
            return not cell.west
        elif cell.x - 1 == neighbor.x and cell.y == neighbor.y:
            return not neighbor.west
        return False

    def check_finished(self):
        self.generation_finished = any(cell.visited == 0 for column in self.maze for cell in column)

class Game:
    def __init__(self, screen, maze):
        self.size = screen.get_size()
        self.screen = screen
        self.maze_obj = maze
        self.reset()

    def reset(self):
        self.cell_width = self.size[0] / self.maze_obj.cols
        self.cell_height = self.size[1] / self.maze_obj.rows
        w, h = self.cell_width - 3, self.cell_height - 3
        rect = 0, 0, w, h
        base = pygame.Surface((w, h))
        base.fill((255, 255, 255))
        self.green_p = base.copy()
        self.blue_p = base.copy()
        self.goldy = base.copy()
        pygame.draw.ellipse(self.green_p, (0,255,0), rect)
        pygame.draw.ellipse(self.blue_p,  (0,0,255), rect)
        pygame.draw.ellipse(self.goldy, (0xc5,0x93,0x48), rect)
        self.cx, self.cy = 0, 0
        self.maze_obj.clear_visit()
       
    def run(self):
        self.clock = pygame.time.Clock()
        run = True
        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    elif event.key == pygame.K_r:
                        self.reset()
                    elif event.key == pygame.K_DOWN:
                        run = not self.move_player((0, 1))
                    elif event.key == pygame.K_UP:
                        run = not self.move_player((0, -1))
                    elif event.key == pygame.K_LEFT:
                        run = not self.move_player((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        run = not self.move_player((1, 0))    
            self.draw()
            pygame.display.update()

    def move_player(self, dir):
        x, y = self.cx + dir[0], self.cy + dir[1]
        if 0 <= x < self.maze_obj.cols and 0 <= y < self.maze_obj.rows:
            if self.maze_obj.can_pass(self.maze_obj.maze[self.cx][self.cy], self.maze_obj.maze[x][y]):
                self.maze_obj.maze[self.cx][self.cy].visited += 1
                self.cx, self.cy = x, y
        finished = self.cx + 1 == self.maze_obj.cols and self.cy + 1 == self.maze_obj.rows
        if finished:
            print ('You won!') 
        return finished

    def draw(self):
        self.screen.fill( (255,255,255) )
        
        for y in range(self.maze_obj.rows):
            for x in range(self.maze_obj.cols):
                if self.maze_obj.maze[x][y].south:
                    pygame.draw.line(self.screen, (0,0,0), \
                        (x * self.cell_width, (y+1) * self.cell_height), \
                        ((x+1) * self.cell_width, (y+1) * self.cell_height) )
                if self.maze_obj.maze[x][y].west:
                    pygame.draw.line(self.screen, (0,0,0), \
                        ((x+1) * self.cell_width, y * self.cell_height), \
                        ((x+1) * self.cell_width, (y+1) * self.cell_height) )                
        pygame.draw.rect(self.screen, (0,0,0), (0,0, self.size[0], self.size[1]), 1)

        for y in range(self.maze_obj.rows):
            for x in range(self.maze_obj.cols):
                if self.maze_obj.maze[x][y].visited >= 1:
                    self.screen.blit(self.green_p, (x*self.cell_width+2, y*self.cell_height+2))
        self.screen.blit(self.blue_p, (self.cx*self.cell_width+2, self.cy*self.cell_height+2))
        self.screen.blit(self.goldy, ((self.maze_obj.cols-1) * self.cell_width + 2, (self.maze_obj.rows-1) * self.cell_height + 2))

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Maze')

maze = Maze(10, 10)
maze.generate(maze.maze[0][0])

game = Game(window, maze)
game.run()

pygame.quit()
exit()

