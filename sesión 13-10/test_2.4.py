
"""Manejo de archivos"""

def fileManipulation(dir, mode):
    try:
        file = open(dir, mode)
        print(file.read())
        file.close()
        return file
    except OSError as err:
        print("Erro de lectura: {}".format(err))


fileWrite = "my_files/file_2.txt"

print("Lectura de un archivo")
fileManipulation(fileWrite, "r")

fileWrite2 = "my_files/append.txt"
fileManipulation(fileWrite2, "a+")
