import random as r
import sympy as sym
import tkinter as tk

numlist = [x for x in range(0,100)]

class bets():
    def __init__(self, cash):
        self.cash = cash
   
    @staticmethod
    def rollWheel():
        return r.randint(0,32)

    def firstHalf(self, HalfSelection):
        # first = 1 | second = 2
        if HalfSelection == 1:
            if number <=49:
                cash = self.cash*2
        else:
            if number >49:
                cash = self.cash*2
        return cash
        
    def evenodd(self, EvenOddSelection):
        # Even = 1 | Odd = 2
        if EvenOddSelection == 1:
            if number%2 == 0:
                self.cash = self.cash*2
        else:
            if number%2 != 0:
                self.cash = self.cash*2
        return self.cash
            

    def prime(self):
        Primelist = [x for x in sym.primerange(0,100)]
        if number in Primelist:
            self.cash = self.cash*4
        return self.cash



    def rangeof10(self):
        rangeof10_int = int(input('rangeend'))
        if (rangeof10_int < 10 or rangeof10_int > 100):
            print('retry')
        else:
            rangeof10List = [x for x in range(rangeof10_int-10, rangeof10_int)]
            if number in rangeof10List:
                self.cash = self.cash*10
        return self.cash
        
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
        return self.cash
     

number = bets.rollWheel()

Player = bets(15000)
print(Player.evenodd(1))
