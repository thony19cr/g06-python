
"""Manejo de archivos"""

tecnologiasBackend = ["\nPython", "\nJava", "\nPHP"]

file = open("my_files/file_4.txt", "a+")

file.writelines(tecnologiasBackend)

file = open("my_files/file_4.txt", "r")

for newLine in file:
    #print(newLine)
    if newLine.find("Python"):
       print("Tienes en tu lista a Python")


"""Cierre del archivo"""
file.close()
