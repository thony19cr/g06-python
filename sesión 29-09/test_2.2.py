"""Diccionarios en Python"""

diccionario = {"nombre": "Python", "tipo": "Backend"}

print("Mi diccionario es: {}".format(diccionario))

"""Para eliminar valores de nuestros diccionario usamos: del"""

del diccionario["tipo"]

print("Mi diccionario actualizado es: {}".format(diccionario))

del diccionario["nombre"]

print("Mi diccionario actualizado es: {}".format(diccionario))
