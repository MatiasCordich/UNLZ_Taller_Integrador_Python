# ------------------------- [EXCEPCIONES] -------------------------
'''
En Python podemos manejar los errores con el fin de poder capturar las excepciones ya que nuestro código es suceptible a los fallos. Veamos con un ejemplo sencillo.
'''

# Ingresamos un nombre

nombre = input("¿Cuál es tu nombre?: ")

'''
El problema está es que podemos ingresar un valor vacio, es decir, darle Enter de forma directa por lo que primero tenemos que validar que el nombre no sea algo vacío.
'''

#if len(nombre) > 1:
#    nombre_usuario = "El nombre es " + nombre

#print(nombre_usuario)

'''
El problema es que si no pasa la validación, voy a tener un error porque al no pasar la validación, la variable nombre_usuario no va a estar definida y vamos a tener un error del tipo NameError, para eso debemos capturar esa excepción, para eso debemos hacer lo siguiente:
'''

try:
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("ERROR! Necesitas introducir un nombre")

'''
Debemos usar la estructura que se llama try/except, que es muy parecida, en otros lenguajes, a la estructura try/catch pero con la diferencia que la excepción se llama except. 

Esta estructura se compone de 2 partes: 

- try: En esta estructra se "intenta" lo que dice el programa, en esta sección si todo sale bien el programa sigue su flujo de ejecución hasta el final. 

- except: Esta sección captura el error si se hizo algo en el try que no se debe hacer, se corta todo el flujo de ejecución y se ejecuta lo que haya en el except, en este caso muestra un mensaje de error más amigable al mensaje de error por defecto. 

En el except podemos también especificar qué tipo de error queremos capturar, en caso de no hacerlo el programa va a capturar todas las excepciones. 

Podemos usar la cantidad de except como sea necesario en base a las excepciones que queremos capturar. 


---------- ELSE Y FINALLY ----------

- Else. Este bloque se ejecuta como parte final cuando se ha terminado de ejecutar todo el programa SIN errores. 

- Finally. Este bloque se ejecutea también como parte final cuando se ha terminado de ejecutrar el programa con o sin errores. 
'''

# Uso del try/except/else/finally

try:
    num = int(input("Ingrese un número: "))
    resultado = 10 / num
except ValueError: # Capturamos el error de ingresar un caracter
    print("Entrada no válida. Debe ingresar un número.")
except ZeroDivisionError: # Capturamos el error de la división por cero
    print("¡No se puede dividir por cero!")
else:
    print(f"Resultado: {resultado}")  # Se ejecuta solo si no hay errores
finally:
    print("Ejecución finalizada.")  # Siempre se ejecuta

# Uso de excepcines para buscar una lista

# Lista de 10 números

numeros = [3, 7, 12, 18, -25, 33, -42, 56, 61, -78]

print("##### Búsqueda en la lista #####")

while True:
    try:
        # Solicitamos un número y lo convertimos a int
        busqueda = int(input("Introduce el número: "))
    except ValueError: # Capturamos la excepcion si ingresamos un valor no numerico
        print("Entrada no válida. Debes ingresar un número entero. Intente nuevamente.")
    else:
        print(f"Has introducido el número {busqueda}. Buscando en la lista...")
        try:
            # Buscar el índice del número en la lista
            search = numeros.index(busqueda)  
            print(f"¡El número {busqueda} existe en la lista! Está en la posición: {search}")
        except ValueError:  # Capturamos la excepcion si ingresamos un valor incorrecto
            print(f"El número {busqueda} no está en la lista.")
        else:
            print("Fin de la búsqueda.") # Mostramos el mensaje final si termino de ejecutarse correctamente
            break # Salimos del bucle una vez finalizado
       