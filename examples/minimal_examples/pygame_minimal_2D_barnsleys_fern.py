# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Barnsley fern
# https://en.wikipedia.org/wiki/Barnsley_fern
#
# Having issues trying to use a dictionary to define parameters for Barnsley's Fern
# https://stackoverflow.com/questions/56913062/having-issues-trying-to-use-a-dictionary-to-define-parameters-for-barnsleys-fer
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Fractal
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md
#
# https://replit.com/@Rabbid76/PyGame-BarnsleysFern

import pygame  
import random   
pygame.init()  

def general_algorithm(a,b,c,d,e,f,x,y):  
    return a*x + b*y + e, c*x + d*y + f    

def generate_next_point(x, y, constants):  
    randompercentage = random.randint(0, 100)  
    for n in constants['p']:  
        if randompercentage <= n:  
            i = constants['p'].index(n)  
            break  
    return general_algorithm(constants['a'][i],constants['b'][i],constants['c'][i],constants['d'][i],constants['e'][i],constants['f'][i],x,y)

def draw_point(surface, color, fern_x, fern_y, margin): 
    width, height = surface.get_size() 
    cartesian_x = int((fern_x+2.1820+margin) * (width /(2.1820+2.6558+2*margin)))  
    cartesian_y = int((fern_y*-1+9.9983+margin) * (height/(9.9983+2*margin))) 
    if 0 <= cartesian_x <= width and 0 <= cartesian_y <= height: 
        surface.set_at((cartesian_x, cartesian_y), color)   

fern_paramters = {  
    'a':[0   ,0.85 ,0.2  ,-0.15],  
    'b':[0   ,0.04 ,-0.26,0.28 ],  
    'c':[0   ,-0.04,0.23 ,0.26 ],  
    'd':[0.16,0.85 ,0.22 ,0.24 ],  
    'e':[0   ,0    ,0    ,0    ],  
    'f':[0   ,1.6  ,1.6  ,0.44 ],  
    'p':[1   ,86   ,93   ,100  ]  
}  
fern_x, fern_y, margin = 0, 0, 0.5  

window = pygame.display.set_mode((400, 400))  
window.fill((60, 30, 10))  

pygame.time.wait(5000)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    fern_x, fern_y = generate_next_point(fern_x, fern_y, fern_paramters)
    draw_point(window, (64, 255, 128), fern_x, fern_y, margin)
    pygame.display.flip() 

pygame.quit()
exit()