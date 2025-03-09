# ------------------------- [OPERADORES DE IDENTIDAD] -------------------------
'''
Comparan si dos variables APUNTAN al mismo objeto en memoria (se aplica a cualquier tipo de variable, pero en tipos inmutables como enteros y cadenas puede haber optimización en caché).
Los operadores son 
- is
- is not
El valor de esta comparacion entre dos variables nos da como resultado final un valor BOOLEANO
'''

# Tenemos 3 variables

# a es una lista
a = [1, 2, 3]

# b apunta al mismo objeto que a
b = a  

# c es un objeto diferente aunque tiene los mismos valores
c = [1, 2, 3]  

print("a es b:", a is b)  # True (mismo objeto en memoria)
print("a es c:", a is c)  # False (diferente objeto en memoria)
print("a no es c:", a is not c)  # True (son diferentes en memoria)
