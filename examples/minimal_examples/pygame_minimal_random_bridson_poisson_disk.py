# Random non overlapping circles(with circle number controlled) in python and pygame
# https://stackoverflow.com/questions/62079192/random-non-overlapping-circleswith-circle-number-controlled-in-python-and-pyga
#
# Sebastion Lague explained the Bridson's algorithm
# https://www.youtube.com/watch?v=7WcmyxyFO7o
#
# My implementation of Bridson's algorithm Poisson-Disk Sampling seems to be stuck in an infinite loop
# https://stackoverflow.com/questions/58240188/my-implementation-of-bridsons-algorithm-poisson-disk-sampling-seems-to-be-stuck/58241165#58241165
#
# GitHub - PyGameExamplesAndAnswers - Random and random distribution - Random distribution
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_random_and_random_distribution.md

import pygame
import math
import random

def FindNeighbours(cellNumberX, cellNumberY, index, cellGrid):
    neighbours = []
    for cellX in range(max(0, index[0]-2), min(cellNumberX, index[0]+3)):
        for cellY in range(max(0, index[1]-2), min(cellNumberY, index[1]+3)):
            if cellGrid[cellX][cellY] != None:
                neighbours.append(cellGrid[cellX][cellY])
    return neighbours

def PoissonDiskSampling(width, height, radius, startPos = None, spawnAttempts = 10):

    if startPos == None:
        startPos = [width//2,height//2]

    cellSize = radius / math.sqrt(2)
    cellNumberX = int(width // cellSize + 1)
    cellNumberY = int(height // cellSize + 1)
    cellGrid = [[None for x in range(cellNumberX)] for y in range(cellNumberY)]

    startingPoint = pygame.math.Vector2(*startPos)
    cellGrid[int(startingPoint.x/radius)][int(startingPoint.y/radius)] = startingPoint

    points = [startingPoint]
    spawnpoints = [startingPoint]

    while len(spawnpoints) > 0:

        spawnIndex = random.randint(0,len(spawnpoints)-1)
        #spawnIndex = 0
        spawnpoint = spawnpoints[spawnIndex]

        spawned = False
        for _ in range(spawnAttempts):

            r = random.uniform(radius, 2*radius)
            radian = random.uniform(0, 2*math.pi)
            newPoint = pygame.math.Vector2(spawnpoint.x + r*math.cos(radian), spawnpoint.y + r*math.sin(radian))
            if not (0 <= newPoint.x <= width and 0 <= newPoint.y <= height):
               continue

            newPointIndex = [int(newPoint.x/cellSize), int(newPoint.y/cellSize)]
            if cellGrid[newPointIndex[0]][newPointIndex[1]] != None:
                continue
            
            neighbours = FindNeighbours(cellNumberX, cellNumberY, newPointIndex, cellGrid)
            if all(newPoint.distance_squared_to(neighbour) >= radius**2 for neighbour in neighbours):
                cellGrid[newPointIndex[0]][newPointIndex[1]] = newPoint
                points.append(newPoint)
                spawnpoints.append(newPoint)
                spawned = True
                break

        if spawned == False:
            spawnpoints.remove(spawnpoint)

    return points

pygame.init()
window = pygame.display.set_mode((350, 350))
clock = pygame.time.Clock()

margin = 20
count = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False

    if count == 0:
        pts = PoissonDiskSampling(window.get_width()-margin*2, window.get_height()-margin*2, 15)
    count += 1
    if count >= len(pts):
        count = 0

    window.fill(0)
    for pt in pts[:count]:
        pygame.draw.circle(window, (255, 255, 255), (round(pt.x+margin), round(pt.y+margin)), 3)
    pygame.display.flip()

pygame.quit()