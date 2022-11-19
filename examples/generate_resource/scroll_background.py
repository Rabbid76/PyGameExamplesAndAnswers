import pygame

pygame.init()
window = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)
text1 = font.render("1", True, "red")
text2 = font.render("2", True, "red")
textScreen = font.render("Screen", True, "red")

tree1_image = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.rect(tree1_image, (64, 32, 0), (45, 75, 10, 25))
pygame.draw.polygon(tree1_image, (16, 64, 0), [(50, 0), (70, 35), (65, 35), (90, 75), (10, 75), (35, 35), (30, 35)])

bg_layer_1_image = pygame.Surface((300, 200))
bg_layer_1_image.fill((128, 192, 255))
pygame.draw.rect(bg_layer_1_image, (64, 164, 64), (0, 150, 300, 50))
for i in range(3):
    bg_layer_1_image.blit(tree1_image, (i*100, 50))
bg_layer_1_image = pygame.transform.smoothscale(bg_layer_1_image, (150, 100))

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    bg_rect1 = bg_layer_1_image.get_rect(topleft = (25, 50))
    bg_rect2 = bg_layer_1_image.get_rect(topleft = (175, 50))

    window.fill((255, 255, 255))
    window.blit(bg_layer_1_image, bg_rect1)
    window.blit(bg_layer_1_image, bg_rect2)
    pygame.draw.rect(window, "black", bg_rect1, 3)
    pygame.draw.rect(window, "black", bg_rect2, 3)
    pygame.draw.rect(window, "red", (123, 48, 154, 104), 5)
    window.blit(textScreen, textScreen.get_rect(midbottom = (200, 46)))
    window.blit(text1, text1.get_rect(center = (150, 100)))
    window.blit(text2, text2.get_rect(center = (250, 100)))
    pygame.display.flip()

pygame.quit()
exit()
