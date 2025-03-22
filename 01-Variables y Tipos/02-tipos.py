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

# Lista: Son colecciones ordenadas de elementos
lista = [1, 2, 3, "cuatro"]  
print(type(lista)) # list: Lista modificable
print("Lista:", lista)

# Tupla: Son lo mismo que las listas pero no cambian
tupla = (10, 20, 30)
print(type(tupla))  # tuple: Es una lista inmutable
print("Tupla:", tupla)

# Diccionario: Permiten almacenar pares clave-valor. Su estructura es similar a la de un JSON
diccionario = {
    "nombre": "Pepe", 
    "edad": 25
}
print(type(diccionario))  # dict: Pares clave-valor
print("Diccionario:", diccionario)

# Rango: Es una secuencia de numeros donde le definimos un rango 
rango = range(9)
print(type(rango))  # range: rango de valores del 0 al 9 (más adelante veremos como imprimir todos los valores)
print("Rango:", rango)

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


