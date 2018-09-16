# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 13:29:54 2018

@author: koenf
"""
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        



def drawHealthBars(window, top, bottom, left, right):
    
    for ii in range(top,bottom): # life timer, top and bottom lines of rectangle
        pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,left,2,2))
        pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,right,2,2))
        
    for ii in range(left,right): # life timer, left and right lines of rectangle
        pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(top,ii,2,2))
        pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(bottom,ii,2,2))
        
def drawQuestion(window):
    #displays question***********************************************************
    largeText = pygame.font.SysFont('comicsansms',35)
    TextSurf, TextRect = text_objects("What is to be in Spanish?", largeText,  (60,60,60) )
    TextRect.center = (1020, 600)
    window.blit(TextSurf, TextRect)

    #displays choices************************************************************
    choice1 = button('to talk',850, 650, 100, 50, (100,100,100), (200,200,200),None)
    choice2 = button('to do',970, 650, 100, 50, (100,100,100), (200,200,200),None)
    choice3 = button('to be',1090, 650, 100, 50, (100,100,100), (200,200,200),None)
     
        
def button(msg, x, y, w, h, initialColor, afterColor, action=None):
    
    #creates mouse and click variables to track mouse behavior
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  
    #if mouse is within the button range, the color changes
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, afterColor,(x,y,w,h))

        if click[0] == 1 and action != None:
            #if button is clicked the action occurs
            action()         
    else:
    #if mouse is not within button range, the color is the inital color
        pygame.draw.rect(window, initialColor,(x,y,w,h))

    
    smallText = pygame.font.SysFont("comicsansms",20)
    
    #passes into text_objects to create words
    textSurf, textRect = text_objects(msg, smallText, (100,90,80))
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)
    
            