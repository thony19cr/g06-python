"""

    3. Crear una función donde el usuario ingresa un número entero.
    Requisitos
    - La función debe indicar si el número ingresado es primo o no.
    - Retornar True si el número es primo si no retornar False.

"""


def primo(numero):

    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


num = int(input("Ingrese el número a evaluar"))
if primo(num):
    print("El número {} es primo".format(num))
else:
    print("El número {} no es primo".format(num))
