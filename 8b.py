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
            sporsmaal = linje_liste.pop(0)
            rett_svar = int(linje_liste.pop(0))
            alternativer = [x.strip(' []') for x in linje_liste]
            ny_instans = MultipleChoice(sporsmaal, rett_svar, alternativer)
            question_list.append(ny_instans)
    return question_list
            

class MultipleChoice:
    #Constructor
    def __init__(self, question, correct_answer, alternatives):
        self.question = question
        self.correct_answer = correct_answer
        self.alternatives = alternatives
        
    
    def answer_check(self, entered_integer):
        if entered_integer == self.correct_answer+1:
            return True
        else:
            return False
        
    
    def korrekt_svar_tekst(self):
        return self.alternatives[self.correct_answer]
    
    
    def __str__(self):
        return f'{self.question}\n' + '\n'.join(f'{indeks} - {element}' for indeks, element in enumerate(self.alternatives,1))+ '\n'
       
    
if __name__ == '__main__':
    liste_med_alle_instansene = read_the_document() # Unngår jeg global variabel slik?
    sum_spiller1 = 0
    sum_spiller2 = 0
    for sporsmaal in liste_med_alle_instansene:
        print(sporsmaal)
        svar_spiller1 = int(input("Velg et svaralternativ for spiller 1: "))
        svar_spiller2 = int(input("Velg et svaralternativ for spiller 2: "))
        print(f'Korrekt svar: {sporsmaal.korrekt_svar_tekst()}')
        if sporsmaal.answer_check(svar_spiller1):
            sum_spiller1 += 1
            print('Spiller 1: Korrekt')
        else:
            print('Spiller 1: Feil')
        if sporsmaal.answer_check(svar_spiller2):
            sum_spiller2 += 1
            print('Spiller 2: Korrekt')
        else:
            print('Spiller 2: Feil')
    print(f'Sum spiller 1: {sum_spiller1}')
    print(f'Sum spiller 2: {sum_spiller2}')
        
        
        
        
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
    
    
    
    
    
    
    
    
    

    




    
