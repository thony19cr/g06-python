"""Diccionarios en Python"""

"""Obtener elemento de una lista: paises[i]"""


paises = []
paises.append("Uruguay")
paises.append("Perú")
paises.append("España")
paises.append("Canadá")

print("Mi lista actual es: {}".format(paises))
print("El país de mi item 1 es: {}".format(paises[1]))
print("El país de mi item 3 es: {}".format(paises[3]))

edades = [13, 13, 11, 13, 11, 13, 13, 13]
print("El índice de mi edad errónea es: {}".format(edades[2]))
actualizar = edades[2] + 2
edades[2] = 13
edades[4] = 13

print("Mi lista actualizada de edades es: {}".format(edades))
