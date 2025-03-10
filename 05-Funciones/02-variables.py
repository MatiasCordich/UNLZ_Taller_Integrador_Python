# ------------------------- [VARIABLES] -------------------------
'''
Este apartado de variables se encuentra en la carpeta de 05-Funciones porque con las mismas podemos definir dos topos de variables:

Variables locales: Son la variables que se definen dentro de la funcion y no se pueden usar fuera de lla, su ciclo de vida empieza y termina dentro de la funcion, aunque podemos recuperar el valor de la misma si hacemos un return. 

Variables globales: Son las variables que se declaran fuera de la funcion y estan disponible tanto dentro como fuera de la misma. 

'''

# Ejemplo 1 - Variable GLOBAL

mensaje = "Hola, mundo"

def mostrarMensaje():
    print(mensaje) # Al ser global se puede usar dentro de una funcion

mostrarMensaje()

# Ejemplo 2 - Variable LOCAL

def saludar():
    saludo = "Hola" # Al ser local, solo va a existir dentro de la funcion
    print(saludo)

saludar()
# print(saludo)  # Error: "saludo" no está definida fuera de la función

# Ejemplo 3 - Recuperar el valor de una variable LOCAL

def mostrarFrase():
    texto = "Que lo demuestre!"
    return texto # Gracias al return, antes que la variable muera recuperamos el valor de la misma

print(mostrarFrase())

# Modificar variables globales dentro de una funcion
'''
Supongamos que tenemos el siguiente ejemplo
'''

contador = 0

def incrementar():

    # Le estamos diciendo a Python que esta variable ya existe y es global
    global contador 
    contador += 1

incrementar()
print(contador)  # Output: 1

'''
¿Porqué utilice esa palabra reservada?

Supongamos que no hubiesemos usado la palabra "global"

    contador = 0  --> Variable global

    def incrementar():
        contador += 1 --> Nos va a saltar ERROR del tipo UnboundLocalError

    incrementar()

Cuando Python ve contador += 1 dentro de la funcion está asumiendo que contador es una NUEVA VARIABLE LOCAL, pero como no fue inicializa aún va a lanzar un UnboundLocalError.

Por eso, en ejemplo correcto, al utilizar la palabra "global" le estamos diciendo a Python que la variable contador YA ES una variable global y que no hace falta crear una nueva varible local
'''