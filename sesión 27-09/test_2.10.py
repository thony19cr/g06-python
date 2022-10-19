"""Estructura de datos"""

"""Listas (del): Un dato de la lista indicando el índice, usando: del"""

lista = []
lista.append(2022)
lista.append("Setiembre")
lista.append("Módulo 1")
lista.append(40)

print(lista)

del lista[2]
print("Mi lista actualizada es: {}".format(lista))

""""""
del lista[6]