import random as r
from typing import Dict
import sympy as sym
import tkinter as tk

cash = 1


numlist = [x for x in range(0,100)]
number = r.randint(0,99)
print(number)

class bets():
    def __init__(self, cash):
        self.cash = cash
 
        
    def firstHalf(self, HalfSelection):
        firstHalfList = [x for x in range(0,50)]
        if HalfSelection == 1:
            if number in firstHalfList:
                self.cash = self.cash*2
        else:
            if number not in firstHalfList:
                self.cash = self.cash*2
        
    def evenodd(self, EvenOddSelection):
        # Even = 1 | Odd = 2
        Evenlist = [item for item in numlist if item%2==0]
        if EvenOddSelection == 1:
            if number in Evenlist:
                self.cash = self.cash*2
        else:
            if number not in Evenlist:
                self.cash = self.cash*2
            

    def prime(self):
        Primelist = [x for x in sym.primerange(0,100)]
        if number in Primelist:
            self.cash = self.cash*4



    def rangeof10(self):
        rangeof10_int = int(input('rangeend'))
        if (rangeof10_int < 10 or rangeof10_int > 100):
                print('retry')
        else:
            rangeof10List = [x for x in range(rangeof10_int-10, rangeof10_int)]
            if number in rangeof10List:
                self.cash = self.cash*10
        
    def oneToFiveNumbers(self):
        numlist_input = (input("1-5 Numbers").split(','))
        numlist_input = list(map(lambda x:int(x), numlist_input))
        oddsDict = {1: 100,
                2: 50,
                3: 33,
                4: 25,
                5: 20}
        if number in numlist_input:
            self.cash = self.cash*(oddsDict[len(numlist_input)])
        



Player = bets(cash)
