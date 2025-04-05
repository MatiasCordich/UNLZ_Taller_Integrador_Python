import json 

# loads() toma un STRING en formato JSON y lo convierte en un diccionario de Python
# load() lee directamente desde un archivo JSON y lo convierte en un diccionario

# Abrimos el archivo, leemos el contenido como string y lo convertimos con loads()
with open("perrito1.json", "r") as f:
    json_perrin = f.read()
    p1 = json.loads(json_perrin)

print(p1["edad"]) # Mostramos la edad del primer perrito

'''
El problema con esto es que la variable p1 sigue existiendo despues de salir del bloque del with. Por lo que el scope, a Python, le da igual. 
'''

# Usamos load() directamente, sin necesidad de leer el archivo como string
with open("perrito2.json", "r") as f:
    p2 = json.load(f)  # Lee el archivo y lo convierte automáticamente a diccionario

print(p2["nombre"])
