"""Listas en Python"""

"""Listas: recorrido de una lista"""

sueldos = [1000, 1500, 2000, 4000, 5000, 8000, 9000]

print("Tamaño de mi lista es: {}".format(len(sueldos)))

for i in range(len(sueldos)):
    print(sueldos[i])
    sueldos[i] = sueldos[i]*2

print("Mi lista actualizada es: {}".format(sueldos))
