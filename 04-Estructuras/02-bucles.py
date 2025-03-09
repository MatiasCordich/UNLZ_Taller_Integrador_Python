# ------------------------- [BUCLES] -------------------------
'''
Los bucles son estructuras de control que permiten repetir un bloque de código múltples veces, se utilizan para poder automatizar tareas repetitivas y recorrer estructuras de datos como listas o cadenas. 

En Python tenemos dos tipos de bucles:
- WHILE: Se usa cuando no sabemos cuántas veces se repetirá el bucle, pero sí tenemos una condición de parada.
- FOR: Se usa cuando sabemos cuántas veces queremos iterar o recorremos alguan estructura como lista, lista, rango, etc.
'''

# Bucle while
'''Se ejecuta mientras la condición sea verdadera. Es útil cuando la cantidad de iteraciones no está definida.'''
contador = 0
while contador < 5:
    print("Contador:", contador)  # Imprime el valor de contador en cada iteración
    contador += 1  # Incremento para evitar un bucle infinito

# Bucle for
'''Se usa para iterar sobre una secuencia de valores. En este caso, recorre un rango de números.'''
for i in range(5):  # Itera de 0 a 4
    print("Valor de i:", i)  # Muestra cada número en la secuencia

# Bucle for con lista
'''Se usa para recorrer listas y acceder a cada elemento individualmente.'''
numeros = [10, 20, 30, 40]
for num in numeros:
    print("Número:", num)  # Muestra cada número de la lista

# Bucle for para strings
'''Permite recorrer cada carácter de una cadena de texto.'''
cadena = "Python"
for letra in cadena:
    print("Letra:", letra)  # Muestra cada letra de la palabra "Python"

# Uso de break
'''Se utiliza para salir del bucle antes de que la condición deje de ser verdadera.'''
i = 0
while i < 10:
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)
    i += 1  # Incremento en cada iteración

# Uso de continue
'''Salta la iteración actual y continúa con la siguiente sin ejecutar el código restante en esa vuelta.'''
for i in range(5):
    if i == 2:
        continue  # Omite la impresión cuando i es 2
    print("i:", i)  # Se imprimen todos los valores excepto el 2

# Uso de else en bucles
'''Es un bloque de codigo que solo se ejecuta solo si el bucle no se interrumpe con un break.'''
for i in range(3):
    print("i:", i)
else:
    print("Bucle completado sin interrupciones")  # Se ejecuta si el for finaliza sin interrupciones
