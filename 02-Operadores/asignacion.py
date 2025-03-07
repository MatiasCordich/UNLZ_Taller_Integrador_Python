# ------------------------- [OPERADORES ARITMÉTICOS] -------------------------
'''
Son los operadores que permiten darle un valor a una variable que pueden ser

- igual
- incremente
- decremento
- multiplica y asigna
- divide y asigna
- modulo y asingna
'''

# Igual: Le asigne que la variable numero sea IGUAL  al valor 55
a = 55

# Incremento
a += 5 # a = 55 + 5 = 60
print(a)

# Decremento
b = 20
b -= 10 # b = 20 - 10 = 10
print(b)

# Multiplica y asigna
c = 34
c *= 4 # c = 34 * 4 = 136
print(c)

# Divide y asigna
d = 87
d /= 5 # d = 87/5 = 17.4
print(d)

# Modulo y asigna
e = 23
e %= 9 # e = 23 % 9 = 5
print(e)


'''
Los contadores de incremento y decremento en Python en 1 en 1 NO EXISTEN en su forma simplificada como en otros lenguajes sí. Es decir, no existe esto en Python

a = 0

a++
a--

La unica forma valida sera 

a += 1
a -= 1
'''