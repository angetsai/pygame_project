print ("Project 4: Pygame")

import random
import sys
import pygame
import os
#from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *
from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000;

class HarryPotter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('harrypotter.bmp').convert() #enable alpha transparency option  ##look up how to make bmp background transparent
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
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
        
    def hit(self, target):
        return self.rect.colliderect(target)


class Snitch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snitch.bmp')
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.x = 600
        self.y = 0
        
          #random movement // design object to move 1 pixel per each instance in while loop 
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 15
        if key[pygame.K_UP]:
            self.y += dist
        elif key[pygame.K_DOWN]:
            self.y -= dist
        if key[pygame.K_LEFT]:
            self.x += dist
        elif key[pygame.K_RIGHT]:
            self.x -= dist
            
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)
      
# set window size to match picture size
width = 847
height = 636

# initialise pygame
pygame.init()
#create a surface
screen = pygame.display.set_mode((width,height),1,16) #initialize with a tuple
#lets add a title, aka "caption"
pygame.display.set_caption("Hogwarts")
#load picture
background= pygame.image.load('hogwarts.bmp')
hp = HarryPotter()
snitch = Snitch()
#sprite= pygame.image.load('HarryPotter.bmp')

#quidditch = pygame.sprite.Renderplain(())
mouse.set_visible(False)

f = pygame.font.SysFont(None, 25)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

clock = pygame.time.Clock()
crashed = False

pygame.mixer.music.load('HarryPotter.wav')
pygame.mixer.music.play(loops=0)

#pygame.mixer.music.stop()



gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            
        elif event.type == MOUSEBUTTONDOWN:
            if hp.hit(snitch):
            #mixer.Sound("cha-ching.wav").play()
                snitch.move()
                hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
        elif event.type == USEREVENT + 1: # TIME has passed
            snitch.move()
           

    hp.handle_keys()
    snitch.handle_keys()
#display picture
    screen.blit(background,(0,0))
    hp.draw(screen)
    snitch.draw(screen)
    
    text = f.render("Score = " + str(hits), True, (0,0,0))
    screen.blit(text, (320, 0))
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(120)

#pygame.display.flip() 		#similar to a flip book, updates entire surface
#pygame.display.update()		#only updates portion specified


#required
pygame.quit()
quit()	

