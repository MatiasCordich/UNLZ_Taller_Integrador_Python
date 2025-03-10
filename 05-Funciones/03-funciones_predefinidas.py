# ------------------------- [FUNCIONES PREDIFINIDAS] -------------------------
'''
Al igual que cualquier lenguaje de programacion. 
Python tambien tiene funciones predefinidas que ya vienen con el lenguaje. A continuación se veran alguna de las funcines más comunes. 
'''

# Funciones de entrada y salida. Estas funciones ya las conocemos que son print() e input()

print("Hola, mundo!")

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# Funcion type(). Nos dice el tipo de dato que es la funcion
print(type(nombre))

# Conversión de tipo. Estas funciones ya las conocemos, son las funciones que se encargan de castear el tipo de dato de una variable que pueden ser str(), int() y float()
edad = "25"
edad_int = int(edad)
print(type(edad_int))  # Resultado: <class 'int'>

# Funcion isinstance(). Esta funcion nos permite determinar si el valor de una variable es de un tipo determinado. Su valor final sera un BOOLEANO.

'''
La función isinstance() recibe dos parametros que son: 
- La variable en sí con su valor
- El tipo de dato que queremos comprobar

En el ejemplo siguiente vemos lo siguiente:
- En el 1er parámetro usamos la variable nombre. 
- En el 2do parámetro usamos un tipo en este caso str. 

Con esto estamos diciendo si el valor de la variable nombre es de tipo string. 
Si es así entonces el valor será TRUE caso contrario será FALSE
'''
comprobar = isinstance(nombre,str) 

if comprobar:
    print("Esa variable es de tipo string")
else:
    print("Esa variable NO es de tipo string")

# Funcion round(). Esta funcion nos permite redondear un numero decimal y podemos decidir con cuantos decimales. 
'''
La función round() recibe dos parametros que son: 
- La variable de tipo decimal
- La cantidad de decimales que queremos redondear

En el ejemplo siguiente vemos lo siguiente:
- En el 1er parámetro usamos la variable numero. 
- En el 2do parámetro le indicamos cuantos decimales va a tener en este caso 2. 
'''
numero = 3.14159
print(round(numero, 2))  # Resultado: 3.14

# Funcion strip(). Esta función la se encarga de limpar los espacio de un string
frase = "      mi contenido       "
print(frase)
print(frase.strip())

# Funcion upper() y lower(). Convertir a mayúsculas y minúsculas
texto = "Hola Mundo"
print(texto.upper())  # Resultado: "HOLA MUNDO"
print(texto.lower())  # Resultado: "hola mundo"

# Funcion split(). Dividir un string en una lista
frase = "manzana, banana, cereza"
lista_frutas = frase.split(", ")
print(lista_frutas)  # Resultado: ['manzana', 'banana', 'cereza']

# Funcion join(). Unir una lista de strings en un solo string
frutas = ["manzana", "banana", "cereza"]
fruta_unida = ", ".join(frutas)
print(fruta_unida)  # Resultado: "manzana, banana, cereza"

# Funcion find(). Esta funcion se encarga de encontrar caracteres en un string
frase = "El aplauso señores"
print(frase.find("señores")) 
'''
Esta funcion me devuelve un entero. En ejemplo anterior me devuelve el valor 11. 

Eso es porque cuenta todos los caracteres (incluido los espacios). Del caracter E hasta el segundo espacio hay 11 caracteres. Despues de ahí se encuentra la palabra que buscamos. 

Si no encuentra la palabra nos devuelve -1
'''

# max() y min(). Estas funciones nos permiten encontrar el valor máximo y mínimo de la lista
numeros = [10, 20, 5, 30]
print(max(numeros))  # Resultado: 30
print(min(numeros))  # Resultado: 5

# sum(). Esta funcion nos permite sumar todos los elementos de la lista
suma = sum(numeros)
print(suma)  # Resultado: 65

# sorted() Ordenar una lista
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Resultado: [5, 10, 20, 30]

# Crear diferentes colecciones
mi_lista = list((1, 2, 3))  # Convierte tupla en lista
mi_tupla = tuple([1, 2, 3])  # Convierte lista en tupla
mi_set = set([1, 2, 2, 3])  # Elimina duplicados
mi_dict = dict(a=1, b=2)  # Diccionario

# map(). Esta funcion va a recorrer la lista y va a modificar sus valores de cada elemento de la misma. Utilizamos la expresion lambada
numeros_2 = [1, 2, 3, 4]
cuadrados = map(lambda x: x**2, numeros_2)
print(list(cuadrados))  # Resultado: [1, 4, 9, 16]

# filter(). Esta funcion va a recorrer la lista y nos va a devolver una lista filtrada en base a un criterio. Utilizamos la expresion lambda. 
numeros_3 = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros_3)
print(list(pares))  # Resultado: [2, 4, 6]
