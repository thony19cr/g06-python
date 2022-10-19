"""Uso de la librería date y datetime"""

from datetime import datetime

strFecha = "2/6/2021"

"""
    d: día
    m: mes
    Y: año
"""

conversion = datetime.strptime(strFecha, "%m/%d/%Y")

print("La fecha formateada es: {}".format(conversion))

"""Traer el mes de la fecha con letras: strftime de datetime"""

conversionMes = datetime.strftime(conversion, "%d %b del %Y")
print("Nuestra fecha con cambio en el mes es el siguiente: {}".format(conversionMes))

""" 
    b: reemplaza a 'm' para mostrar el mes literalmente
"""