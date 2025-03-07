# ------------------------- [TIPOS DE DATOS] -------------------------
'''
Aunque Python sea un lenguaje de programación de tipado dinámico y, no haga falta especificar el tipo de dato a la variable, aun así posee distintos tipos de datos. Existen dos grandes categorias de tipos de datos que son los PRIMITIVOS y ESTRUCTURADOS.
'''


# 1- Tipos Primitivos: Son los tipos de datos más básicos, que almacenan un solo valor.

# Nulo: Representa una variable cuyo valor es nulo 
nada = None # None 
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

# 2- Tipos Estructurados: Permiten almacenar y organizar múltiples valores.

# Lista: Son colecciones ordenadas de elementos
lista = [1, 2, 3, "cuatro"]  
print(type(lista)) # list: Lista modificable
print("Lista:", lista)

# Tupla: Son lo mismo que las listas pero no cambian
tupla = (10, 20, 30)
print(type(tupla))  # tuple: Es una lista inmutable
print("Tupla:", tupla)

# Diccionario: Permiten almacenar pares clave-valor.
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

