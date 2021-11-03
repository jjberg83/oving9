#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:58:13 2021

@author: jjberg
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
        if entered_integer == self.correct_answer:
            return True
        else:
            return False
        
    
    def korrekt_svar_tekst(self):
        return self.alternatives[self.correct_answer]
    
    
    def __str__(self):
        return f'{self.question}\n' + '\n'.join(f'{indeks} - {element}' for indeks, element in enumerate(self.alternatives,1))+' \n'
       
    
if __name__ == '__main__':
    liste_med_alle_instansene = read_the_document()
    sum_spiller1 = 0
    sum_spiller2 = 0
    for oppgave in liste_med_alle_instansene:
        print(oppgave)
        svar_spiller1 = int(input(f'Velg et svaralternativ for spiller 1:\n'))
        svar_spiller2 = int(input(f'Velg et svaralternativ for spiller 2:\n'))
        print(f'Korrekt svar: {oppgave.korrekt_svar_tekst()}')
        if oppgave.answer_check(svar_spiller1-1):
            print(f'Spiller 1: Korrekt')
            sum_spiller1 += 1
        else:
            print(f'Spiller 1: Feil')
        if oppgave.answer_check(svar_spiller2-1):
            print(f'Spiller 2: Korrekt')
            sum_spiller2 += 1
        else:
            print(f'Spiller 2: Feil')
        
        
    print(f'Spiller 1 har til sammen {sum_spiller1} rette svar!')
    print(f'Spiller 2 har til sammen {sum_spiller2} rette svar!')  
"""
    

Programmet skal også telle antall korrekte svar for hver spiller og
skrive ut dette til slutt. 

Et eksempel på forventet output er oppgitt under. Det er helt OK at
nummereringen starter på 1 i stedet for 0, men da må dette være gjennomført. Nummeret til
korrekt svar i fila antar standard Python liste nummerering, som starter på 0.

spm_1 = MultipleChoice('Hva heter din kjære?', 1, ['Hanne', 'Lori', 'Kathrine'])
svar_1 = int(input(spm_1))
print(f'Du svarte at din kjære er {spm_1.alternatives[svar_1-1]}!')
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
    

    




    
