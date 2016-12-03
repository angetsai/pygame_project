print ("Project 4: Pygame")

import sys
import pygame
import os
#from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *
from pygame import *
from pygame.sprite import *
from random import *


class HarryPotter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('harrypotter.bmp').convert() #enable alpha transparency option  ##look up how to make bmp background transparent
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.radius = self.rect.height/2
        self.rect.x = 0
        self.rect.y = 0
        self.reverse = 1
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 636:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        elif key[pygame.K_UP]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 636:
                self.reverse = 1
        if key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 636:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_LEFT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 847:
                self.reverse = 1
                 
        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        


class Snitch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snitch.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.radius = self.rect.height/2
        self.rect.x = 700
        self.rect.y = 500
        self.reverse = 1
        
          #random movement // design object to move 1 pixel per each instance in while loop 
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,15)
        if key[pygame.K_UP]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 636:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 636:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 847:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 636:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y += dist*self.reverse
                    if self.rect.y >= 636:
                        self.reverse = -1
                    if self.rect.y <= 0:
                        self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x -= dist*self.reverse
                    if self.rect.x <= 0:
                        self.reverse = -1
                    if self.rect.x >= 847:
                        self.reverse = 1
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    
        
        
class Quaffle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('quaffle.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 500
        self.reverse = 1
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,7)
        if key[pygame.K_UP]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 636:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 636:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 847:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 636:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y -= dist*self.reverse
                    if self.rect.y <= 0:
                        self.reverse = -1
                    if self.rect.y >= 636:
                        self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x += dist*self.reverse
                    if self.rect.x >= 636:
                        self.reverse = -1
                    if self.rect.x <= 0:
                        self.reverse = 1
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 847)
        randY = randint(0, 636)
        self.rect.center = (randX,randY)
        
class Bludger1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bludger.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 280
        self.reverse = 1
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,30)
        if key[pygame.K_UP]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 636:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 636:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 636:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 847:
                self.reverse = 1
                
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y -= dist*self.reverse
                if self.rect.y <= 0:
                    self.reverse = -1
                if self.rect.y >= 636:
                    self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x += dist*self.reverse
                    if self.rect.x >= 636:
                        self.reverse = -1
                    if self.rect.x <= 0:
                        self.reverse = 1  
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 847)
        randY = randint(0, 636)
        self.rect.center = (randX,randY)
        
class Bludger2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bludger.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 20
        self.reverse = 1

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,30)
        if key[pygame.K_UP]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 636:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 636:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 636:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 847:
                self.reverse = 1
                
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y += dist*self.reverse
                    if self.rect.y >= 636:
                        self.reverse = -1
                    if self.rect.y <= 0:
                        self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x -= dist*self.reverse
                    if self.rect.x <= 0:
                        self.reverse = -1
                    if self.rect.x >= 847:
                        self.reverse = 1  
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 847)
        randY = randint(0, 636)
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
quaffle = Quaffle()
bludger1 = Bludger1()
bludger2 = Bludger2()

mouse.set_visible(False)

f = pygame.font.SysFont(None, 25)

hits = 0

clock = pygame.time.Clock()
crashed = False

pygame.mixer.music.load('HarryPotter.wav')
pygame.mixer.music.play(loops=-1)


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            
        #movement for harry    
        
        #elif event.type == pygame.KEYDOWN:
        #    dist = 10
        #    if event.key == pygame.K_UP:
        #        hp.rect.y -= dist
        #    if event.key == pygame.K_DOWN:
        #        hp.rect.y += dist
        #    if event.key == pygame.K_RIGHT:
        #        hp.rect.x += dist
        #    if event.key == pygame.K_LEFT:
        #        hp.rect.x -= dist
                
        #    elif event.type == pygame.KEYUP:
        #        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #            hp.rect.y = 0
        #        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
        #            hp.rect.x = 0
                    
            # movement of snitch
        #    dist = randint(1,15)
        #    if event.key == pygame.K_UP:
        #        snitch.rect.y -= dist
        #    if event.key == pygame.K_DOWN:
        #        snitch.rect.y += dist
        #    if event.key == pygame.K_RIGHT:
        #        snitch.rect.x += dist
        #    if event.key == pygame.K_LEFT:
        #        snitch.rect.x -= dist
                
        #    elif event.type == pygame.KEYUP:
        #        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #            snitch.rect.y += dist
        #        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
        #            snitch.rect.x -= dist 
                    
            # movement of quaffle
        #    dist = randint(1,7)
        #    if event.key == pygame.K_UP:
        #        quaffle.rect.y += dist
        #    if event.key == pygame.K_DOWN:
        #        quaffle.rect.y -= dist
        #    if event.key == pygame.K_RIGHT:
        #        quaffle.rect.x -= dist
        #    if event.key == pygame.K_LEFT:
        #        quaffle.rect.x += dist
                
        #    elif event.type == pygame.KEYUP:
        #        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #            quaffle.rect.y -= dist
        #        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
        #            quaffle.rect.x += dist   
    
            # movement of bludger1    
        #    dist = randint(1,30)
        #    if event.key == pygame.K_UP:
        #        bludger1.rect.y -= dist
        #    if event.key == pygame.K_DOWN:
        #        bludger1.rect.y += dist
        #    if event.key == pygame.K_RIGHT:
        #        bludger1.rect.x += dist
        #    if event.key == pygame.K_LEFT:
        #        bludger1.rect.x -= dist
                
        #    elif event.type == pygame.KEYUP:
        #        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #            bludger1.rect.y -= dist
        #        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
        #            bludger1.rect.x += dist  
        
            # movement of bludger2
        #    dist = randint(1,30)
        #    if event.key == pygame.K_UP:
        #        bludger2.rect.y -= dist
        #    if event.key == pygame.K_DOWN:
        #        bludger2.rect.y += dist
        #    if event.key == pygame.K_RIGHT:
        #        bludger2.rect.x += dist
        #    if event.key == pygame.K_LEFT:
        #        bludger2.rect.x -= dist
                
        #    elif event.type == pygame.KEYUP:
        #        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #            bludger2.rect.y += dist
        #        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
        #            bludger2.rect.x -= dist  
            
            
            #hp.handle_keys()
            #snitch.handle_keys()
            #quaffle.handle_keys()
            #bludger1.handle_keys()
            #bludger2.handle_keys()
    if pygame.sprite.collide_rect(hp, quaffle):
        #mixer.Sound("c.wav").play()
        hits += 10
        quaffle.move()
    
    if pygame.sprite.collide_circle(hp, snitch):
        hits += 150
        
        print ('You won the Quidditch game')
        gameExit = True
        
    if pygame.sprite.collide_rect(hp, bludger1):
        mixer.Sound("crowd-groan.wav").play()
        hits -= 15
        bludger1.move()
        
    if pygame.sprite.collide_rect(hp, bludger2):
        mixer.Sound("crowd-groan.wav").play()
        hits -= 15
        bludger2.move()
            
    
     

    hp.handle_keys()
    snitch.handle_keys() # have these again to make movement more smooth
    quaffle.handle_keys()
    bludger1.handle_keys()
    bludger2.handle_keys()
    screen.blit(background,(0,0))
    hp.draw(screen)
    snitch.draw(screen)
    quaffle.draw(screen)
    bludger1.draw(screen)
    bludger2.draw(screen)
    
    
    text = f.render("Score = " + str(hits), True, (0,0,0))
    screen.blit(text, (380, 0))
    if gameExit == True:
        text_end = f.render("You caught the snitch! YOU WIN", True, (255,255,255))
        mixer.Sound("cheers.wav").play()
        screen.blit(text_end, (350, 300))
        pygame.display.update()
        pygame.time.delay(3000)
        break
        
    
    pygame.display.flip()
    pygame.display.update()

 

#pygame.display.flip() 		#similar to a flip book, updates entire surface
#pygame.display.update()		#only updates portion specified


#required
pygame.quit()
quit()	
