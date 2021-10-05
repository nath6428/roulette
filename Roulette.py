from math import *
from random import *
from time import *
from tkinter import *

# INTRODUCTION

## Player Profile Creation
lst = []
adjlist = [
'mighty', 
'fierce', 
'incredible', 
'ferocious', 
'beautiful', 
'charming', 
'strong', 
'marvellous', 
'phenomenal', 
'remarkable', 
'spectacular', 
'prodigious', 
'dazzling', 
'amazing', 
'formidable',
'astonishing']

def adj_fn():
    adj = adjlist[randint(0,len(adjlist))]
    adjlist.pop(adjlist.index(adj))
    return adj


class Player:
    def __init__(self, name, cash=15000):
        self.name = name
        self.cash = float(cash)

    def input_fn():
        players = int(input('Enter the number of players: '))
        for i in range(1,players+1):
            pname = Player(input(f'Enter Player {i}s name: '))
            lst.append(pname)

    @classmethod
    def print_fn(cls):
        tempnamelist = []
        for i in lst:
            tempnamelist.append(i.name)
        print(tempnamelist)
            
        name_list = (", ".join(zip(tempnamelist, adjlist)[:-1]))

        # print(f'the ultimate game between {adj_fn()} {name_list} and {tempnamelist[-1]}!')

p1 = Player('sa')
p1.print_fn()