'''
Dado un número real estrictamente positivo, regresar su raíz cúbica. Sugerencia: usar exp y log.
Ejemplo. Entrada: 65. Salida: 4.02072575858906.
Ejemplo. Entrada: 1000. Salida: 10.0000000000000.
'''

from math import *

def raiz_cubica(x):
 
 if x > 0:
   resultado = exp(log(x)/3)
 else:
   print("ERROR ingrese un numero positivo")

 return resultado

print(raiz_cubica(65))
print(raiz_cubica(1000))




