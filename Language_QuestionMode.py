# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:32:48 2018

@author: koenf
"""
from Language_Questions import spanishVerbs, spanishVocab, filipinoSports, frenchFood

class Question():
    
    def __init__(self, language, difficulty, question, choice1, choice2, answer):
        self.language = language
        self.difficulty = difficulty
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2
        self.answer = answer
        self.correct = False
        self.right = False
        
    def getLanguage(self):
        return self.language
    
    def getDifficulty(self):
        return self.difficulty
    
    def getQuestion(self):
        return self.question
    
    def getChoice1(self):
        return self.choice1
    
    def getChoice2(self):
        return self.choice2
    
    def getAnswer(self):
        return self.answer
    
    def getCorrect(self):
        return self.correct
    
    def attemptAnswer(self, answer):
        if answer == self.answer:
            self.correct = True
        else:
            self.correct = False
            
    def setRight(self,right):
        self.right = right
    
    def getRight(self):
        return self.right
            
spanishVerb1 = Question('Spanish', 'Easy', spanishVerbs[0][3], spanishVerbs[0][2], spanishVerbs[0][1], spanishVerbs[0][0])

        