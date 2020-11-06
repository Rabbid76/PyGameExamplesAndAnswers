# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Shooting a bullet in pygame in the direction of mouse
# https://stackoverflow.com/questions/60464828/calculating-direction-of-the-player-to-shoot-pygame
#
# GitHub - PyGameExamplesAndAnswers - Move towards target - Move towards target Shoot a bullet in a certain direction - Rotate player and shoot bullet towards faced direction
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_move_towards_target.md

import math
import pygame
 
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super().__init__() 
        self.image = player
        self.is_shooting = False
        self.original_player_image = player
        self.rect = self.original_player_image.get_rect(center = (x, y))
        self.angle = 0
 
    def rotate_to(self, to_x, to_y):
        rel_x, rel_y = to_x - self.rect.x, to_y - self.rect.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        self.image = pygame.transform.rotate(self.original_player_image, round(self.angle))
        self.rect = self.image.get_rect(center = self.rect.center)
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect(center = (x, y))
        self.hit = False
    
    def update(self):
         color = (255, 128, 0) if self.hit else (0, 255, 0)
         pygame.draw.circle(self.image, color, (15, 15), 15)

class Laser(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__() 
        self.original_image = pygame.Surface((5, 150))
        self.original_image.set_colorkey((0, 0, 0))
        self.original_image.fill((255, 0, 0))
        self.copy_image = self.original_image.copy()
        self.copy_image.set_colorkey((0, 0, 0))
        self.rect = self.copy_image.get_rect(center = (start_x, start_y - 75))
        self.image = pygame.Surface((5, 150))
 
    def rotate(self, anker_rect, angle):

        # get rectangle of player and laser, as if the angle would be 0 
        laser_rect  = self.original_image.get_rect(midbottom = anker_rect.midtop)
        pos         = anker_rect.center
        pivotPos    = [pos[0] - laser_rect.x, pos[1] - laser_rect.y]   

        # calcaulate the axis aligned bounding box of the rotated image
        w, h       = self.original_image.get_size()
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot 
        pivot        = pygame.math.Vector2(pivotPos[0], -pivotPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move   = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (pos[0] - pivot[0] + min_box[0] - pivot_move[0], pos[1] + pivot[1] - max_box[1] + pivot_move[1])

        # get a rotated image
        self.image = pygame.transform.rotate(self.original_image, angle)

        # get new rectangle
        self.rect = self.image.get_rect(topleft = (round(origin[0]), round(origin[1])))

def collideLineLine(l1_p1, l1_p2, l2_p1, l2_p2):
    
    # normaliced direction of the line and start of the line
    P  = pygame.math.Vector2(*l1_p1)
    line1_vec = pygame.math.Vector2(*l1_p2) - P
    R = line1_vec.normalize()
    Q  = pygame.math.Vector2(*l2_p1)
    line2_vec = pygame.math.Vector2(*l2_p2) - Q
    S = line2_vec.normalize()

    # normal vectors to the lines
    RNV = pygame.math.Vector2(R[1], -R[0])
    SNV = pygame.math.Vector2(S[1], -S[0])

    # distance to the intersection point
    QP  = Q - P
    t = QP.dot(SNV) / R.dot(SNV)
    u = QP.dot(RNV) / R.dot(SNV)

    return t > 0 and u > 0 and t*t < line1_vec.magnitude_squared() and u*u < line2_vec.magnitude_squared()

def colideRectLine(rect, p1, p2):
    return (collideLineLine(p1, p2, rect.topleft, rect.bottomleft) or
            collideLineLine(p1, p2, rect.bottomleft, rect.bottomright) or
            collideLineLine(p1, p2, rect.bottomright, rect.topright) or
            collideLineLine(p1, p2, rect.topright, rect.topleft))
 
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

player_image = pygame.Surface((30, 30), pygame.SRCALPHA)
player_image.fill((0, 0, 0, 0))
pygame.draw.circle(player_image, (128, 128, 255), (15, 15), 15)
pygame.draw.line(player_image, (0, 0, 0), (15,0), (15,30))
original_player_image = pygame.Surface((30, 30), pygame.SRCALPHA)
original_player_image.fill((128, 128, 255))

player = Player(window.get_width() // 2, window.get_height() - 100, player_image)
laser = Laser(player.rect.centerx + player_image.get_width() // 2, player.rect.centery - 75)
enemy = Enemy(window.get_width() // 2, 200)
group = pygame.sprite.Group([player, laser, enemy])

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    player.rect.x += (keys[pygame.K_d] - keys[pygame.K_a]) * 10
    player.rect.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 10
    player.rect.clamp_ip(window.get_rect())
    
    player.rotate_to(*pygame.mouse.get_pos())
    laser.rotate(player.original_player_image.get_rect(center = player.rect.center), player.angle)
    
    angle = player.angle + 360 if player.angle < 0 else player.angle 
    if angle < 90 or (angle > 180 and angle < 270):
        laserline = [laser.rect.topleft, laser.rect.bottomright]
    else:
        laserline = [laser.rect.bottomleft, laser.rect.topright]
    enemy.hit = colideRectLine(enemy.rect, *laserline)
    enemy.update()

    window.fill((127, 127, 127))
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()