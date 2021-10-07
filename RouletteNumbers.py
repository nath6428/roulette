import random as r
from typing import Dict
import sympy as sym
import tkinter as tk


cash = 1

numlist = [x for x in range(0,100)]


number = 7
firstHalfList = [x for x in range(0,50)]
Evenlist = [x for x in range(0,100,2)]
Oddlist = [item for item in numlist if item not in Evenlist]
Primelist = [x for x in sym.primerange(0,100)]
# rangeof10 = int(input('rangeend'))
# if (rangeof10 < 10 or rangeof10 > 100):
#         print('retry')
# else:
#     rangeof10List = [x for x in range(rangeof10-10, rangeof10)]
#     print(rangeof10List)

numlist_input = (input("1-5 Numbers").split(','))
numlist_input = list(map(lambda x:int(x), numlist_input))

oddsDict = {1: 100,
        2: 50,
        3: 33,
        4: 25,
        5: 20}
if number in numlist_input:
    cash = cash*(oddsDict[len(numlist_input)])

print(number, cash)


