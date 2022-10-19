
"""Manejo de archivos"""

tecnologiasBackend = ["\nPython", "Java", "Ruby", "NodeJS"]
tecnologiasFrontend = ["\nAngular", "Javascript", "React JS", "Boostrap"]

"""Apertura de nuestro archivo
    a+: Permite escribir varias líneas en nuestro archivo
    a+: Escribe nuevas líneas de texto sin sobreescribir el contenido del archivo
"""

file = open("my_files/file_3.txt", "a+")

file.writelines(tecnologiasBackend)
file.writelines(tecnologiasFrontend)

file = open("my_files/file_3.txt", "r")

print("El contenido de mi archivo file_3.txt es: {}".format(file.read()))

"""Cierre del archivo"""
file.close()
