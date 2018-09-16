# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 13:21:26 2018

@author: koenf
"""
import pygame
from Language_Background import Background, drawHealthBars
from Language_Player import Player
from GIFImage import GIFImage
from Language_Questions import spanishVerbs
from Language_QuestionMode import Question

questionsRight = 0

#******************************************************************
def text_objects(text, fonts, color):
    textSurface = fonts.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
#******************************************************************
def button(msg, x, y, w, h, initialColor, afterColor,isRight, action=None):
    
    #creates mouse and click variables to track mouse behavior
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  
    #if mouse is within the button range, the color changes
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, afterColor,(x,y,w,h))

        if click[0] == 1 and isRight == False :
            #if button is clicked the action occurs
            player1.damageByBoss(3)
            player2.damageByBoss(1)
            player3.damageByBoss(1)
            player1.setRight(False)
            explosion.render(window, (180,180))
            
        elif click[0] == 1 and isRight == True :
            player1.heal(10)
            player2.heal(5)
            player3.heal(5)
            boss.damageByBoss(10)
            player1.setRight(True)
            slash.render(window,(550,130))
            player.render(window, (80,150))
            
            
    else:
    #if mouse is not within button range, the color is the inital color
        pygame.draw.rect(window, initialColor,(x,y,w,h))

    
    smallText = pygame.font.SysFont("comicsansms",20)
    
    #passes into text_objects to create words
    textSurf, textRect = text_objects(msg, smallText, (225,225,225))
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)

#draw question********************************************************************   
    
def drawQuestion(window, question, choice1, choice2, answer):
    #displays question***********************************************************
    largeText = pygame.font.SysFont('comicsansms',35)
    TextSurf, TextRect = text_objects(question, largeText,  (225,225,225) )
    TextRect.center = (970, 600)
    window.blit(TextSurf, TextRect)

    #displays choices************************************************************
    button(choice1,800, 650, 100, 50, (232,93,117), (32,164,243),False,None)
    button(choice2,920, 650, 100, 50, (232,93,117), (32,164,243),False,None)
    button(answer,1040, 650, 100, 50, (232,93,117), (32,164,243),True,None)

#draw question********************************************************************   
    
def drawQuestion2(window, question, choice1, choice2, answer):
    #displays question***********************************************************
    largeText = pygame.font.SysFont('comicsansms',35)
    TextSurf, TextRect = text_objects(question, largeText,  (225,225,225) )
    TextRect.center = (970, 600)
    window.blit(TextSurf, TextRect)

    #displays choices************************************************************
    button(choice1,800, 650, 100, 50, (232,93,117), (32,164,243),False,None)
    button(answer,920, 650, 100, 50, (232,93,117), (32,164,243),True,None)
    button(choice2,1040, 650, 100, 50, (232,93,117), (32,164,243),False,None)
    
    
#draw question********************************************************************   
    
def drawQuestion3(window, question, choice1, choice2, answer):
    #displays question***********************************************************
    largeText = pygame.font.SysFont('comicsansms',35)
    TextSurf, TextRect = text_objects(question, largeText,  (225,225,225) )
    TextRect.center = (970, 600)
    window.blit(TextSurf, TextRect)

    #displays choices************************************************************
    button(answer,800, 650, 100, 50, (232,93,117), (32,164,243),True,None)
    button(choice2,920, 650, 100, 50, (232,93,117), (32,164,243),False,None)
    button(choice1,1040, 650, 100, 50, (232,93,117), (32,164,243),False,None)

pygame.init()
pygame.display.init()

fps = pygame.time.Clock()

#window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
window = pygame.display.set_mode((1200,750))  #sets size of pygame window
pygame.display.set_caption("Gemini")   #caption on top of window

#pygame.load('C:\Users\koenf\Projects\Shell Hacks\Floor.png')

#



player1 = Player()
#max health and health default 100

player2 = Player()
player2.setMaxHealth(150)
player2.setHealth(150)

player3 = Player()
player3.setMaxHealth(80)
player3.setHealth(80)

boss = Player()
boss.setMaxHealth(300)
boss.setHealth(300)

background = GIFImage("Background3sized.gif")
archer = GIFImage("Archer.gif")
bossGif = GIFImage("Bosss.gif")

player = GIFImage("PlayerFinal2.gif")
playerBlue = GIFImage("PlayerBlue.gif")
playerGreen = GIFImage("PlayerGreen.gif")
playerStand = GIFImage("PlayerStanding.gif")

slash = GIFImage("SlashFinal.gif")
explosion = GIFImage("ExplosionFinal.gif")

p1 = GIFImage("p1.gif")

while True:
    
    
    #background = Background('Background2.png', [0,0])
    
    #background.render(window, (1000,500))
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #sys.exit()


    window.fill(pygame.Color(225,225,225))
    background.render(window, (20, 0))
    
    #archer.render(window, (30, 200))
    bossGif.render(window, (700, 200))
    #player.render(window, (80,150))
   # if player1.getRight != True:
    #   playerStand.render(window, (80,150))
    #else:
     #   player.render(window, (80,150))
    player.render(window, (80,150))
    
    playerGreen.render(window,(-60,130))
    playerBlue.render(window,(-10,170))
    #slash.render(window,(550,130))
    #explosion.render(window, (180,180))
    
    p1.render(window,(0, 20))
    #window.blit(background.image, background.rect)
    
    #*******************************player one bar************************************************
    drawHealthBars(window, 170,530,30,60)
    if player1.getPercentHealth() > 1:
        pygame.draw.rect(window, pygame.Color(10,200,0), pygame.Rect(172,31.5, 359,29.5))
    elif player1.getPercentHealth() > 0:
        pygame.draw.rect(window, pygame.Color(10,200,0), pygame.Rect(172,31.5, (player1.getPercentHealth()*359),29.5)) #(x location,y location,length % life,height of green square)
    
        
     #*******************************player two bar************************************************
    drawHealthBars(window, 170,530,75,105)
    if player2.getPercentHealth() > 1:
        pygame.draw.rect(window, pygame.Color(10,200,0), pygame.Rect(172,76.3, 359,29.5))
    elif player2.getPercentHealth() > 0:
        pygame.draw.rect(window, pygame.Color(10,200,0), pygame.Rect(172,76.3,(player2.getPercentHealth()*359),29.5)) #(,,length % life,height of green square)
   
     #*******************************player three bar************************************************
    drawHealthBars(window, 170,530,120,150)
    if player3.getPercentHealth() > 1:
        pygame.draw.rect(window, pygame.Color(10,200,0), pygame.Rect(172,121.5, 359,29.5))
    elif player3.getPercentHealth() > 0:
        pygame.draw.rect(window, pygame.Color(10,200,0), pygame.Rect(172,121.5,(player3.getPercentHealth()*359),29.5)) #(,,length % life,height of green square)
    
    
     #*******************************boss bar************************************************
    drawHealthBars(window, 810,1170,75,105)
    if boss.getPercentHealth() > 1:
        pygame.draw.rect(window, pygame.Color(10,200,0), pygame.Rect(812,76.3, 359,29.5))
    elif boss.getPercentHealth() > 0:
        pygame.draw.rect(window, pygame.Color(200,10,0), pygame.Rect(812,76.3,(boss.getPercentHealth()*359),29.5)) #(,,length % life,height of green square)
    
    
    
    if player1.getRight() == True:
        questionsRight+=1
        player1.setRight(False)
    #Questions*********************************************************************************
    if questionsRight == 0:    
        drawQuestion(window, "What is \"to be\" in Spanish?", spanishVerbs[0][1], spanishVerbs[0][2], spanishVerbs[0][0])
        spanishVerb1 = Question('Spanish', 'Easy', spanishVerbs[0][3], spanishVerbs[0][2], spanishVerbs[0][1], spanishVerbs[0][0])
        
    elif questionsRight == 1:
        drawQuestion2(window, "What is \"to talk\" in Spanish?", spanishVerbs[1][1], spanishVerbs[1][2], spanishVerbs[1][0])
        spanishVerb2 = Question('Spanish', 'Easy', spanishVerbs[1][3], spanishVerbs[1][2], spanishVerbs[1][1], spanishVerbs[1][0])
    
    elif questionsRight == 2:
        drawQuestion3(window, "What is \"to do\" in Spanish?", spanishVerbs[2][1], spanishVerbs[2][2], spanishVerbs[2][0])
        spanishVerb3 = Question('Spanish', 'Easy', spanishVerbs[2][3], spanishVerbs[2][2], spanishVerbs[2][1], spanishVerbs[2][0])
        
    '''
    for ii in range(120,480): # life timer
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,30,2,2))
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,60,2,2))
            
    for ii in range(30,60): # life timer
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(120,ii,2,2))
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(480,ii,2,2))


    #displays question***********************************************************
    largeText = pygame.font.SysFont('comicsansms',35)
    TextSurf, TextRect = text_objects("What is to be in Spanish?", largeText,  (225,225,225) )
    TextRect.center = (1020, 600)
    window.blit(TextSurf, TextRect)

    #displays choices************************************************************
    choice1 = button('to talk',850, 650, 100, 50, (232,93,117), (32,164,243),None)
    choice2 = button('to do',970, 650, 100, 50, (232,93,117), (32,164,243),None)
    choice3 = button('to be',1090, 650, 100, 50, (232,93,117), (32,164,243),None)
'''

    #print(player1.getHealth())
  
    #print(player2.getPercentHealth())
    print(questionsRight)

    pygame.display.flip()