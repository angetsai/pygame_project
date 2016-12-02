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

quidditch = pygame.sprite.Group()

class HarryPotter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('harrypotter.bmp').convert() #make background transparent
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
        
    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
    
    #def move(self):
     #   randX = randint(0, 600)
      #  randY = randint(0, 400)
       # self.rect.center = (randX,randY)
        
        
    #def moveme(self,x,y):
     #   if self.rect.left + x < 0:
      #      self.rect.left = 0
       # elif self.rect.right + x > 847:
        #    self.rect.right = 847
        #elif self.rect.top + y < 0:
         #   self.rect.top = 0
        #elif self.rect.bottom + y > 636:
         #   self.rect.bottom = 636
        #else:
         #   self.rect.move_ip((x,y))


class Snitch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snitch.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.x = 700
        self.y = 500
        
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
        
class Quaffle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('quaffle.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.x = 320
        self.y = 280
        
          #random movement // design object to move 1 pixel per each instance in while loop 
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 11
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
        
class Bludger1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bludger.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.x = 20
        self.y = 500
        
          #random movement // design object to move 1 pixel per each instance in while loop 
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 11
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
        
class Bludger2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bludger.bmp').convert()
        self.transColor = self.image.get_at((0,0))
        self.image.set_colorkey(self.transColor)
        self.rect = self.image.get_rect()
        self.x = 700
        self.y = 20
        
          #random movement // design object to move 1 pixel per each instance in while loop 
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 11
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
        
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

        

      
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
walls = [] 
#sprite= pygame.image.load('HarryPotter.bmp')

#quidditch = pygame.sprite.Renderplain(())
mouse.set_visible(False)

f = pygame.font.SysFont(None, 25)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

clock = pygame.time.Clock()
crashed = False

pygame.mixer.music.load('HarryPotter.wav')
pygame.mixer.music.play(loops=-1)

#pygame.mixer.music.stop()

# group all sprites together so can draw and move all with just one command
quidditch.add(hp)
quidditch.add(snitch)
quidditch.add(quaffle)
quidditch.add(bludger1)
quidditch.add(bludger2)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        
        elif event.type == pygame.KEYDOWN:
            if hp.hit(quaffle):
            #mixer.Sound("cha-ching.wav").play()
                quaffle.move()
                hits += 10
                
            
            if pygame.sprite.collide_rect(hp,snitch):
                #quaffle.move()
                text_end = f.render("You caught the snitch! YOU WIN", True, (0,0,0))
                screen.blit(text_end, (380, 300))
                pygame.display.flip()
                print ('You won the Quidditch game')
                quit()
            
            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
        elif event.type == USEREVENT + 1: # TIME has passed
            snitch.move()
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        hp.move(-2, 0)
    if key[pygame.K_RIGHT]:
        hp.move(2, 0)
    if key[pygame.K_UP]:
        hp.move(0, -2)
    if key[pygame.K_DOWN]:
        hp.move(0, 2)
        
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
        
    #if hp.rect.colliderect(bludger1.rect):
        #gameExit = True
     #   print ('Hello')
        

    hp.handle_keys()
    snitch.handle_keys()
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
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(120)

#pygame.display.flip() 		#similar to a flip book, updates entire surface
#pygame.display.update()		#only updates portion specified


#required
pygame.quit()
quit()	

