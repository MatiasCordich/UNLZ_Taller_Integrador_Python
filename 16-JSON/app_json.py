import json 

# Creo mi diccionario
dict_perrito_1 = {
    "nombre": "Pippo",
    "edad": 1
}

# json.dumps() convierte el diccionario a un STRING en formato JSON
# Sirve cuando queremos guardar el resultado en una variable o imprimirlo
json_perrito = json.dumps(dict_perrito_1)

# Escribimos el string JSON en nuestro archivo perrito1.json
with open("perrito1.json", "w") as f:
    f.write(json_perrito)

print("Fin de la primera ejecución")

# Creamos un 2do diccinario
dict_perrito_2 = {
    "nombre": "Chicho",
    "edad": 7
}

# json.dump() escribe directamente el diccionario en formato JSON dentro del archivo
# Es más directo si no necesitamos guardar el string antes
with open("perrito2.json", "w") as f:
    json.dump(dict_perrito_2, f)

print("Fin de la segunda ejecución")

'''
Diferencias:
- dumps(): convierte un diccionario a un string JSON.
- dump(): escribe directamente el diccionario en un archivo como JSON.

Importante: abrir un archivo en modo "w" borra el contenido anterior.
'''

