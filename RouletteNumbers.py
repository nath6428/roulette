import random as r
import sympy as sym


numlist = [x for x in range(0,100)]
print(numlist)

number = numlist[r.randint(0,100)]
Evenlist = [x for x in range(0,100,2)]
print(Evenlist)
Oddlist = [item for item in numlist if item not in Evenlist]
print(Oddlist) 
Primelist = [x for x in sym.primerange(0,100)]
print(Primelist)

