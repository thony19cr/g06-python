
"""Manejo de archivos"""

"""
    w: Abre el archivo para poder escribir sobre él
"""

file = open("my_files/file_2.txt", "w")

file.write("\n- Lenguaje multiplataforma\n")
file.write("- Basado en POO\n")
file.write("- Python es un lenguaje intuitivo")

file = open("my_files/file_2.txt", "r")

print("Nuestro 'file_2.txt' tiene el siguiente contenido: {}".format(file.read()))

"""Cierre del archivo"""
file.close()
