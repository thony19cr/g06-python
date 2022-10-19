"""Estructura de datos"""

"""Listas (copy): Copiar los elementos de una lista"""

var1 = ["sQLServer", "rDS", "mysql", "postgresql"]

var2 = var1.copy()
var2.append("sqlite3")

print("La copia de mi lista 1 es: {}".format(var1))
print("La copia de mi lista 2 es: {}".format(var2))
