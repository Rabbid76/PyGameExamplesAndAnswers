# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# How to make a character jump in Pygame?
# https://stackoverflow.com/questions/70591591/how-to-make-a-character-jump-in-pygame/70591592#70591592
# 
# Jump is triggered twice per click in Pygame
# https://stackoverflow.com/questions/66253320/jump-is-triggered-twice-per-click-in-pygame/66254270#66254270
# 
# python, pygame - jumping too fast?
# https://stackoverflow.com/questions/58474204/python-pygame-jumping-too-fast/58474280#58474280
#
# How does this algorithm make the character jump in pygame?
# https://stackoverflow.com/questions/65873880/how-does-this-algorithm-make-the-character-jump-in-pygame/65874132#65874132
#
# How To Make Object Jump Forward In Pygame?
# https://stackoverflow.com/questions/66051418/how-to-make-object-jump-forward-in-pygame/66051478#66051478
#  
# GitHub - PyGameExamplesAndAnswers - Jump
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_jump.md
#
# https://replit.com/@Rabbid76/PyGame-Jump#main.py

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

rect = pygame.Rect(135, 220, 30, 30) 
vel = 5
jump = False
jumpCount = 0
jumpMax = 15

run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax

    keys = pygame.key.get_pressed()    
    rect.centerx = (rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel) % 300
    
    if jump:
        rect.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False 

    window.fill((0, 0, 64))
    pygame.draw.rect(window, (64, 64, 64), (0, 250, 300, 100))
    pygame.draw.circle(window, (255, 0, 0), rect.center, 15)
    pygame.display.flip()

pygame.quit()
exit() 