from math import *
from random import *
from time import *
from tkinter import *

# INTRODUCTION

## Player Profile Creation
class Player:
    def __init__(self, name, cash=15000):
        self.name = name
        self.cash = float(cash)

lst = []
def input_fn():
    players = int(input('Enter the number of players: '))
    for i in range(1,players+1):
        pname = Player(input(f'Enter Player {i}s name: '))
        lst.append(pname)

