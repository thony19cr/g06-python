"""
    Programación Orientada a Objetos
    Herencia en Python
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


"""Aplicando  Herencia"""
"""Creamos nuestra clase Hija"""


class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carro1 = Carro("Rojo", 30)
carroVolador = CarroVolador("Blanco", 60)

print("Color de mi carro volador es: {}".format(carroVolador.color))
print("El estado inicial de mi carro volador es: {}".format(carroVolador.estadoVolando))
print("La velocidad inicial de mi carro volador es: {}".format(carroVolador.velocidad))

carroVolador.vuela()
carroVolador.acelerar()
carroVolador.acelerar()

print("La velocidad actual de mi carro volador es: {}".format(carroVolador.velocidad))

"""Esto no puede suceder, porque la herencia es sólo sobre la clase HIJA"""
#print("El estado de vuelo de mi primer carro es: {}".format(carro1.estadoVolando))
