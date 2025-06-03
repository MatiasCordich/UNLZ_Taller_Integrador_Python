import json
import requests # IMPORNTANTE: Tenemos que instalar el módulo resquest -> pip install requests

# Vamos a hacer una petición a una API

urlBase = "https://ferrari-api.onrender.com/ferrari" # La URL base de mi API

# Hacemos una petición GET para obtener un dinosaurio aleatorio
r = requests.get(f"{urlBase}/id/23") # Realizo la petición

print(r.text)