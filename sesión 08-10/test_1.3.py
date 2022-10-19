"""
    1. Crear una clase Persona
    Requerimientos:
    - Debe tener dos métodos, ahorrar y retirar
    - Inicializar la clase con los valores de monto en bolsillo con 100 dólares y el valor monto ahorro
    - Instanciar la clase Persona para ahorrar 10 USD, luego ahorra 20 USD
    - Un método para saber el monto que se tiene ahorrado.
"""


class Persona():

    def __init__(self):
        self.montoBolsillo = 100
        self.montoAhorro = 0

    def ahorrar(self, monto):
        self.montoAhorro = self.montoAhorro + monto
        self.montoBolsillo = self.montoBolsillo - monto

    def retirar(self, monto):
        self.montoBolsillo = self.montoBolsillo + monto
        self.montoAhorro = self.montoAhorro - monto

    def mostrarAhorro(self):
        print("Usted tiene ahorrado: {} USD".format(self.montoAhorro))

    def mostrarMontoBolsillo(self):
        print("Usted tiene: {} USD en bolsillo".format(self.montoBolsillo))


persona1 = Persona()
persona1.ahorrar(10)
persona1.ahorrar(20)
persona1.retirar(5)

persona1.mostrarAhorro()
persona1.mostrarMontoBolsillo()
