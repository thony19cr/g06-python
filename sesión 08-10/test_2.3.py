"""Control de excepciones"""
"""
TypeError.
ZeroDivisionError
OverflowError
IndexError
KeyError
FileNotFoundError
ImportError
"""

"""Estructura y uso"""
"""
    try:
        #bloque de código 1
    except exepción:
        #bloque de código 2
    else:
        #bloque de código 3
"""


def division(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    else:
        print(resultado)


division(20, 0)

division(100, 40)
