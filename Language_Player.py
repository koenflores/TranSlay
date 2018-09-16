# -*- coding: utf-8 -*-
import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.x = 0
        self.y = 0
        self.health = 100
        self.maxHealth = 100
        self.height = 50
        self.width = 50
        self.alive = True
        self.streak = 0
        self.attack = 10
        self.isTurn = False
        self.correct = True
        self.percentHealth = self.health / self.maxHealth
        self.right = False
        
      
    def getHealth(self):
        return self.health
    
    def setRight(self,right):
        self.right = right
    
    def getRight(self):
        return self.right
    
    def getPercentHealth(self):
        return self.health / self.maxHealth
    
    def setCorrect(self, isCorrect):
        if isCorrect == True:
            self.correct = True
        elif isCorrect == False:
            self.correct = False
    
    def setHealth(self, health):
        self.health = health
        
    def setMaxHealth(self, maxHealth):
        self.maxHealth = maxHealth
        
    def getAttack(self):
        return self.attack
    
    
    def attackBoss(self):
        self.streak+=1
        
    
    def damageByBoss(self, damage):
        self.health-= damage
    
    def heal(self, heal):
        self.health+=heal
        
    def setTurn(self, isTurn):
        if isTurn == True:
            self.isTurn = True
        elif isTurn == False:
            self.isTurn == False
    
    def getTurn(self):
        return self.isTurn
        
    