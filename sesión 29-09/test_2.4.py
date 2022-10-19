"""Diccionarios en Python"""

varDiccionario = {"nombre": "Mysql", "tipo": "BD relacional"}

"""Convirtiendo diccionario a lista"""
list(varDiccionario)

print("Mi diccionario convertido es el siguiente: {}".format(list(varDiccionario)))

valores = list(varDiccionario.values())
print(valores)

keys = list(varDiccionario.keys())
print(keys)

lista_convertida = varDiccionario.items()
print(lista_convertida)
