'''
Dados tres números a, b, c, regresar la longitud de la diagonal del paralelogramo cuyos lados tienen longitudes a, b, c.
Entrada: −2.5, 0.3, −1.9. Salida: 3.1532620591175.
'''

from math import *

def diagonal_parelelogramo(a,b,c):
 
 # Calcula el angulo C en radianes
 c_rad = radians(c)

 # Calcular la diagonal 
 resultado = sqrt(pow(a,2) + pow(b,2) + 2*a*b*cos(c_rad))

 return resultado

print(diagonal_parelelogramo(-2.5,0.3,-1.9))




