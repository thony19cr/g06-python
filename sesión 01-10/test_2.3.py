"""Uso del for"""

ingenierias = ["Software", "Sistemas", "Industrial", "Química"]

nombre = input("Ingrese su primer nombre: ")
i = 0

print("El tamaño de mi lista es: {} y el programa fue creado por: {}".format(len(ingenierias), nombre))

for ingenieria in ingenierias:
    print(ingenieria)
    print("Esta es la vuelta número: {}".format(i))
    i = i + 1