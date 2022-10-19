
"""
    2. Crear una función donde el usuario ingresará el número 0, en este caso el programa se detendrá.
    Requisitos:
    - Crear lógica dentro de la función
    - Mostrar la suma de dígito

"""


def sumarDigitos(numero):
    suma = 0
    while numero!=0:
        digito = numero%10
        suma = suma + digito
        numero = int(numero/10)
        print("digito: {}".format(digito))
        print("suma de digitos: {}".format(suma))
    return suma


num = int(input("Ingrese número a procesar: "))

while num!=0:
    print("Suma: {}".format(sumarDigitos(num)))
    num = int(input("Ingrese número a procesar: "))
