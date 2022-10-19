"""Manejo de errores"""


def operacion(a, b):
    try:
        #resultado = a/b
        resultado = 100 + "Hola Pythonista"
    except (ZeroDivisionError, TypeError):
        print("Excepción ZeroDivisionError/TypeError")
    else:
        print(resultado)


operacion(4, 9)
