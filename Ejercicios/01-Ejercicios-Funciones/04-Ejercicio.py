'''
Escribir una función de dos argumentos reales a, b que calcule y regrese la raíz cuadrada de la suma de sus cuadrados, es decir, la longitud de la hipotenusa del triángulo rectángulo cuyos catetos tienen longitudes a, b. Sugerencia: en el lenguaje de programación elegido encontrar la función que calcula la raíz cuadrada.
Ejemplo. Entrada: 11, 27.5. Salida: 29.6184064392398.
'''

from math import *

def hipotenusa(a,b):
 
 num_1 = pow(a, 2)
 num_2 = pow(b, 2)

 resultado = sqrt(num_1 + num_2)

 return resultado


print(hipotenusa(11, 27.5))
