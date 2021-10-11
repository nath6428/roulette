import random as r
import sympy as sym
import tkinter as tk

numlist = [x for x in range(0,100)]
number = 18
class bets():

    def __init__(self, cash):
        self.cash = cash
   
    @staticmethod
    def rollWheel():
        return r.randint(0,32)

    def firstHalf(self):
        # first = 1 | second = 2
        flag = int(input('First (1) / Second (0): '))
        if flag == 1:
            if number <=49:
                self.cash = self.cash*2
        else:
            if number >49:
                self.cash = self.cash*2
        return self.cash
        
    def evenodd(self):
        # Even = 1 | Odd = 2
        flag =  int(input('Even(1) / Odd(0): '))
        if flag == 1:
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
        rangeLst = input("enter start and end of 10 numbers, e.g 10-20")
        rangeLst = list(map(int, rangeLst.split('-')))

        if number in list(range(rangeLst[0],rangeLst[1])):
            self.cash = self.cash * 10      
        return self.cash
    
    def oneToFiveNumbers(self):
        oddsDict = {1: 100, 2: 50, 3: 33, 4: 25, 5: 20}

        inp = input('enter numbers to 1 to 5 Numbers, e.g 1,2,..')
        lst = list(map(int, inp.split(',')))
        if number in lst:
            self.cash = self.cash*(oddsDict[len(lst)])
        return self.cash

# number = bets.rollWheel()

# Player = bets(15000)
# print(Player.evenodd(1))
