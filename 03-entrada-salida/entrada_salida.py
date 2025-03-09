# ------------------------- [ENTRADA Y SALIDA DE DATOS] -------------------------
'''
Desde que comenzamos, siempre hemos utilizado una funcion para la salida de datos que es la funcion print()

Pero,tambien, existe una función que nos permite poder ingresar datos que es la función input()

Veamos el ejemplo a continuacion
'''

'''
RECOMENDACION: EJECUTEN ESTE ARCHIVO DESDE LA TERMINAL DE WINDOWS
'''
# Variable nombre que va a guardar un valor de entrada, es decir, lo que escribamos por tecaldo
nombre = input("Hola, ¿cual es tu nombre?: ")
edad = input("¿Cuantos años tenes?: ")
print(f"Te doy la bienvenida {nombre}, veo que tenes {edad} años")

# Manipular valores que ingresamos 

'''
Supongamos que queremos hacer una conversion entre el año gregoriano y el año nuevo chino
'''

# Variable nombre que va a guardar un valor de entrada, es decir, lo que escribamos por tecaldo
año_gregoriano = input("Ingrese un año: ")

'''
Este ejemplo que vemos nos va a dar eror porque, como vemos, aunque hayamos ingresado un numero, el valor que ingresemos por teclado 
va a ser de tipo string y es incompatible hacer una operacion aritmética entre un string y un numero. 
'''
#print(f"El año ingresado es {año_gregoriano}, lo que en China sería el año chino {año_gregoriano + 2698}")

# Ejemplo correcto. Debemos convertir el valor ingresado a tipo int
print(f"El año ingresado es {año_gregoriano}, lo que en China sería el año chino {int(año_gregoriano) + 2698}")