# ------------------------- [LISTAS] -------------------------
'''
En capítulos anteriores ya vimos que es una lista. Para recordar, una LISTA o ARRAY es una estructura de datos en la que una colección o conjnto de datos o valores se encuentran bajo un único nombre. 

En esta sección vamos a profundizar más en las listas trabajando en ellas. 
'''

# Definir una lista
pilotos = ["Leclerc", "Verstappen", "Norris", "Alonso", "Hamilton"] 

# Las listas no tienen ninguna reestriccion 
estadísticas = ["Verde", 23, 4.4, True, "Texto"] 

print(pilotos)

'''
En la lista piloto, cada valor es un ELEMENTO. Donde cada elemento tiene un ÍNDICE donde se empieza a contar del 0. 

La lista piloto tiene 4 elementos donde:

Leclerc -> ÍNDICE 0
Verstappen -> ÍNDICE 1
Norris -> ÍNDICE 2
Alonso -> ÍNDICE 3
Hamilton -> ÍNDICE 4

'''

# Indices 
'''
Para poder acceder a un elemento de una lista en particular tenemos que tner en cuenta su número de índice y lo tenemos que hacer de la siguiente manera. 
'''

print(pilotos[1]) # Verstappen

'''
También puede seleccionar la cantidad de elemntos que quiera de mi lista a partir de especificarle un rango desde cúal índice hasta qué indice, como vemos a continuación.
'''

print(pilotos[2:4]) # [Norris, Alonso]
'''
Como vemos solo me trajo dos elemntos. Debemos creer que debería también incluir el elemento "Hamilton" que es el índice 4 pero tenemos que tener en cuenta esto:

- El primer índice es INCLUSIVO, es decir, se incluye dentro de lo que voy a recuperar de esa lista.
- El segundo índice es EXCLUYENTE, es decir, no se va incluir dentro de la información que se va a recuperar. Este índice sólo me indica el límite del rango de elemntos. 
'''

# Modificar un índice
rookies = ["Bearman", "Doohan", "Hadjar", "Bortoleto", "Antonelli", "Lawson"]

rookies[1] = "Colapinto"

print(rookies)

# Añadir un elemento a la lista
escuderias = ["Ferrari", "McLaren", "Mercedes", "Redbull", "Williams"]

'''
Para añadir un elemento a una lista debo utlizar el método append()
'''

escuderias.append("Racing Bulls")
escuderias.append("Aston Martin")

print(escuderias)

# Iterar una lista con un bucle FOR
print("----------- PILOTOS -----------")

for piloto in pilotos:
    print(f"{pilotos.index(piloto) + 1} - {piloto}")

'''
El método index() es un método que puedo utlizar en la lista con el fin de obtener el índice del elemnto. En el bucle por cada "piloto" me va a sacar su número de índice de la lista y le sumamos 1 para que la lista que me muestra se más natural
'''

# Iterando una lista con un bucle WHILE
'''
Vamos a hacer un programa donde vamos a ingresar más equipos de F1 y cuando escriba la palabra "parar" deje de introducir equipos y me muestra la lista. 
'''

nueva_escuderia = ""

while nueva_escuderia != "parar":
    nueva_escuderia = input("Introduce una nueva escudería: ")

    if nueva_escuderia != "parar":
        escuderias.append(nueva_escuderia)

print("----------- ESCUDERÍAS -----------")

for escuderia in escuderias:
    print(f"{escuderias.index(escuderia) + 1} - {escuderia}")

# Listas multidimensionales
'''
Una lista multidensional puede ocurrir por ejemplo cuando tenemso una lista de listas. 
'''

pilotos_ferrari = [
    ["Charles Leclerc", 16], # ÍNDICE 0
    ["Lewis Hamilton", 44] # ÍNDICE 1
]

# Acceder a un valor de la lista multidemnsional
'''
Supongamos que queremos acceDER al valor 16. Para eso debemos entender lo siguiente:

Primero tenemos que entender que nuestra lista pilotos_ferrari tiene 2 elementos que son sublistas:

pilotos_ferrari[0] → ["Charles Leclerc", 16]
pilotos_ferrari[1] → ["Lewis Hamilton", 44]

Dentro de pilotos_ferrari[0], el 16 está en la posición 1.

En resumen. 

En la lista pilotos_ferrari hay dos sublistas, primero debemos acceder a la sublista que se encuentra en el ÍNDICE 0

En dicha sublista, debemos acceder al elemento numérico 16 que está en el ÍNDICE 1. 

El primer índice [0] selecciona la primera lista, y el segundo índice [1] selecciona el número 16 dentro de ella.

'''

print(pilotos_ferrari[0][1]) # Salida: 16

# Recorrer esta lista multidimensinal

for piloto in pilotos_ferrari:  # Recorremos la lista principal
    print(f"Piloto: {pilotos_ferrari.index(piloto) + 1}")
    for dato in piloto:  # Recorremos cada elemento dentro de la sublista
        print(f"{dato}")