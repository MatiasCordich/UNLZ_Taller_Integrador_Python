# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [VARIABLES] -------------------------
'''
Como mencionamos anteriormente, Python es un lenguaje de programación cuyo tipado es DINÁMICO, es decir, NO es necesario declarar el tipo de una variable; el tipo de variable se determina en tiempo de ejecución. 
'''

variable = 10  # x es un entero
variable = "Hola"  # Ahora x es una cadena

print(variable) # Cuando se ejecute se va a ejectuar el ultimo valor asigna de x

'''
También podemos crear múltiples variables y asignarles a cada una de ellas una valor específico separándolas por comas como vemos en el siguiente ejemplo
'''
# Variables múltiples en una sola línea
x, y, z = 10, 20, 30 
print("Valores:", x, y, z) # Como vemos a la variable x se le asigna el valor 10, y el valor 20 y z el valor 30

'''
También podemos crear múltiples variables y asignarles el mismo valor a cada una de ellas como se muestra en el siguiente ejemplo. 
'''
# Asignación del mismo valor a múltiples variables
a = b = c = 100
print("Mismo valor:", a, b, c) # Como vemos, creamos las variables a,b y c. A cada una le dimos un valor en comun que es 100

# Buenas prácticas para nombrar variables
"""
- Usar nombres descriptivos (ej: nombre_usuario en vez de x)
- No comenzar con números (Ejemplo incorrecto: 1nombre)
- Usar snake_case para nombres de variables (ej: mi_variable)
"""






