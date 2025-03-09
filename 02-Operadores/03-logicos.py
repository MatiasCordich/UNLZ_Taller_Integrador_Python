# ------------------------- [OPERADORES LOGICOS] -------------------------
'''
Estos operadores se usan en las estructuras condicionales. 
Se centran en combinar dos o más comparaciones y, dependiendo del operador, nos dará un valor booleano. 

- and: Todas las condiciones deben ser verdaderas, en caso de que na no la sea entonces el valor final sera FALSE
- or: Con que una condición ya sea verdadera, el valor final sera TRUE.
- not: Invierte el valor final de la comparación
'''

x = 10
y = 3

# AND
'''
Tenemos dos comparaciones: 

x > 5 -> Esta comparacion es TRUE
y < 5 -> Esta comparaciion es TRUE

Al utilzar el AND estamos uniendo estas dos comparaciones y como ambas comparaciones dan TRUE el valor final sera TRUE
'''
print("AND:", x > 5 and y < 5)  # True

# OR
'''
Tenemos dos comparaciones: 

x > 15 -> Esta comparacion es FALSE
y == 3 -> Esta comparaciion es TRUE

Al utilzar el OR estamos uniendo estas dos comparaciones, aunque la primera comparacion de FALSE, la segunda da TRUE entonces el valor final sera TRUE.
'''
print("OR:", x > 15 or y == 3)  # True

#NOT
'''
Tenemos dos comparaciones: 

x > y -> Esta comparacion es TRUE

Este es el unico operador que funciona como funcion.

Esta comparacion da TRUE pero al utilizar el NOT() lo que hacemos el cambiar el valor contrario por lo que el valor final sera FALSE. 
'''
print("NOT:", not(x > y))  # False