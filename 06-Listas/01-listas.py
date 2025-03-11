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