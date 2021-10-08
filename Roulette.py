from math import *
# from os import stat
from random import *
from time import *
from tkinter import *

# INTRODUCTION

## Global vars

adjlist = ['mighty', 'fierce', 'incredible', 'ferocious', 'beautiful', 'charming', 
            'strong', 'marvellous', 'phenomenal', 'remarkable', 'spectacular', 
            'prodigious', 'dazzling', 'amazing', 'formidable','astonishing']
obj_list = []
option_dic = {
    'odd_even' : '1:1',
    'firsthalf_secondhalf' : '1:1',
    'primeNumber': '4:1',
    'rangeOf10' : '10.1',
    'fiveNumbers' : '20:1',
    'fourNumbers' : '25:1',
    'threeNumbers' : '33:1',
    'twoNumbers' : '50:1',
    'straight' : '100:1'
}

class Player:
    name_list = []

    def __init__(self, name, cash=15000):
        self.name = name
        self.cash = float(cash)
        Player.Names(self)
    
    @classmethod
    def Names(cls,self):
        cls.name_list.append(self.name)  
    
    @classmethod
    def print_names(cls):
        print(cls.name_list)
    
    @classmethod
    def intro_fn(cls):
        string = 'The ultimate game between'
        shuffle(adjlist)
        for name, adj in zip(cls.name_list[:-1], adjlist):
            string = string + f' the {adj} {name},'
        string = string + f' and the {adjlist[-1]} {Player.name_list[-1]}!'
        print(string+'\n')

    def __add__(self,other):
        return self.cash + other.cash


class Round:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def initiate():
        global initiate
        print('Ladies and gentleman!')
        # sleep(1)
        print('Welcome to the greatest roulette game of the century!')
        # sleep(1.5)
        Player.intro_fn()
        # sleep(3)
        initiate = 'y' #input('shall we begin? (y/n)')
        
    def print_prob(self):
        n = 1
        for i,j in zip(list(option_dic.keys()), list(option_dic.values())):
            print(n,i,j)
            n +=1
        print('\n')
    
    def rules():
        pass

    @staticmethod
    def rollDice():
        return randint(0,32)
    


    def round(self):
        
        print('Choose a bet mf:')
        for i in range(len(obj_list)):
            choice = int(input(f'{self.obj[i].name}, enter bet number (1-9): '))

            while choice not in range(1,10):
                choice = int(input(f'{self.obj[i].name}, stop fkn around nigga, enter bet number again (1-9): '))
        dice = Round.rollDice()
      

def input_fn():
    players = 3 #int(input('Enter the number of players: '))
    return players

def main():
    players = input_fn()

    for i in range(1,players+1):
        player = Player('name'+str(i)) #input(f"Enter Player{i}'s gamertags: ")
        obj_list.append(player)


    Round.initiate()
    if initiate == 'n':
        print('farewell brothers and sisters')
    else:
        game = Round(obj_list) # create game instance

        game.print_prob() # print probabilities
        game.round()

main()





