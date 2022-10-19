"""Uso de la librería JSON para tratar tipos de datos JSON"""

import json

"""Uso de la librería JSON"""

jsonData = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'

"""Convirtiendo a un dato manejable para Python: loads()"""

jsonToPython = json.loads(jsonData)

print("Nuestro dato tipo JSON a dato para Python es: {}".format(jsonToPython))
print("El tipo de dato de nuestra variable es: {}".format(type(jsonToPython)))
