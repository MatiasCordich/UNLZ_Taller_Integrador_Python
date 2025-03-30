# ------------------------- [MODULO PERSONALIZADO] -------------------------
'''
Vamos a crear un módulo personalizado. 

Recordemos que los módulos son un conjunto de variables y funciones que podemos utilizar. 

'''

# Funcion para saludar

def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

# Funcion calculadora

def calculadora(num_1, num_2, basicas = False):

    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else: 
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        if(num_2 == 0):
            cadena += "ERROR: No se puede dividir por cero"
        else:
            division = num_1 / num_2
            cadena += "Division: " + str(division)
            cadena += "\n"
    
    return cadena

# Puedo hacer una función que me devuelva un diccionario 
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

# Funcion que me haga una sumatorio de un conjunto
def sumar_todos(ite) -> int:
    acum = 0

    for x in ite:
        acum += x  

    return acum 