# How to make parallax scrolling work properly with a camera that stops at edges pygame
# https://stackoverflow.com/questions/63712333/how-to-make-parallax-scrolling-work-properly-with-a-camera-that-stops-at-edges-p/74002486#74002486
#
# GitHub - PyGameExamplesAndAnswers - Background - Parallax
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_background.md

import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

tree1_image = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.rect(tree1_image, (64, 32, 0), (45, 75, 10, 25))
pygame.draw.polygon(tree1_image, (16, 64, 0), [(50, 0), (70, 35), (65, 35), (90, 75), (10, 75), (35, 35), (30, 35)])
tree2_image = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.rect(tree2_image, (128, 64, 16), (45, 75, 10, 25))
pygame.draw.polygon(tree2_image, (64, 128, 0), [(50, 0), (70, 35), (65, 35), (90, 75), (10, 75), (35, 35), (30, 35)])
tree2_image = pygame.transform.smoothscale(tree2_image, (75, 75))
tree3_image = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.rect(tree3_image, (164, 128, 96), (45, 75, 10, 25))
pygame.draw.polygon(tree3_image, (128, 164, 64), [(50, 0), (70, 35), (65, 35), (90, 75), (10, 75), (35, 35), (30, 35)])
tree3_image = pygame.transform.smoothscale(tree3_image, (50, 50))

bg_layer_1_image = pygame.Surface((600, 100), pygame.SRCALPHA)
for i in range(6):
    bg_layer_1_image.blit(tree1_image, (i*100, 0))
bg_layer_2_image = pygame.Surface((600, 75), pygame.SRCALPHA)
for i in range(8):
    bg_layer_2_image.blit(tree2_image, (i*75, 0))  
bg_layer_3_image = pygame.Surface((600, 50), pygame.SRCALPHA)
for i in range(12):
    bg_layer_3_image.blit(tree3_image, (i*50, 0))    
bg_layer_1_x = 0
bg_layer_2_x = 0
bg_layer_3_x = 0
move_x = 1

def draw_background(surf, bg_image, bg_x, bg_y):
    surf.blit(bg_image, (bg_x - surf.get_width(), bg_y))
    surf.blit(bg_image, (bg_x, bg_y))

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    bg_layer_1_x = (bg_layer_1_x - move_x) % 600
    bg_layer_2_x = (bg_layer_2_x - move_x*0.75) % 600
    bg_layer_3_x = (bg_layer_3_x - move_x*0.5) % 600

    window.fill((192, 192, 255))
    pygame.draw.rect(window, (64, 128, 64), (0, 250, 600, 150))
    pygame.draw.rect(window, (128, 164, 192), (0, 170, 600, 80))
    draw_background(window, bg_layer_3_image, bg_layer_3_x, 120)
    draw_background(window, bg_layer_2_image, bg_layer_2_x, 135)
    draw_background(window, bg_layer_1_image, bg_layer_1_x, 150)
    pygame.display.flip()

pygame.quit()
exit()