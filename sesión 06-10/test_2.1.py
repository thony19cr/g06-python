"""
    Programación Orientada a Objetos
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


"""Instanciamos nuestra clase"""
carro1 = Carro("Negro", 50)
print("El color de primer carro es: {}".format(carro1.color))
print("La aceleración de mi primer carro es: {}".format(carro1.aceleracion))
print("La cantidad total de ruedas de mi primer carro es: {}".format(carro1.ruedas))

carro2 = Carro("Rojo", 30)
print("El color de mi segundo carro es: {}".format(carro2.color))
print("La aceleración de mi segundo carro es: {}".format(carro2.aceleracion))

