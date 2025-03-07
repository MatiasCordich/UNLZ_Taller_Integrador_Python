# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [COMENTARIOS EN PYTHON] -------------------------

# La primera forma de comentar en Python es utilizando el símbolo numeral (#). Esto va a hacer que se comente cada línea de forma individual. 

'''
Otro método alternativo es utilizar las comillas simples triples, aunque oficialmente no son comentarios de bloque, a menudo, se utilizan para poder comentar varias líneas de código. 
'''

# ------------------------- [IMPRIMIR POR CONSOLA] -------------------------

# En Python utilizamos la función print() para poder imprimir en la consola ya sea un texto, números y variables.
print("Hola, mundo!")

# Podemos imprimir más de un valor, para eso debemos utilizar la CONCATENACIÓN donde podemos hacerlo de dos formas. 

mascota = "perro"
nombre = "Chicho"


# 1ra forma de Concatenación: UNIÓN
print(mascota + " " + nombre)

# 2da forma de Concatenación: INTERPOLACIÓN
print(f"{mascota} {nombre}") 

# Gracias a la interpolación tambien podemos insertar valores en un string
print(f"Mi {mascota} se llama {nombre}") 


# ------------------------- [SINTAXIS] -------------------------

'''
La sintaxis de Python es una de las más sencillas, las características que la hacen como tal son:
    - No se usan llaves {} para bloques de código
    - No es necesario el uso del punto y coma (;)
    - La IDENTACIÓN es fundamental en Python

if True:
    print("Este bloque está indentado correctamente")  <--- Se debe usar la misma indentación

Error si la indentación es incorrecta:

if True:
print("Error de indentación") <--- ERROR de identaci[on]

'''