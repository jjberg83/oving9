#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:58:13 2021

@author: jjberg
"""

            

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
        
    
    def korrekt_svar_tekst(self):
        return self.alternatives[self.correct_answer]
    
    
    def __str__(self):
        return f'{self.question}\n' + '\n'.join(f'{indeks} - {element}' for indeks, element in enumerate(self.alternatives,1))+'\n--------------\nDitt svar her: \n'
       
    
if __name__ == '__main__':
    spm_1 = MultipleChoice('Hva heter din kjære?', 1, ['Hanne', 'Lori', 'Kathrine'])
    svar_1 = int(input(spm_1))
    print(f'Du svarte at din kjære er {spm_1.alternatives[svar_1-1]}!')
    
 
"""
Her er et eksempel på spill, de to første spørsmålene:
    
Den delen av en datamaskin som kjører programmet kalles? 
Svaralternativer:
0: RAM
1: Harddisk
2: CPU
3: Sekundærlager

Velg et svaralternativ for spiller 1: 0
Velg et svaralternativ for spiller 2: 2

Korrekt svar: CPU

Spiller 1: Feil
Spiller 2: Korrekt
"""
    

    




    
