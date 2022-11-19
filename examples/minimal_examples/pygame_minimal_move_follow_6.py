# Pygame sprites overlapping issue
# https://stackoverflow.com/questions/66291255/pygame-sprites-overlapping-issue/66291672#66291672 
#
# Pygame object instance speed increases
# https://stackoverflow.com/questions/66943486/pygame-object-instance-speed-increases  
#
# Python Pygame Making a ball push another ball
# https://stackoverflow.com/questions/66721398/python-pygame-making-a-ball-push-another-ball
#
# GitHub - Motion and movement - Physics
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame, math, random

class Ball():
    def __init__(self, color, pos, radius, vel):
        super().__init__()
        self.color = color
        self.pos = pos
        self.radius = radius
        self.vel = vel

    def draw(self):
        pygame.draw.circle(window, self.color, self.pos, self.radius)

def move_to(pos, target_pos, vel):
    dx, dy = target_pos[0] - pos[0], target_pos[1]- pos[1]
    dist = math.hypot(dx, dy)
    if dist > 0:
        dx, dy = round(dx * vel / dist), round(dy * vel / dist)
        xyb = target_pos if dist < vel else [pos[0] + dx,  pos[1] + dy]  
    return xyb

def collide_and_react(xyb, xyb1, radius1, radius2):
    dx, dy = xyb1[0]- xyb[0], xyb1[1]- xyb[1]
    distance = math.hypot(dx, dy)
    if distance < radius1 + radius2 and distance != 0:
        overlap = (radius1 + radius2 - distance) / distance
        xyb = [xyb[0] - dx * overlap , xyb[1] - dy * overlap]
    return xyb

def new_follower_pos():
    return [
         random.choice([window.get_width() + random.randrange(10, 50) , 0 - random.randrange(10, 50)]), 
         random.choice([window.get_height() + random.randrange(10, 50) , 0 - random.randrange(10, 50)])]

pygame.init()
window = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()

player = Ball((0, 0, 255), [window.get_width() / 3, window.get_height() / 3], 15, 5)
obstacles = [Ball((0, 255, 0), window.get_rect().center, 45, 0)]
followers = [Ball((255, 0, 0), new_follower_pos(), 15, 2) for _ in range(10)]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    player.pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player.vel
    player.pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player.vel
    player.pos[0] = max(player.radius, min(window.get_width() - player.radius, player.pos[0]))
    player.pos[1] = max(player.radius, min(window.get_height() - player.radius, player.pos[1]))

    for i, f1 in enumerate(followers):
        f1.pos = move_to(f1.pos, player.pos, f1.vel) 

        for f2 in followers[i+1:]:   
            f1.pos = collide_and_react(f1.pos, f2.pos, f1.radius, f2.radius)                             
            
            for obstacle in obstacles:
                f1.pos = collide_and_react(f1.pos, obstacle.pos, f1.radius, obstacle.radius)
                player.pos = collide_and_react(player.pos, obstacle.pos, player.radius, obstacle.radius)
            
            player.pos = collide_and_react(player.pos, f1.pos, player.radius, f1.radius)
    
    window.fill(0) 
    for obstacle in obstacles:
        obstacle.draw()
    for follower in followers:
        follower.draw()
    player.draw()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()