# line collision detector with circles
# https://stackoverflow.com/questions/74592905/line-collision-detector-with-circles/74593239#74593239
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Line and Circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md

import pygame, math

window = pygame.display.set_mode((500, 400))

l1 = [100, 100]
l2 = [400, 300]
l3 = [250, 250]
l4 = [210, 290]
r = 40

def sign(x):
    return -1 if x < 0 else 1

def interectLineCircle(l1, l2, cpt, r):
    x1 = l1[0] - cpt[0]
    y1 = l1[1] - cpt[1]
    x2 = l2[0] - cpt[0]
    y2 = l2[1] - cpt[1]
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx*dx + dy*dy)
    D = x1 * y2 - x2 * y1
    discriminant = r*r*dr*dr - D*D
    if discriminant < 0:
        return []
    if discriminant == 0:
        xa = (D * dy ) /  (dr * dr)
        ya = (-D * dx ) /  (dr * dr)
        ta = (xa-x1)*dx/dr + (ya-y1)*dy/dr
        return [(xa + cpt[0], ya + cpt[1])] if 0 < ta < dr else []
    
    xa = (D * dy + sign(dy) * dx * math.sqrt(discriminant)) / (dr * dr)
    ya = (-D * dx + abs(dy) * math.sqrt(discriminant)) / (dr * dr)
    ta = (xa-x1)*dx/dr + (ya-y1)*dy/dr
    xpt = [(xa + cpt[0], ya + cpt[1])] if 0 < ta < dr else []
    
    xb = (D * dy - sign(dy) * dx * math.sqrt(discriminant)) / (dr * dr) 
    yb = (-D * dx - abs(dy) * math.sqrt(discriminant)) / (dr * dr)
    tb = (xb-x1)*dx/dr + (yb-y1)*dy/dr
    xpt += [(xb + cpt[0], yb + cpt[1])] if 0 < tb < dr else []
    return xpt

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    cpt = pygame.mouse.get_pos()
    isect1 = interectLineCircle(l1, l2, cpt, r)
    isect2 = interectLineCircle(l3, l4, cpt, r)
    
    window.fill("black")
    pygame.draw.line(window, "white", l1, l2, 3)
    pygame.draw.line(window, "white", l3, l4, 3)
    pygame.draw.circle(window, "white", cpt, r, 3)
    for p in isect1 + isect2:
        pygame.draw.circle(window, "red", p, 5)
    pygame.display.flip()

pygame.quit()
exit()