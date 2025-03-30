# ------------------------- [FUNCIONES] -------------------------
'''
La funcion es un conjunto de intrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesaria. 

En Ptyhon las funciones tienen la siguiente estructura: 

def nombreDeMiFuncion(parametros):
    BLOQUE / CONJUNTO DE INSTRUCCIONES


nombreDeMiFuncion(mi_parametro)

'''

# Ejemplo 1 - FUNCION SIMPLE

# Definimos una funcion
def mostarNombre():
    print("Chicho")
    print("Sultan")
    print("Esculapio")

# Invocamos la funcion
mostarNombre()

# Ejemplo 2 - FUNCION CON PARAMETROS

# Definimos una funcion con parametros
def mostrarTuNombre(nombre_ingresado):
    print(f"Tu nombre es: {nombre_ingresado}")

#Invocamos la funcion y le pasamos un nonmbre com parametro
mostrarTuNombre("Paco")
mostrarTuNombre("Lucia")
mostrarTuNombre("Nestor")

# Tambien podemos hacer un programa sencillo donde podemos ingresar un nombre y mostrarlo
nombre = input("Introduce tu nombre: ")
mostrarTuNombre(nombre)

# Puedo utilizar la cantidad de parametros que sean necesarios y crear progrmas mas complejos
def mostrarColorYNumero(color_ingresado, numero_ingresado):

    # Mostrarmos el color que ingresamos por teclado
    print(f"El color ingresado es: {color_ingresado}")

    # Evaluamos el valor numerico ingresado si esta dentro del rango del 1 al 10
    if numero_ingresado <= 0 or numero_ingresado > 10:
        print("ERROR! Ha ingresado un número fuera del rango")
    else:
        print(f"El número ingresado es: {numero_ingresado}")

color = input("Introduce un color: ")
numero = int(input("Introduce un número del 1 al 10: ")) # Recordemos que tiene que ser int porque en la condicion se evaluan numeros

mostrarColorYNumero(color, numero)

# Ejemplo 3 - FUNCION CON PARAMETROS Y BUCLE

def multiplicarConTablas(numero_tabla):

    print("\n")
    print(f"---------- Tabla de multiplicar del numero:{numero_tabla} ----------")
    for contador in range(0,11): # El rango va ir desde el 1 hasta el 10
        operacion = numero_tabla*contador
        print(f"{numero_tabla} x {contador} = {operacion}")

multiplicarConTablas(3)

# Ejemplo 4 - USAR FUNCIONES DENTROD DE BUCLES 

# En el ejemplo anterior se ingresaba un numero por parametro y se hacia la tabla de ese numero ingresado, ahora podemos hacer tablas completas

for numero_tabla in range(1,11):
    multiplicarConTablas(numero_tabla) # Vamos a hacer las tablas del 1 al 10 con iteracion haciendo en totoal 10 tablas

# Funciones con parametros opcionales
'''
En Python, los parametros que ingrese son OBLIGATORIOS, es decir, si o si es necesario que se le pase un valor para que la funcio funcione correctamente. 

Pero se puede cambiar este comportamiento volviendo un parametro opcional, es decir, definirle un valor de entrada al parametro. De esta manera puedo optar por un valor por parametro o no en dicha funcion. 
'''

# Ejemplo 5 - Parmaetros opcionnaes

def mostararUsuario(nombre, dni = None):

    if dni == None:
        print(f"Bienvenidx {nombre}, eres invitadx")
    else: 
        print(f"Bienvenidx {nombre}, eres empleado, tu dni es {dni}")

mostararUsuario("Carlos", 23545678) # En este caso decido pasar dni como parametro
mostararUsuario("Ana") # En este caso decido no pasar el dni como parametro

# Uso del return 
'''
El return nos va a servir para poder devolver un valor en Python, hasta ahora solo hemos MOSTRADO resultados por consola. Con el return devolvemos un resultado. 

Al igual que en variables, en Python no es necesario especificiar que tipo de dato es el que devuelve. 
'''

# Ejemplo 6 - Return basico 
def sumar(a, b):
    return a + b

resultado = sumar(5,3)
print(resultado)

# Ejemplo 6.1 - Return de un diccioario

def info_numero(num):
 
 # Variable que transforma el numero ingresado a su doble
 d = num * 2

 # Validación por si ingresamos un numero positivo
 neg = num
 if num > 0:
   neg = num * (-1)

 resultado = {
     "original": num,
     "cuadrado": num**2,
     "doble": d,
     "es par": num % 2 == 0,
     "neg": neg 
 }

 return resultado

resultado_2 = info_numero(5)
print(resultado_2)



# Funciones dentro de otras de funciones
'''
Podemos definir funciones dentro de otras con el fin de poder orgarnizar mejor el codigo y limitar el alcance de una funcion auxiliar. Vamos con un ejemplo. 
'''

# Uso de funciones separadas
'''
En este caso vamos que se tiene que llamar a dos funciones por separado porque cada una hace una accion diferente. 
'''


def getNombre(nombre):
    texto = f"Tu nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Tu apellido es: {apellidos}"
    return texto

# Ejemplo 7 - Uso de funciones anidadas 
'''
En este caso creamos una funcion que va a encapsular a las otras dos funciones con el fin de realizar dos acciones a la vez. 
'''
def getNombreYApellido(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(getNombreYApellido("Fernado", "Alonso"))

# Funciones LAMBDA
'''
Una funcion LAMBDA es una funcion ANONIMA, es decir, es una funcion que no tiene nombre concreto y se definen en una sola linea. 

Para definirlas debemos utlizar la palabra reservada  lambda

Su sintaxis es la siguiente

lambda argumentos: expresion

Todo lo que venga despues de la palabra lambda es la funcion en si donde se divide en dos partes

los argumentos: Los argumentos que recibe esa funcion anonima
la expresion: Que vendria a ser el bloque de codigo simple de la funcion. 
'''

# Ejemplo 8 - Uso de una funcion lambda

dime_el_year = lambda year: f"El año es {year}"


print(dime_el_year(2025))