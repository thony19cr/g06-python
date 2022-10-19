
# https://pokeapi.co/api/v2/pokemon/charizard

# 200: OK
# 404: error de permisos
# 500: Error de conexión con el servidor

import requests as rq

# https://pokeapi.co/
res = rq.get("https://pokeapi.co/api/v2/pokemon/charizard")

print(res.status_code)
print(res.headers)

json = res.json()
print("JSON: {}".format(json))
