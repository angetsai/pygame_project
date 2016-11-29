print ("Project 4: Pygame")

import random
import sys
import pygame
import os
#from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *



class HarryPotter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('harrypotter.bmp').convert_alpha() #enable alpha transparency option  ##look up how to make bmp background transparent
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# set window size to match picture size
width = 774
height = 581

# initialise pygame
pygame.init()
#create a surface
screen = pygame.display.set_mode((width,height),1,16) #initialize with a tuple
#lets add a title, aka "caption"
pygame.display.set_caption("Hogwarts")
#load picture
background= pygame.image.load('hogwarts.bmp')
hp = HarryPotter()
#sprite= pygame.image.load('HarryPotter.bmp')

clock = pygame.time.Clock()
crashed = False



gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    hp.handle_keys()
#display picture
    screen.blit(background,(0,0))
    hp.draw(screen)
    pygame.display.flip()

    clock.tick(120)

#pygame.display.flip() 		#similar to a flip book, updates entire surface
#pygame.display.update()		#only updates portion specified


#required
pygame.quit()
quit()	

