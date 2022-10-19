"""POO en Python"""
"""Polimorfismo"""

class Perro():
    def sonido(self):
        print("Guauuu")

class Gato():
    def sonido(self):
        print("Mmiauuu")

class Vaca():
    def sonido(self):
        print("Muuuu")

vaca = Vaca()
perro = Perro()
gato = Gato()

listaAnimales = [vaca, perro, gato]

def canto(animales):
    for animal in animales:
        animal.sonido()

"""Aplicando Polimorfismo: Es el uso de los métodos que tienen como mismo nombre en diferentes clases"""

canto(listaAnimales)
