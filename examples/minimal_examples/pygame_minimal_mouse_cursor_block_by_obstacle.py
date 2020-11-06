# pygame.mouse module
# https://www.pygame.org/docs/ref/mouse.html
#
# Make cursor unable to move through sprite pygame
# https://stackoverflow.com/questions/54509869/make-cursor-unable-to-move-through-sprite-pygame/54511823#54511823
#
# GitHub - Mouse - Change mouse position
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mouse_and_mosuse_events.md
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Line and line
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame

def IntersectEndlessLineLine(l1_p1, l1_p2, l2_p1, l2_p2):
    
    # calculate the line vectors and test if both lengths are > 0
    P = pygame.math.Vector2(*l1_p1)
    Q = pygame.math.Vector2(*l2_p1)
    line1 = pygame.math.Vector2(*l1_p2) - P
    line2 = pygame.math.Vector2(*l2_p2) - Q
    if line1.length() == 0 or line2.length() == 0:
        return (False, (0, 0))

    # check if the lines are not parallel
    R, S = (line1.normalize(), line2.normalize())
    dot_R_nvS = R.dot(pygame.math.Vector2(S[1], -S[0]))
    if abs(dot_R_nvS) < 0.001:
       return (False, (0, 0))

    # calculate the intersection point of the lines
    # t  =  dot(Q-P, (S.y, -S.x)) / dot(R, (S.y, -S.x))
    # X  = P + R * t
    ptVec = Q-P
    t = ptVec.dot(pygame.math.Vector2(S[1], -S[0])) / dot_R_nvS
    xPt = P + R * t
    return (True, (xPt[0], xPt[1]))

def InRange(coord, range_s, range_e):
    if range_s < range_e:
        return coord >= range_s and coord <= range_e
    return coord >= range_e and coord <= range_s

def PtInRect(pt, lp1, lp2):
    return InRange(pt[0], lp1[0], lp2[0]) and InRange(pt[1], lp1[1], lp2[1])

def IntersectLineLine(l1_p1, l1_p2, l2_p1, l2_p2):
    isect, xPt = IntersectEndlessLineLine(l1_p1, l1_p2, l2_p1, l2_p2)
    isect = isect and PtInRect(xPt, l1_p1, l1_p2) and PtInRect(xPt, l2_p1, l2_p2)
    return isect, xPt

def IntersectLineRec(p1, p2, rect):
    iL = [
        IntersectLineLine(p1, p2, rect.bottomleft, rect.bottomright),
        IntersectLineLine(p1, p2, rect.bottomright, rect.topright),
        IntersectLineLine(p1, p2, rect.topright, rect.topleft),
        IntersectLineLine(p1, p2, rect.topleft, rect.bottomleft) ]
    iDist = [(i[1], pygame.math.Vector2(i[1][0] - p1[0], i[1][1] - p1[1]).length()) for i in iL if i[0]]
    iDist.sort(key=lambda t: t[1])
    return iDist
           
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (x, y))
        self.prev_loc = None

    def collision(self, object_location):
        
        if not self.prev_loc:
            self.prev_loc = object_location
            return None 
        
        intersect = IntersectLineRec(self.prev_loc, object_location, self.rect)
        self.prev_loc = object_location

        if intersect:
            ip = [*intersect[0][0]]
            for i in range(2):
                tp = self.rect.center[i] if ip[i] == object_location[i] else object_location[i]
                ip[i] += -3 if ip[i] < tp else 3
            self.prev_loc = ip
            return intersect, ip
    
        return None

pygame.init()
window = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

obstacle = Obstacle(*window.get_rect().center, 30, 150)
all_sprites = pygame.sprite.Group()
all_sprites.add(obstacle)
count = 0
run = True
while run:
    clock.tick(60)
    mouse_move = (0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    
    intersect_information = obstacle.collision(pygame.mouse.get_pos())
    if intersect_information:
        intersect, new_location = intersect_information
        pygame.mouse.set_pos(new_location)
        count += 1
        print("hit:", count, -intersect[0][0][0], intersect[0][0][1])     
    
    window.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()