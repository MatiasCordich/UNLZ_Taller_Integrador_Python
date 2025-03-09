# ------------------------- [CONDICIONALES] -------------------------
'''
Los condicionales son estructuras que se encargan controlar el flujo del programa en base a condiciones. 

La estructura basica de un if en Python es la siguiente. 

if se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
else:
    Se ejecutan otro grupo de instrucciones.

Las condiciones que se realizan se realizan por medio de los OPERADORES DE COMPARACION
'''

# Ejemplo 1 - If simple

color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("CORRECTO! Mi color favorito es el ROJO")
else:
    print("Colo INCORRECTO!")

# Operadores de comparacion
'''
Como mencionamos, el resultado final de utilizar los operadores de comparacion son los BOOLEANOS.
Con los valors booleanos podremos realizar condicioanales. 
'''
a = 10
b = 20
print(a < b)  # Menor que TRUE (Excluye el valor de A)
print(a > b)  # Mayor que FALSE (Excluye el valor de A)
print(a == b) # Igual que FALSE
print(a != b) # Diferente que TRUE
print(a <= b) # Menor o igual que TRUE (Incluye el valor de A)
print(a >= b) # Mayor o igual que FALSE (Incluye el valor de A)

if a < b:
    print("a es menor que b")
else:
    print("a no es menor que b")

# Condicionales anidados
'''
Evaluan varias condiciones dentro de un mismo bloque. Su estructura seria.

if condicion_1:

    # Codigo que se ejecuta de condicion_1
    if condicion_2:
    
        # Codigo que se ejcuta de condicon_2
        if condicion_3
            Ejecutar codigo condicion_3
        else:
            Ejecutar este otro codigo condicion_3

    else:
        Ejecutar otro codigo de condicion_2

else:
    Ejecutar otro codigo de condicion_1

'''

# Ejemplo 2 - If anidados

nombre = "Sultan"
animal = "perro"
pais = "Argentina"
edad = 2
adultez = 6

# Primera condicion: Si el animal es perro o no
if animal == "perro":
    print(f"{nombre} es un perro")

    # Segunda condicion (anidada): El perro es adulto o no
    if edad >= adultez:
        print(f"{nombre} es un perro un adulto")

        # Tercera condicion (anidada): El perro es argentino o no
        if pais >= "Argentina":
            print(f"{nombre} es un perro adulto ARGENTINO")
        else:
            print(f"{nombre} es un perro adulto pero no es argentino")
    else:
        print(f"{nombre} NO es perro un adulto")
else:
     print(f"{nombre} NO es un perro")

# Ejemplo 3 - Elif
'''
En ejemplo anterior teniamos 2 ifs anidados donde ya empezaba a ser un problema de estructura. 

Tener muchos ifs anidados puede ser un problema. ya que despues podemos tener problemas con la identicacion haciendo que nuestra estructura sea muy dificil de mantener. 

Para eso tenemos una estructura con el fin de poder evaluar multiples condiciones que es el ELIF. Su estructura es la siguiente

if condicion_1:
    bloque de codigo
elif condicion_2:
    bloque de codigo
elif condicion_3:
    bloque de codigo
elif condicion_4:
    bloque de codigo
elif condicion_5:
    bloque de codigo
else:
    bloque de codigo

Esta estructura es muy parecida a la estructura SWITCH ya que en Python esa estructura no existe y su equivalente es ELIF.

'''

dia = int(input("Introduce un numero de la semana: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sabado")
elif dia == 7:
    print("Es Domingo")
else:
    print("ERROR ha ingresado un numero invalido")

# Ejemplo 4 - Operadores logicos y multiples condiciones
'''
Vimos los operadores logicos que son AND y OR que se utilizan para poder evaluar multiples condiciones. 
'''

d = 25
e = 30

# and - Ambas condiciones TRUE
if d > 20 and e > 25:
    # Ambos condiciones son TRUE
    print("Ambas condiciones son verdaderas por lo que la condicion general es VERDADERA")

# and - Una condicinoes es FALSE
if d < 20 and e > 25:
    # Ambas condiciones deben ser TRUE (en este caso no)
    print("Ambas condiciones son verdaderas por lo que la condicion general es VERDADERA")
else: 
     # La condicion d > 20 es FALSE con eso ya podemos concluir que la condicion general es FALSE
    print("Al menos una condicion es falsa por lo que la condicion final es FALSA")

# or - Una condicion al menos es TRUE
if d > 20 or e < 25:
    # La condicion d > 20 es TRUE por lo que la condicion general es TRUE aunque la condicion e < 25 sea FALSE
    print("Al menos una de las condiciones es verdadera por lo que la condicion general es VERDADERA")

# not - Cambia el vaor booleano de la condicion
if not(d < 20):
    # d < 20 en realidad es FALSE pero el NOT invierte el valor a TRUE
    print("El valor booleando ha sido cambiaod a TRUE")