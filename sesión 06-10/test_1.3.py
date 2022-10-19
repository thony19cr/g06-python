"""

    4. Crear una función donde el usuario ingresa un número entero.
    Requisitos
    - La función debe arrojar el factorial del número ingresado
    - El programa debe terminar si ingresa el valor de -1

"""


def factorial(numero):
    fact = 1
    if numero!=0:
        for num in range(1, numero+1):
            fact = fact * num
    return fact


num = int(input("Ingrese un número: "))

while num!=-1:
    print("El factorial es: {}".format(factorial(num)))

    num = int(input("Ingrese el valor de -1 para terminar el programa: "))
