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
            if self.rect.x >= 1270:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_LEFT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1270:
                self.reverse = 1
                 
        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        
class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rival.bmp').convert() #enable alpha transparency option  ##look up how to make bmp background transparent
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.radius = self.rect.height/2
        self.rect.x = 1100
        self.rect.y = 0
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
            if self.rect.x >= 1270:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1270:
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
                    if self.rect.x >= 1270:
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
        self.rect.x = 580
        self.rect.y = 300
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
            if self.rect.x >= 1270:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 1270:
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
                    if self.rect.x >= 1270:
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
        dist = randint(1,10)
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
            if self.rect.x >= 1270:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 1270:
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
                    if self.rect.x >= 1270:
                        self.reverse = -1
                    if self.rect.x <= 0:
                        self.reverse = 1
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 1270)
        randY = randint(0, 636)
        self.rect.center = (randX,randY)
        
class Bludger1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bludger.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 200
        self.reverse = 1
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,25)
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
            if self.rect.x >= 1270:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1270:
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
                    if self.rect.x >= 1270:
                        self.reverse = -1
                    if self.rect.x <= 0:
                        self.reverse = 1  
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 1270)
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
        self.rect.y = 400
        self.reverse = 1

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,25)
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
            if self.rect.x >= 1270:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1270:
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
                    if self.rect.x >= 1270:
                        self.reverse = 1  
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 1270)
        randY = randint(0, 636)
        self.rect.center = (randX,randY)
        

      
# set window size to match picture size
width = 1270
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
rival = Rival()
snitch = Snitch()
quaffle = Quaffle()
bludger1 = Bludger1()
bludger2 = Bludger2()

mouse.set_visible(False)

f = pygame.font.SysFont(None, 25)

hits = 0
comp = 0

clock = pygame.time.Clock()
crashed = False

pygame.mixer.music.load('HarryPotter.wav')
pygame.mixer.music.play(loops=-1)


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            

    if pygame.sprite.collide_rect(hp, quaffle):
        mixer.Sound("metal-clang.wav").play()
        hits += 10
        quaffle.move()
    
    if pygame.sprite.collide_circle(hp, snitch):
        hits += 150
        
        print ('The Quidditch game has ended')
        gameExit = True
        
    if pygame.sprite.collide_rect(hp, bludger1):
        mixer.Sound("crowd-groan.wav").play()
        hits -= 15
        bludger1.move()
        
    if pygame.sprite.collide_rect(hp, bludger2):
        mixer.Sound("crowd-groan.wav").play()
        hits -= 15
        bludger2.move()
            
    if pygame.sprite.collide_rect(rival, quaffle):
        comp += 10
        quaffle.move()
    
    if pygame.sprite.collide_rect(rival, snitch):
        comp += 150
        print ('The Quidditch game has ended')
        gameExit = True
        
    if pygame.sprite.collide_rect(rival, bludger1):
        comp -= 15
        bludger1.move()
        
    if pygame.sprite.collide_rect(rival, bludger2):
        comp -= 15
        bludger2.move()
    
     

    hp.handle_keys()
    rival.handle_keys()
    snitch.handle_keys() 
    quaffle.handle_keys()
    bludger1.handle_keys()
    bludger2.handle_keys()
    screen.blit(background,(0,0))
    hp.draw(screen)
    rival.draw(screen)
    snitch.draw(screen)
    quaffle.draw(screen)
    bludger1.draw(screen)
    bludger2.draw(screen)
    
    
    text = f.render("Your Score = " + str(hits), True, (0,0,0))
    screen.blit(text, (400, 0))
    text2 = f.render("Opponent's Score = " + str(comp), True, (0,0,0))
    screen.blit(text2, (700, 0))
    if gameExit == True:
        if hits > comp:
            text_win = f.render("The snitch has been caught and YOU WIN", True, (255,255,255))
            mixer.Sound("cheers.wav").play()
            screen.blit(text_win, (500, 300))
            pygame.display.update()
        elif comp > hits:
            text_lose = f.render("The snitch has been caught but YOU LOSE", True, (255,255,255))
            mixer.Sound("crowd-boo.wav").play()
            screen.blit(text_lose, (500, 300))
            pygame.display.update()
        elif comp == hits:
            text_tie = f.render ("This game has ended in a tie", True, (255,255,255))
            screen.blit(text_tie, (500, 300))
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
