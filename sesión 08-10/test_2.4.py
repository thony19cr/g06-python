"""Manejo de errores"""


def operacion(a, b):
    try:
        #resultado = a/b
        resultado = 100 + "Hola Pythonista"
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    except TypeError:
        print("No se puede sumar un string con un dato tipo int")
    else:
        print(resultado)


operacion(4, 9)
