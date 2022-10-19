"""Uso de la librería date y datetime"""
"""
    Conversión total del tiempo
"""

from datetime import datetime

"""Uso del método timestamp"""

timeNow = datetime.strptime("2022/12/15 20:30:00", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversión de nuestro valor timenow es: {}".format(timeNow))
