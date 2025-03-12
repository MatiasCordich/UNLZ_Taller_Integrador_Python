# ------------------------- [Diccionario] -------------------------
'''
Es otra estructura de datos que es muy similar a la lista pero en lugar de tener un ÍNDICE numérico va a tener índices alfanúmericos.

Su similitud, con respecto a otros lenguajes, es con un ARRAY ASOCIATIVO o un OBJETO JSON.
'''

piloto = {
    "nombre": "Fernado",
    "apellido": "Alonso",
    "edad": 43,
    "numero": 14,
    "escuderia": "Aston Martin",
    "campeonatos": [2005,2006] 
}

print(piloto)
print(type(piloto))

# Acceder a los valores del diccionario

print(piloto["nombre"])
print(piloto["apellido"])
print(piloto["edad"])
print(piloto["numero"])
print(piloto["escuderia"])
print(piloto["campeonatos"])

# Si queremos acceder a los valores de una lista dentro de un diccionario
print(piloto["campeonatos"][0]) # 2005
print(piloto["campeonatos"][1]) # 2006

# Lista de diccinario
'''
Tambien podemos hacer una lista de diccionarios donde nos quedara de la siguietne forma
'''

pilotos = [
    {
        "nombre": "Fernando",
        "apellido": "Alonso",
        "edad": 43,
        "numero": 14,
        "escuderia": "Aston Martin",
        "campeonatos": [2005, 2006]
    },
    {
        "nombre": "Lewis",
        "apellido": "Hamilton",
        "edad": 40,
        "numero": 44,
        "escuderia": "Ferrari",
        "campeonatos": [2008, 2014, 2015, 2017, 2018, 2019, 2020]
    },
    {
        "nombre": "Max",
        "apellido": "Verstappen",
        "edad": 27,
        "numero": 1,
        "escuderia": "Red Bull",
        "campeonatos": [2021, 2022, 2023, 2024]
    }
]

# Acceder a un valor especifico - Supongamos que queremos acceder al valor "Ferrari" 

# Acceder al valor "Mercedes"
escuderia_hamilton = pilotos[1]["escuderia"]
print(escuderia_hamilton)  # Output: Ferrari

'''
Lo que se hizo fue lo siguiente:
- Primero se accedo al índice del diccionario, en este caso piltos[1]
- Una vez que accedí al diccinario debo acceder a la índice cuyo valor es "Ferrari" que es el "escudería".

Entonces me quedaría como en el ejemplo donde primero accedemos por índice y después por clave.
'''

# Recorrer la lista de diccionarios 
print("---------------------------------")
for piloto in pilotos:
    print(f"Nombre: {piloto['nombre']}")
    print(f"Apellido: {piloto['apellido']}")
    print("---------------------------------")