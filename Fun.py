from math import *
from cmath import *
from random import *
from time import *
from tkinter import *

#  introduction 
lst = []
def input_fn():
    players = int(input('Enter the number of players: '))
    for i in range(1,players+1):
        pname = Player(input(f'Enter Player {i}s name: '))
        lst.append(pname)
    #for y in range(players):
        # print(lst[y].name)
    

class Player:
    def __init__(self, name):
        self.name = name
    def intro(self):
        global initiate
        print('Ladies and gentleman!')
        sleep(2)
        print('Welcome to the greatest roulette game of the century!')
        sleep(2)
        print('the ultimate game between the mighty', lst[0].name )
        sleep(3)
        initiate = input('shall we begin? (y/n)')
    
    @classmethod
    def print_fn(cls):
        listt = []
        for i in lst:
            listt.append(i.name)
        
        name_list = (", ".join(listt[:-1]))

        print(f'the ultimate game between {name_list} and {listt[-1]}!')




# rules 
def rules():
    print('Thats excellent, lets kick this off with the rules of the game')
    sleep(2)
    print('The game we will be playing, is quite obviously, roulette!')
    sleep(2)
    

if initiate == 'y':
    rules()
else:
    re = input('thats unfortunate! would you like to give it another shot?')
    if re == 'y':
        Player.intro()
    else:
        print('Thats truly sad, you will be missed :(')
        sleep(2)
        print('Farewell warriors!')
        exit()


input_fn()

Player.print_fn()