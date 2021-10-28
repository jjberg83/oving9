#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:58:13 2021

@author: jjberg_
"""

def read_the_document():
    question_list = list()
    with open('sporsmaalsfil.txt', 'r', encoding='UTF8') as fila:
        for linje in fila:
            linje_liste = linje.replace(':', ',').strip('\n').split(',')
            #print(linje_liste)
            sporsmaal = linje_liste[0]
            rett_svar = int(linje_liste[1])
            alternativer = linje_liste[2].strip(' []').split(',')
            #print(f'Spørsmålet er: {sporsmaal}')
            #print(f'Rett svar er: {rett_svar}')
            print(f'Alternativene er: {alternativer}')
            

class MultipleChoice:
    #Constructor
    def __init__(self, question, correct_answer, alternatives):
        self.question = question
        self.correct_answer = correct_answer
        self.alternatives = alternatives
        
    
    def answer_check(self, entered_integer):
        if entered_integer == self.correct_answer:
            return 'You´re right champ!'
        else:
            return 'Sorry mate, that´s not correct...'
    
    
    def __str__(self):
        return f'{self.question} (enter the number you think is correct under the dotted line below)\n' + '\n'.join(f'{indeks} - {element}' for indeks, element in enumerate(self.alternatives,1))+ '\n--------------------\n'
       
    
if __name__ == '__main__':
    read_the_document()
    
    
    
    
    
    
    
    
    
    """
    question1 = MultipleChoice('What is best?', 1 , ['Mac', 'PC'])
    answer1 = int(input(question1))
    print(question1.answer_check(answer1))
    """
    




    
