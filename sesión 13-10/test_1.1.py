
import json

class Empleado():

    def __init__(self, nombre):
        self.nombre = nombre

empleado = Empleado("Juan")

empleado1 = {"nombre": empleado.nombre}

print("nombre: {}".format(empleado1))

empleadoToJson = json.dumps(empleado1)

print("El dato de nuestra nueva variables es: {}".format(empleadoToJson))
