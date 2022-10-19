
from funciones import suma, multiplicar

var1 = int(input("Ingrese un primer valor: "))
var2 = int(input("Ingrese un segundo valor: "))

sum = suma(var1, var2)
print("El resultado de sus dos valores es: {}".format(sum))

mul = multiplicar(var1, var2)
print("El resultado de sus dos valores es: {}".format(mul))
