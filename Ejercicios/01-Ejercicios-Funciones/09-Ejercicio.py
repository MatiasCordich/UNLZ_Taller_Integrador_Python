'''
Dado un número entero no negativo x, devolver la suma de los últimos dos dígitos de x en el sistema decimal.
Sugerencia: usar el cociente y el resido al dividir entre 10.
Ejemplo. Entrada: 729. Salida: 11.
Ejemplo. Entrada: 688. Salida: 16.
Ejemplo. Entrada: 5. Salida: 5.
'''

from math import *

def suma_ultimos_dos_digitos(x):
 
 ultimo = x % 10
 penultimo = (x // 10) % 10
 resultado = ultimo + penultimo

 return resultado

print(suma_ultimos_dos_digitos(729))
print(suma_ultimos_dos_digitos(689))
print(suma_ultimos_dos_digitos(5))



