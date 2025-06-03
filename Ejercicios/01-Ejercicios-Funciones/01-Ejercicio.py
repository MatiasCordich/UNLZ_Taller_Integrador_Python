from math import *

'''
Escribir una función de un argumento entero a que calcule y regrese el cubo de a.
Ejemplo. Entrada: −11. Salida: −1331.
Ejemplo. Entrada: 5. Salida: 125.
'''

def obtener_cubo(a):
 resultado = a ** 3
 return resultado

print(obtener_cubo(-11))
print(obtener_cubo(5))


def cubo(a):
 resultado = pow(a, 3)
 return resultado

print(cubo(-11))
print(cubo(5))
'''
Dados dos números enteros, regresar la suma de sus cubos. Sugerencia: usar la función programada en el Ejercicio Fun0.
Ejemplo. Entrada: 3, −12. Salida: −1701.
Ejemplo. Entrada: 15, −14. Salida: 631.
'''

def sumar_de_cubos(a, b):
 num_1 = obtener_cubo(a)
 num_2 = obtener_cubo(b)
 resultado = num_1 + num_2
 return resultado

print(sumar_de_cubos(3, -12))
print(sumar_de_cubos(15, -14))


