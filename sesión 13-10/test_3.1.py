
"""Decoradores en Python"""

"""Creación interna de la función decoradora"""
def funcionA(funcionB):

    """Funcion interna de la función decoradora"""
    def funcionC():
        print("1. Antes de ejecutar la función a decorar\n")
        funcionB()
        print("2. Después de ejecutar la función a decorar\n")

    return funcionC()

@funcionA
def saludar():
    print("Hola Pythonistas!!")

#saludar()
