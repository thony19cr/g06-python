"""Estructura de datos"""

"""Listas (pop): Quitar un elemento indicando su índice"""

lista = ["Día del descubrimiento de América", True, 1000, 20.8]

print("1er valor de mi lista: {}".format(lista[0]))
print("2do valor de mi lista: {}".format(lista[1]))

lista.append(False)
lista.append(800)

print("Mi lista actualizada tiene los siguiente datos: {}".format(lista))

lista.pop(1)
print("Mi lista actualizada tiene los siguiente datos: {}".format(lista))

lista.pop(0)
print("Mi lista actualizada tiene los siguiente datos: {}".format(lista))
