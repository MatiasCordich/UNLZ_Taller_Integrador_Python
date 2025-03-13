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