
from sys import float_repr_style
from typing import Dict
from pygame import *
import pygame
from pygame.transform import rotozoom, scale
import Roulette, RouletteNumbers



SIZE = 1200,900  
WIN  = pygame.display.set_mode(SIZE)
FPS = 60 
WIN.fill("white")

bg = image.load("bg.jpg")
bg = scale(bg, (1200,900))





OriginalWheel = scale(pygame.image.load("wheel-modified.png").convert_alpha(), (300,300))
angle , x, incr = 3, 0, 5

def DisplayNumber():
    

def angleAlg():
        global x, angle, incr
        dictA = {0:5, 1:4, 2:3, 3:2, 4:1 ,5:0}
        if angle >= 720:
            incr = incr - 1
            angle = 0
        if incr == 0:
            DisplayNumber()
        angle = angle + incr
        return angle

def spin(image):
    global angle
        
    wheelRotated = rotozoom(image, -angleAlg() ,1).convert_alpha()
    wheelRect = wheelRotated.get_rect(center = (600,450))
    WIN.blit(bg, (0,0)) 
    WIN.blit(wheelRotated.convert_alpha(), wheelRect)
    pygame.display.update()




run = True

while run == True:
    clock = pygame.time.Clock()
    
    for event in pygame.event.get():
        clock.tick(FPS)
        if event.type == pygame.QUIT:
            print("Thanks for playing!")
            run = False
       

    spin(OriginalWheel)    
        
        
        
        
        
        
        
        
        
        
      
pygame.quit()
