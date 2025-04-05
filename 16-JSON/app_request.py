import json
import requests # IMPORNTANTE: Tenemos que instalar el módulo resquest -> pip install requests

# Vamos a hacer una petición a una API

urlBase = "https://dinosaur-facts-api.shultzlab.com" # La URL base de mi API

# Hacemos una petición GET para obtener un dinosaurio aleatorio
r = requests.get(f"{urlBase}/dinosaurs/random") # Realizo la petición

status = r.status_code # Con esto obtengo el status HTTP de la petición
contenido = r.text # Me va a dar todo el contenido de la peticion guardado como un string

print(status) # Si me devuelve un 200 significa que está todo bien
print(contenido) 


# Convertimos el string JSON a un diccionario de Python
dino = json.loads(contenido)

print(dino["Name"])