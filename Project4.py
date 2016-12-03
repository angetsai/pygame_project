print ("Project 4: Pygame")

import sys
import pygame
import os
from pygame.locals import *
from pygame import *
from pygame.sprite import *
from random import *


class HarryPotter(pygame.sprite.Sprite):                                                         # implement class inheritance
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('harrypotter.bmp').convert()         
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)                                                 # make the background transparent
        self.rect = self.image.get_rect()
        self.radius = self.rect.height/2
        self.rect.x = 0                                                                          # determine's sprite's starting coordinates
        self.rect.y = 0
        self.reverse = 1
        
    def handle_keys(self):                                                                       # function to control movement with keys
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]:
            self.rect.y += dist*self.reverse                        
            if self.rect.y >= 625:                                                               # wall detection; if go out of bounds, will 'bounce back'
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        elif key[pygame.K_UP]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 625:
                self.reverse = 1
        if key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 1250:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_LEFT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1250:
                self.reverse = 1
                         
    def draw(self, surface):                                                                    # function to draw the sprite on surface
        surface.blit(self.image, (self.rect.x, self.rect.y))                                     
        
        
class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rival.bmp').convert() 
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.radius = self.rect.height/2
        self.rect.x = 1100
        self.rect.y = 0
        self.reverse = 1

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,30)                                                                     # sprite moves a random distance between 1 and 30 pixels each time
        if key[pygame.K_UP]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 625:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 625:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x += dist*self.reverse                                                     
            if self.rect.x >= 1250:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1250:
                self.reverse = 1
                
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:                       # controls for movement even if user doesn't press down a key
                    self.rect.y += dist*self.reverse
                    if self.rect.y >= 625:
                        self.reverse = -1
                    if self.rect.y <= 0:
                        self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x -= dist*self.reverse
                    if self.rect.x <= 0:
                        self.reverse = -1
                    if self.rect.x >= 1250:
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
        self.radius = self.rect.height/2                                                         # setting radius for snitch so hp will be able to detect its center
        self.rect.x = 580
        self.rect.y = 300
        self.reverse = 1
         
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = randint(1,15)
        if key[pygame.K_UP]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 625:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 625:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1250:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 1250:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y += dist*self.reverse
                    if self.rect.y >= 625:
                        self.reverse = -1
                    if self.rect.y <= 0:
                        self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x -= dist*self.reverse
                    if self.rect.x <= 0:
                        self.reverse = -1
                    if self.rect.x >= 1250:
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
        dist = randint(1,15)
        if key[pygame.K_UP]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 625:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y += dist*self.reverse
            if self.rect.y >= 625:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1250:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 1250:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y -= dist*self.reverse
                    if self.rect.y <= 0:
                        self.reverse = -1
                    if self.rect.y >= 625:
                        self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x += dist*self.reverse
                    if self.rect.x >= 1250:
                        self.reverse = -1
                    if self.rect.x <= 0:
                        self.reverse = 1
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):                                                                              # function for random movement -- jumps to next random coordinate
        randX = randint(0, 1250)
        randY = randint(0, 625)
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
            if self.rect.y >= 625:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 625:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 1250:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1250:
                self.reverse = 1
                
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y -= dist*self.reverse
                if self.rect.y <= 0:
                    self.reverse = -1
                if self.rect.y >= 625:
                    self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x += dist*self.reverse
                    if self.rect.x >= 1250:
                        self.reverse = -1
                    if self.rect.x <= 0:
                        self.reverse = 1  
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 1250)
        randY = randint(0, 625)
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
            if self.rect.y >= 625:
                self.reverse = -1
            if self.rect.y <= 0:
                self.reverse = 1
        elif key[pygame.K_DOWN]:
            self.rect.y -= dist*self.reverse
            if self.rect.y <= 0:
                self.reverse = -1
            if self.rect.y >= 625:
                self.reverse = 1
        if key[pygame.K_LEFT]:
            self.rect.x += dist*self.reverse
            if self.rect.x >= 1250:
                self.reverse = -1
            if self.rect.x <= 0:
                self.reverse = 1
        elif key[pygame.K_RIGHT]:
            self.rect.x -= dist*self.reverse
            if self.rect.x <= 0:
                self.reverse = -1
            if self.rect.x >= 1250:
                self.reverse = 1
                
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.rect.y += dist*self.reverse
                    if self.rect.y >= 625:
                        self.reverse = -1
                    if self.rect.y <= 0:
                        self.reverse = 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.rect.x -= dist*self.reverse
                    if self.rect.x <= 0:
                        self.reverse = -1
                    if self.rect.x >= 1250:
                        self.reverse = 1  
            
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        randX = randint(0, 1250)
        randY = randint(0, 625)
        self.rect.center = (randX,randY)
        
      
width = 1270                                                # set window size to match picture size
height = 636

pygame.init()                                               # initialise pygame
screen = pygame.display.set_mode((width,height),1,16)       # create a surface, initialize with a tuple
pygame.display.set_caption("Hogwarts")                      # add a title, aka "caption"
background= pygame.image.load('hogwarts.bmp')               # load picture for background
hp = HarryPotter()                                          # create instance of each class
rival = Rival()
snitch = Snitch()
quaffle = Quaffle()
bludger1 = Bludger1()
bludger2 = Bludger2()

mouse.set_visible(False)                                    # mouse won't be visible on screen anymore

f = pygame.font.SysFont(None, 25)                           # setting font and size

hits = 0                                                    # initializing scores
comp = 0

pygame.mixer.music.load('HarryPotter.wav')                  
pygame.mixer.music.play(loops=-1)                           # music will loop until game ends


gameExit = False
while not gameExit:                                         # as long as the game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            

    if pygame.sprite.collide_rect(hp, quaffle):             # collision with quaffle results in points (as determined by game of quidditch)
        mixer.Sound("metal-clang.wav").play()               # sound effects to accompany each collision
        hits += 10
        quaffle.move()                                      # sprite will move to random location after hitting once
    
    if pygame.sprite.collide_circle(hp, snitch):
        hits += 150
        
        print ('The Quidditch game has ended')              # prints in command terminal for user
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
    

    hp.handle_keys()                                        # calling function for each of the sprites to move
    rival.handle_keys()
    snitch.handle_keys() 
    quaffle.handle_keys()
    bludger1.handle_keys()
    bludger2.handle_keys()
    screen.blit(background,(0,0))
    hp.draw(screen)                                         # draw each of the sprites onto the screen
    rival.draw(screen)
    snitch.draw(screen)
    quaffle.draw(screen)
    bludger1.draw(screen)
    bludger2.draw(screen)
    
    
    text = f.render("Your Score = " + str(hits), True, (0,0,0))                                     # blits score and opponent's score at the top 
    screen.blit(text, (400, 0))                                                                     # of the page and keeps track
    text2 = f.render("Opponent's Score = " + str(comp), True, (0,0,0))
    screen.blit(text2, (700, 0))
    if gameExit == True:                                                                            # in the case that the snitch is caught and game is going to end
        if hits > comp:
            text_win = f.render("The snitch has been caught and YOU WIN", True, (255,255,255))      # follows game rules to determine winner
            mixer.Sound("cheers.wav").play()
            screen.blit(text_win, (475, 300))
            pygame.display.update()
        elif comp > hits:
            text_lose = f.render("The snitch has been caught but YOU LOSE", True, (255,255,255))
            mixer.Sound("crowd-boo.wav").play()
            screen.blit(text_lose, (475, 300))
            pygame.display.update()
        elif comp == hits:
            text_tie = f.render ("This game has ended in a tie", True, (255,255,255))
            screen.blit(text_tie, (475, 300))
            pygame.display.update()
        pygame.time.delay(3000)                                                                     # delays 3 seconds before exiting while loop
        break
        
    
    pygame.display.flip()                                                                           # updates entire surface
    pygame.display.update()                                                                         # updates portion specified


pygame.quit()                                                                                       # quits game
quit()	
