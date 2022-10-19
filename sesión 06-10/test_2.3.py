"""
    Programación Orientada a Objetos
   Clases y métodos
"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Contructor: Valores que van a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de la clase"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad<0:
            velocidad=0
        self.velocidad = velocidad


carro1 = Carro("Azul", 60)

print("La velocidad inicial de mi carro 1 es: {}".format(carro1.velocidad))

carro1.acelerar()
carro1.acelerar()
carro1.acelerar()

print("La velocidad inicial de mi carro 1 es: {}".format(carro1.velocidad))

carro1.frena()
carro1.frena()

print("La velocidad actual mi carro 1 es: {}".format(carro1.velocidad))

