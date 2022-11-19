# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Pygame: Frame ghosting?
# https://stackoverflow.com/questions/20862695/pygame-frame-ghosting/73964785#73964785 
#
# GitHub - PyGameExamplesAndAnswers - Blending and transparency - Transparency
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md

import pygame, math

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

image1 = pygame.Surface((400, 400))
image1.fill("white")
pygame.draw.circle(image1, "black", (200, 100), 50, 5)
image2 = pygame.Surface((400, 400))
image2.fill("white")
pygame.draw.line(image2, "black", (200, 150), (200, 230), 5)
pygame.draw.line(image2, "black", (200, 180), (120, 140), 5)
pygame.draw.line(image2, "black", (200, 180), (280, 140), 5)
pygame.draw.line(image2, "black", (200, 230), (170, 300), 5)
pygame.draw.line(image2, "black", (200, 230), (230, 300), 5)
image3 = pygame.Surface((400, 400))
image3.fill("white")
pygame.draw.circle(image3, "black", (180, 85), 10, 5)
pygame.draw.circle(image3, "black", (220, 85), 10, 5)
pygame.draw.line(image3, "black", (200, 95), (200, 115), 5)
pygame.draw.arc(image3, "black", (180, 100, 40, 30), math.pi, 0, 5)

images = [image1, image2, image3]
for image in images:
    image.set_colorkey("white")
    image.set_alpha(10)

window.fill("white")
count = 0
run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    index = count // 26
    count += 1
    if index < len(images):
        if count % 26 == 25:
            images[index].set_alpha(255)
        window.blit(images[index], (0, 0))
    pygame.display.flip()

pygame.quit()
exit()