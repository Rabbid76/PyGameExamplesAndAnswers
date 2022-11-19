# Adding rects in list for displaying in 7-segment digits in pygame
# https://stackoverflow.com/questions/70684923/my-parabola-is-working-fine-alone-but-its-wrong-in-pygame/70685947#70685947  
#
# GitHub - PyGameExamplesAndAnswers - Miscellaneous - Collection
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_miscellaneous.md

import pygame
import numpy as np

class Parabola:
    def __init__(self, parabloe_type, *params):
        if parabloe_type == 0:
            self.__a = params[0]
            self.__b = params[1]
            self.__c = params[2]

        elif parabloe_type == 1:
            matrix_a = np.array([
                [params[0][0]**2, params[0][0], 1],
                [params[1][0]**2, params[1][0], 1],
                [params[2][0]**2, params[2][0], 1]
            ])
            matrix_b = np.array([params[0][1], params[1][1], params[2][1]])
            matrix_c = np.linalg.solve(matrix_a, matrix_b)
            self.__a = matrix_c[0]
            self.__b = matrix_c[1]
            self.__c = matrix_c[2]

    def claculateY(self, x):
        return self.__a * x ** 2 + self.__b * x + self.__c

    def pointsOnCurve(self, n, m, step=1):
        return [(x, self.claculateY(x)) for x in range(int(min(n, m)), int(max(n, m)) + 1, step)]

pygame.init()
window = pygame.display.set_mode((800, 600))
window_rect = window.get_rect()
pos0 = 100, window_rect.height - 100

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mx, my = pygame.mouse.get_pos()
    if abs(mx - pos0[0]) < 2:
        mx = mx-2 if mx < pos0[0] else mx + 2
    pts = [pos0, (mx, pos0[1]), ((mx + pos0[0]) // 2, my)]
    trajectory_parabola = Parabola(1, *pts)
    trajectory = [(pt[0], round(pt[1])) for pt in trajectory_parabola.pointsOnCurve(0, window_rect.width)]

    window.fill(0)
    pygame.draw.lines(window, (255, 255, 0), False, trajectory)
    for pt in pts:
        pygame.draw.circle(window, (255, 0, 0), pt, 10)
    pygame.display.flip()

pygame.quit()
exit()