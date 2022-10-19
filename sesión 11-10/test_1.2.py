"""Uso de la librería date y datetime"""
"""
    Conversión de fechas
"""

import datetime

fecha1 = datetime.datetime(2023, 4, 13) #Tipo de dato datetime
fecha2 = datetime.datetime(2023, 4, 17) #Tipo de dato datetime

if fecha1 == fecha2:
    print("Nacieron el mismo día")
elif fecha1 > fecha2:
    print("El niño 1 es mayor que el niño 2")
else:
    print("El niño 2 es mayor que el niño 1")
