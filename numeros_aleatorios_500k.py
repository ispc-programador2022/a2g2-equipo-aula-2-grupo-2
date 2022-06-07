from random import random
import random

def lista_aleatoria_500k():
    lista_500k= []
    for i in range(0,500000000000000000):    
        i = random.randint(0,500000000000000000)
        lista_500k.append(i)
    print(lista_500k)
    
lista_aleatoria_500k()