#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:58:13 2021

@author: jjberg
"""

class MultipleChoice:
    #Constructor
    def __init__(self, question, alternatives, correct_answer):
        self.question = question
        self.alternatives = alternatives
        self.correct_answer = correct_answer
        
    
    def answer_check(self, entered_integer):
        if entered_integer == self.correct_answer:
            return 'You´re right champ!'
        else:
            return 'Sorry mate, that´s not correct...'
    
    
    def __str__(self):
        return f'{self.question} (enter the number you think is correct under the dotted line below)\n' + '\n'.join(f'{indeks} - {element}' for indeks, element in enumerate(self.alternatives,1))+ '\n--------------------\n'
       
    
if __name__ == '__main__':
    question1 = MultipleChoice('What´s best?', ['Mac', 'PC'], 1)
    question2 = MultipleChoice('Biggest city in England?' , ['Manchester','Liverpool', 'London'], 3)
    answer1 = int(input(question1))
    print(question1.answer_check(answer1))
    answer2 = int(input(question2))
    print(question2.answer_check(answer2))
    




    
