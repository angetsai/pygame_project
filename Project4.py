print ("Project 4: Pygame")

import random
import sys
import pygame
import os
#from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *
pygame.init();


# set window size to match picture size
width = 1024
height = 768

# initialise pygame
pygame.init()
screen = pygame.display.set_mode((width,height),1,16)
#load picture
background= pygame.image.load('hogwarts.bmp')
#display picture
screen.blit(background,(0,0))
pygame.display.flip()






#create a surface
#gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Hogwarts")

#pygame.display.flip() 		#similar to a flip book, updates entire surface
#pygame.display.update()		#only updates portion specified


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    

    
  



#required
pygame.quit()
quit()	

