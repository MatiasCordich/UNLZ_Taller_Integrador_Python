import json
import requests

# Vamos a hacer una petición que nos traiga un vector de Dinosaurios

urlBase = "https://dinosaur-facts-api.shultzlab.com" # La URL base de mi API

# Hacemos una petición GET para obtener la lista de dinosaurios
r = requests.get(f"{urlBase}/dinosaurs") 

# Convertimos automáticamente la respuesta JSON en una lista de diccionarios
lista_dinos:list = r.json()

# Recorremos la lista y mostramos los datos de cada dinosaurio
for dino in lista_dinos:
 print("Nombre: " + dino["Name"])
 print("Description: " + dino["Description"])
 print("--------------------------------------")