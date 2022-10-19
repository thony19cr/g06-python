"""Usando las propiedades de cadenas"""

"""Concatenación"""

nombre = "Luke"
apellido = "Skywalker"

nombreCompleto = "El nombre completo del primer usuario es: " + nombre + " " + apellido
print(nombreCompleto)

"""Usando el formato format"""
nombreCompleto2 = "El nombre completo del usuario es: {} {}".format(nombre, apellido)
print(nombreCompleto2)
