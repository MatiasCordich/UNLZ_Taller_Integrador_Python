'''
Dado un número entero x, regresar el resto al dividir x entre 7.
Sugerencia: encontrar la operación o la función correspondiente en el lenguaje de programación elegido.
Ejemplo. Entrada: 17. Salida: 3.
Ejemplo. Entrada: −40. Salida: 2.
Ejemplo. Entrada: 35. Salida: 0.
'''

from math import *

def resto_de_siete(x):
 
 resultado = x % 7

 return resultado

print(resto_de_siete(17))
print(resto_de_siete(-40))
print(resto_de_siete(35))



