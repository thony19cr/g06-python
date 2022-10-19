"""Estructura de datos"""

"""Listas (count): Cantidad de veces que aparece un elemento que se repite en una lista"""


lista = ["Python", "Ruby", "Javascript", "Java"]

lista.append("Python")
lista.append("Python")
lista.append("Java")

print("Mi lista actualizada es: {}".format(lista))
print("La cantidad de veces que se repite 'Java' es: {}".format(lista.count("Java")))
print("La cantidad de veces que se repite 'Python' es: {}".format(lista.count("Python")))
