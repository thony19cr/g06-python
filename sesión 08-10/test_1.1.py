"""POO en Python"""
"""Encapsulamiento"""


class A():
    def __init__(self):
        """Encapsulamiento"""
        self.inicial = False
        self._contador = 0 #Definiendo mi atributo privado

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador


class B():
    def __init__(self):
        """Encapsulamiento"""
        self.inicial = True
        self.__contador = 0 #Definiendo mi atributo privado

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador


varA = A()
varA._contador
varA.inicial = True

varA.incrementa()
varA.incrementa()

print(varA.cuenta())

print("Contador A: {}".format(varA._contador))

varB = B()
varB.inicial = False

varB.incrementa()
varB.incrementa()
varB.incrementa()

print("Valor de contador es: {}".format(varB.cuenta()))
print("Valor de inicial de Clase B: {}".format(varB.inicial))

"""No es posible invocar a una variable porque el encapsulamiento es fuerte por los dos guiones abajo"""
print("Contador B: {}".format(varB.__contador))
