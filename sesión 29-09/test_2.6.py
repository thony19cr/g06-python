"""Importando librería Random"""
"""random: manejor de número aleatorios"""

import random
listaNumeros = []

for indice in range(1, 20):
    #listaNumeros.append(indice)
    listaNumeros.append(random.randint(1, 20))

print(listaNumeros)
