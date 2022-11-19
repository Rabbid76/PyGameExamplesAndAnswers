# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# [Trying to code the Recaman Sequence, but issue with the parameters I pass for drawing an arc
# https://stackoverflow.com/questions/54384422/trying-to-code-the-recaman-sequence-but-issue-with-the-parameters-i-pass-for-dr/54386695#54386695  
#
# GitHub - PyGameExamplesAndAnswers - Recaman's sequence
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame 
import math

pygame.init()
window = pygame.display.set_mode((800, 600))

index, limit = 0, 102
sequence = [0]
for i in range(limit):
    index += -i if index-i > 0 and index-i not in sequence else i
    sequence.append(index)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))

    zx = window.get_width() / 100
    curX = 0
    for n in range(0, len(sequence)-1):
        
        d = 1 if n % 2 == 0 else -1
        s = 1 if sequence[n+1] > sequence[n] else -1
        
        dx = n * zx
        xi = curX
        curX += n * zx * s
        
        diameter = abs(dx)
        rect = pygame.Rect(min(xi, xi + s * dx), 0, diameter, diameter)
        rect.centery = window.get_height() // 2
        clip_rect = pygame.Rect(rect.left, rect.top if d > 0 else rect.centery, rect.width, diameter // 2)
        
        window.set_clip(clip_rect)
        pygame.draw.circle(window, (0, 0, 0), rect.center, diameter // 2, 1)
        
    window.set_clip(None)
    pygame.display.flip()
