from operator import le
from random import random


import random

def lista_aleatoria():
    lista= []
    for i in range(0,50):    
        i = random.randint(0,50)
        lista.append(i)
    print(lista)
    
lista_aleatoria()
