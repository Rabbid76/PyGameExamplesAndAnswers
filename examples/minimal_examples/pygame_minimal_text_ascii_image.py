# pygame.font module
# https://www.pygame.org/docs/ref/font.html
#
# How to display image and text at the same time in python (like SanctuaryRPG)?
# https://stackoverflow.com/questions/67711739/how-to-display-image-and-text-at-the-same-time-in-python-like-sanctuaryrpg/67712339#67712339
#
# GitHub - PyGameExamplesAndAnswers - Text and font
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_text_and_font.md
#
# https://replit.com/@Rabbid76/PyGame-AsciiTextImage

import pygame

img_text = r'''
                 __,__
        .--.  .-"     "-.  .--.
       / .. \/  .-. .-.  \/ .. \
      | |  '|  /   Y   \  |'  | |
      | \   \  \ 0 | 0 /  /   / |
       \ '- ,\.-"`` ``"-./, -' /
        `'-' /_   ^ ^   _\ '-'`
        .--'|  \._   _./  |'--. 
      /`    \   \ `~` /   /    `\
     /       '._ '---' _.'       \
    /           '~---~'   |       \
   /        _.             \       \
  /   .'-./`/        .'~'-.|\       \
 /   /    `\:       /      `\'.      \
/   |       ;      |         '.`;    /
\   \       ;      \           \/   /
 '.  \      ;       \       \   `  /
   '._'.     \       '.      |   ;/_
    /__>     '.       \_ _ _/   ,  '--.
   .'   '.   .-~~~~~-. /     |--'`~~-.  \
  // / .---'/  .-~~-._/ / / /---..__.'  /
 ((_(_/    /  /      (_(_(_(---.__    .'
           | |     _              `~~`
           | |     \'.
            \ '....' |
             '.,___.'
'''

def renderTextImage(surf, font, text, x, y, color):
    img_text = text.splitlines()
    for i, line in enumerate(img_text):
        text_surf = font.render(line, True, color)
        surf.blit(text_surf, (x, y + i * text_height))

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

text_height = 16 
font = pygame.font.SysFont("Courier", text_height)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.fill(0)
    renderTextImage(window, font, img_text, 50, 20, (255, 255, 0))
    pygame.display.flip()

pygame.quit()
exit()