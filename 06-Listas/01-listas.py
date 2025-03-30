# ------------------------- [LISTAS] -------------------------
'''
En capítulos anteriores ya vimos que es una lista. Para recordar, una LISTA o ARRAY es una estructura de datos en la que una colección o conjnto de datos o valores se encuentran bajo un único nombre. 

En esta sección vamos a profundizar más en las listas trabajando en ellas. 
'''

# Definir una lista
pilotos = ["Leclerc", "Verstappen", "Norris", "Alonso", "Hamilton"] 

# Tambien podemos crear una lista a partir de su constructor
grandes_premios = list()

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

# Acceder a un elemento de la lista 
'''
Para poder acceder a un elemento de una lista en particular tenemos que tner en cuenta su número de índice y lo tenemos que hacer de la siguiente manera. 
'''

print(pilotos[1]) # Verstappen

'''
Tambien puedo acceder a los valores con números negativos, esto hace que acceda desde el último elemento 
'''

print(pilotos[-1]) # Hamilton


# Slicing. Acceder a varios elementos de una lista mediante un rango
'''
También puede seleccionar la cantidad de elemntos que quiera de mi lista a partir de especificarle un rango desde cúal índice hasta qué indice, como vemos a continuación.
'''

print(pilotos[:3]) # Muestra desde el inicio hasta el índice 3 (sin incluir el indice 3) ['Leclerc', 'Verstappen', 'Norris']

print(pilotos[2:4]) # Muestra desde el índice 2 hasta el índice 4 (sin incluir el 4) [Norris, Alonso]

print(pilotos[:-3])  # Muestra desde el inicio hasta el tercer elemento desde el final (sin incluirlo) ['Leclerc', 'Verstappen']

# Slicing con paso: [inicio:fin:paso]
'''
Tambíen podemos seleccionar la cantidad de elementos que queramos de mi lista y que, además, me los seleccione mediante pasos
'''
print(pilotos[::2])  # Muestra los elementos de la lista de dos en dos: ['Leclerc', 'Norris', 'Hamilton']

print(pilotos[1:3:2])  # Desde el índice 1 hasta el 3 (sin incluirlo), saltando de 2 en 2: ['Verstappen']

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