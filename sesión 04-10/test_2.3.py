"""Programación funcional en Python"""


def multiplicar(a, b, c=100):
    resultado = a*b*c
    return resultado


print("El resultado de mi función es: {}".format(multiplicar(40, 3, 2)))
