from math import *
from os import stat
from random import *
from time import *
from RouletteNumbers import *
# import pygame


# INTRODUCTION
## Global vars

adjlist = ['mighty', 'fierce', 'incredible', 'ferocious', 'beautiful', 'charming', 
            'strong', 'marvellous', 'phenomenal', 'remarkable', 'spectacular', 
            'prodigious', 'dazzling', 'amazing', 'formidable','astonishing']
obj_list = []
option_dic = {
    'odd_even' :'1:1',
    'firsthalf_secondhalf':'1:1',
    'primeNumber': '4:1',
    'rangeOf10': '10.1',
    'fiveNumbers': '20:1',
    'fourNumbers': '25:1',
    'threeNumbers': '33:1',
    'twoNumbers': '50:1',
    'straight': '100:1'
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


class Round:
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

        if initiate == 'n':
            print('fairwell brothers and sisters')
        else:
            print('Thats excellent, lets kick this off with the rules of the game')
            sleep(1)
            print('The game we will be playing, is quite obviously, roulette!')
            print('\n')
            
    @staticmethod
    def print_prob():
        for index, (odd, prob) in enumerate(zip(list(option_dic.keys()), list(option_dic.values())), start = 1):
            print(index, odd, prob)
        print('\n')
   
    def round(self):
        number = 18 #bets.rollDice()
        print('Choose a bet mf:')
        for i in obj_list:
            choice = int(input(f'{i.name}, enter bet number (1-9): '))
            while choice not in range(1,10):
                choice = int(input(f'{i.name}, stop fkn around nigga, enter bet number again (1-9): '))

            player = bets(i.cash)
            if choice == 1:
                flag = int(input('first/second: '))
                i.cash = player.evenodd(flag) 
                
            elif choice ==2:
                flag = int(input('first/second: '))
                i.cash = player.evenodd(flag)

            elif choice ==3:
                i.cash = player.prime()

            elif choice ==4:
                i.cash = player.rangeof10()

            elif choice ==5:
                i.cash = player.oneToFiveNumbers()

            elif choice ==6:
                # i.cash = player.oneToFiveNumbers()
                return False          

            elif choice ==7:
                # i.cash = player.oneToFiveNumbers()
                return False

            elif choice ==8:
                # i.cash = player.oneToFiveNumbers()
                return False

            elif choice ==9:            
                # i.cash = player.oneToFiveNumbers()
                return False



def input_fn():
    players = 4 #int(input('Enter the number of players: '))
    return players

def main():
    players = input_fn()

    for i in range(1,players+1):
        player = Player('name'+str(i)) #input(f"Enter Player{i}'s gamertags: ")
        obj_list.append(player)
    Round.initiate()
    if initiate == 'y':
        game = Round() # create game instance
        game.print_prob() # print probabilities
        game.round()

main()




for i in obj_list:
    print(i.cash)
