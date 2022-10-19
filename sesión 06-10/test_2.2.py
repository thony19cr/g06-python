"""
    Programación Orientada a Objetos
    Atributos
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


carro1 = Carro("Blanco", 20)

print("El color de mi primer carro es: {}".format(carro1.color))

carro2 = Carro("Negro", 50)
carro2.marchas = 3000

print("El número de marchas de mi segundo carro es: {}".format(carro2.marchas))

"""IMPORTANTE"""
"""No es posible llamar un atributo de datos que se le ha asignado a otra instancia de la clase"""
#print("El número de marchas de mi primer carro es: {}".format(carro1.marchas))
