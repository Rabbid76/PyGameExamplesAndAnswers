# Sometimes the ball doesn't bounce off the paddle in pong game
# https://stackoverflow.com/questions/62864205/sometimes-the-ball-doesnt-bounce-off-the-paddle-in-pong-game

"""
For a mor sophisticated solution you've to distinguish whether the ball hits an ege or a corner.

The collistion of a ball and an edge can be detected with

Whether the ball hits a corner can be detected by intersecting a ray from the corner in the opposite moving direction of the ball, with the ball

This hast detection has to be repeated for all 4 corners and edges, where the nearest collision has to be found.  
"""

import pygame
import math

Vec2 = pygame.math.Vector2

def vec2_norm_and_length(V):
    length = V.length()
    return (V / length if length > 0 else V), length

def intersect_edge(B0, B1, L0, L1, radius):
    LV, line_len = vec2_norm_and_length(Vec2(L1) - L0)
    LX = Vec2(L0) + LV * (Vec2(B0) - L0).dot(LV)
    LNV, n_dist = vec2_norm_and_length(Vec2(B0 - LX))
    if n_dist < radius:
        return None
    BD, b_dist = vec2_norm_and_length(Vec2(B1) - B0)
    dist = (n_dist - radius) / BD.dot(-LNV)
    X = Vec2(B0) + BD * dist
    rd = (Vec2(X) - L0).dot(LV)
    if rd < 0 or rd > line_len:
        return None
    return dist, X, LNV

def intersect_corner(B0, B1, P, radius):
    C = Vec2(B0)
    PC, pc_dist = vec2_norm_and_length(Vec2(C) - P)
    Ray, b_dist = vec2_norm_and_length(Vec2(B0) - B1)
    pc_dot_ray = PC.dot(Ray)
    if pc_dot_ray == 0:
        return None
    p_np_len = pc_dist / PC.dot(Ray)
    NP = Vec2(P) + Ray * p_np_len
    n_dist = (NP - C).length()
    if n_dist > radius:
        return None
    r_d = math.sqrt(radius*radius - n_dist*n_dist)
    if n_dist > r_d or r_d > p_np_len:
        return None
    dist = p_np_len - r_d
    X = C - Ray * dist
    return dist, X, (X - P).normalize()

def collide_rect(ball_rect, ball_move, paddle_rect):
    current_pos = ball_rect.center
    new_pos = Vec2(current_pos) + Vec2(ball_move) 
    paddle_pts = [paddle_rect.topleft, paddle_rect.topright, paddle_rect.bottomright, paddle_rect.bottomleft]
    nearest_intersect = None
    for i in range(len(paddle_pts)):
        
        intersect = intersect_edge(current_pos, new_pos, paddle_pts[i], paddle_pts[(i+1) % 4], ball_rect.width//2)
        if intersect and intersect[0] >= 0.0 and (not nearest_intersect or intersect[0] < nearest_intersect[0]):
            nearest_intersect = intersect

        intersect = intersect_corner(current_pos, new_pos, paddle_pts[i], ball_rect.width//2)
        if intersect and (not nearest_intersect or intersect[0] < nearest_intersect[0]):
            nearest_intersect = intersect

    BD, b_move = vec2_norm_and_length(Vec2(ball_move))
    if not nearest_intersect or nearest_intersect[0] > b_move:
        return None
    
    dist, X, NV = nearest_intersect
    RV = Vec2(BD).reflect(NV)

    ball_move = RV.x * b_move, RV.y * b_move
    ball_rect.centerx = round(X[0] + RV[0] * (b_move - dist))
    ball_rect.centery = round(X[1] + RV[1] * (b_move - dist))

    return ball_rect, ball_move

pygame.init()
window = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

radius = 20
move = 3, 3
#ball = pygame.Rect(window.get_width()//2-radius, window.get_height()//2-radius, radius*2, radius)
ball = pygame.Rect(window.get_width()//2+125, 20, radius*2, radius)
paddleHeight = 80
paddleLeft = pygame.Rect(20, (window.get_height()-paddleHeight)//2, 10, paddleHeight)
paddleRight = pygame.Rect(window.get_width()-30, (window.get_height()-paddleHeight)//2, 10, paddleHeight)

start = False

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: start = True

    keys = pygame.key.get_pressed()
    paddleLeft.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 5
    paddleRight.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    paddleLeft.clamp_ip(window.get_rect())
    paddleRight.clamp_ip(window.get_rect())

    if start:
        collide = None
        if move[0] > 0 and ball.centerx >= window.get_rect().centerx:
            collide = collide_rect(ball, move, paddleRight)  
        elif move[0] < 0 and ball.centerx < window.get_rect().centerx:
            collide = collide_rect(ball, move, paddleLeft)   
        if not collide:
            collide = collide_rect(ball, move, window.get_rect())
        if collide:
            ball, move = collide
        else:
            ball.x += move[0] 
            ball.y += move[1] 

    window.fill('black')
    pygame.draw.rect(window, (255, 255, 255), paddleLeft)
    pygame.draw.rect(window, (255, 255, 255), paddleRight)
    pygame.draw.circle(window, (255, 255, 255), ball.center, radius)
    pygame.display.flip()

pygame.quit()
exit()
