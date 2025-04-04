# ------------------------- [TIPOS DE DATOS] -------------------------
'''
Python es un lenguaje que es fuertemente tipado PERO el lenguaje permite que no se declare explícitamente el tipo de dato, ya que, como dijimos anteriormente, cada variable tiene un tipo ASOCIADO al objeto al que apunta. 

Por eso, en Python no existen los tipos de datos primitivos, sino que cada valor es un instacia de una clase. 
'''

print("# -------------------------------------------------------------------")

# Nulo: Representa una variable cuyo valor es nulo 
nada = None # NoneType 
print(type(nada)) # Con la funcion type() podemos ver que tipo de dato es la variable
  
# Numéricos: Representan valores numéricos.
entero = 10  
print(type(entero)) # int: Número entero

flotante = 3.14  
print(type(flotante)) # float: Número decimal

complejo = 2 + 3j  
print(type(complejo)) # complex: Número complejo

print("Numéricos:", entero, flotante, complejo)

# Booleanos: Representan valores de verdadero o falso.
verdadero = True  
print(type(verdadero)) # bool: Valor verdadero

falso = False 
print(type(falso))  # bool: Valor falso

print("Booleanos:", verdadero, falso)

# Cadenas de texto: Representan secuencias de caracteres.
texto = "Hola, Python!"  
print(type(texto)) # str: Texto en comillas
print("Texto:", texto)

print("# -------------------------------------------------------------------")

# Lista: Son colecciones ordenadas de elementos. Las listas se guardan en memoria por lo que sus valores se guardan. 
lista = [1, 2, 3, "cuatro"]  
print(type(lista)) # list: Lista modificable
print("Lista:", lista)

# Tupla: Son lo mismo que las listas pero no cambian, no se pueden ordenar, modificar o lo que sea que altere su estructura.
tupla = (10, 20, 30)
print(type(tupla))  # tuple: Es una lista inmutable
print("Tupla:", tupla)

# Si yo hago una TUPLA de un solo elemento, Python lo va a entender como una variable para hacer una TUPLA de un solo elemento lo hago de la siguieente forma
tupla_2 = (2,) # Le agrego una coma
print(type(tupla_2))  # tuple: Es una lista inmutable
print("Tupla 2:", tupla_2)

# Diccionario: Permiten almacenar pares clave-valor. Su estructura es similar a la de un JSON

diccionario = dict()

diccionario["gato"] = "Felino chiquito de 4 patas"
diccionario["perro"] = "Animal que tiene cola, 4 patas y laddra"

valor = diccionario["perro"]

print(valor)
print(type(diccionario))  # dict: Pares clave-valor
print("Diccionario:", diccionario)

# Otra forma de definir un diccionar es con las llaves {}

numeros = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro, como los que se comió Brasil"
}

print(numeros[1])

# Rango: Es una secuencia de numeros donde le definimos un rango. Se crea una colección que va desde un numero hasta otro.  
rango = range(9) # 0,1,2,3,4,5,6,7,8
print(type(rango))  # range: rango de valores del 0 al 8 (más adelante veremos como imprimir todos los valores)
print("Rango:", rango)

# Le definimos un numero de inicio
rango_2 = range(2,6) # 2,3,4,5

# Le definimos numeros de inicio, fin y de salto
rango_3 = range(1,7,2) # 1,3,5

# Para poder ver el rango debemos hacer un bucle
for x in rango:
 print(x)

print("\n")
for x in rango_2:
 print(x)

print("\n")

for x in rango_3:
 print(x)

# Los rangos no guardan en memoria. Generan datos a demanda. 
rango_grande = range(0,99999999)

for n in rango_grande:
  if n % 10000000 == 0:
    print(n)

print("# -------------------------------------------------------------------")

# Funciones
'''
En Python tambien puedo asociar funciones a una variable, por ejemplo: si a la variable la asocio a la función print esta va a apuntar a la función y va a servir como un alias de la función. 
'''

mostrar = print  # La variable "mostrar" ahora apunta a la función print
mostrar("La llegaron las pipshassshh")  # Equivale a print("La llegaron las pipshassshh")

'''
¿Qué sucede realmente?

print en Python es un objeto de tipo función.

mostrar = print no copia la función, sino que hace que "mostrar" apunte a la misma función.

Ahora puedes llamar a mostrar() como si fuera print().
'''


