"""Uso del uso condicional life"""

var1 = int(input("Ingrese su primer valor numérico: "))
var2 = int(input("Ingrese su segundo valor numérico: "))

if var1 > var2:  # Si es 'True' ejecuta su lógica interna del flujo condicional
    print("El valor de var1 es mayor que la segunda variable ingresada")
elif var1 == var2:
    print("Los valores ingresados son iguales")
else:
    print("El valor de var1 no es mayor que la segunda variable ingresada")


