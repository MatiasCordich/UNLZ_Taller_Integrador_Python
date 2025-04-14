from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

#Recibe dos números (a y b) y retorna un JSON con el resultado de la suma. 
@app.route('/suma')
def suma():
    
    # Cramos los QUERY param
    a = request.args.get('a', type=int)
    b = request.args.get('a', type=int)

    # Creamos la estructura de la respuesta
    resultado = {
        "primero": a,
        "segundo": b,
        "suma": a + b
    }

    # Devolvemos la respuesta
    return resultado

# Recibe un número por parámetro de ruta y retorna un JSON con información sobre el número.
@app.route('/informacion/<numero>')
def analizar_numero(numero):

    # Convertimos el numero del parametro a int
    # Esto se hace así porque Flask no acepta números enteros negativos en la URL, para que pase sin ningún problema, primero le paso como string y después lo convierto a int. 
    numero_int = int(numero)

    # Validaciones
    es_positivo = False
    es_par = (numero_int%2==0)

    # Validacion del numero ingresado por parametro
    if numero_int > 0:
        es_positivo = True
    elif numero_int == 0:
        es_positivo = 0

    # Creamos el resultado 
    resultado = {
        "numero": numero_int,
        "doble": numero_int * 2,
        "positivo": es_positivo,
        "es par": es_par,
        "cuadrado": numero_int ** 2,
    }

    return resultado

# Recibe la base y la altura de un rectángulo por query params y retorna un JSON con sus propiedades.
@app.route('/rectangulo')
def rectangulo():

    # Creamos las QUERY params
    base = request.args.get('base', type=float)
    altura = request.args.get('altura', type=float)

    # Validaciones 
    son_iguales = (base == altura)
    es_alto = (altura > base)

    # Creamos el resutlado
    resultado = {
        "base": base,
        "altura": altura,
        "area": base * altura,
        "perimetro": 2*(base + altura),
        "cuadrado": son_iguales,
        "alto": es_alto,
    }

    # Devolvemos el resultado
    return resultado

# Recibe una palabra por parámetro de ruta y retorna un JSON con información sobre esa palabra.
@app.route('/palabra/<string:palabra>')
def analizar_palabra(palabra):
    
    # Validamos si la palabra empieza con vocal
    empieza_con_vocal = False

    if palabra[0].lower() in "aeiou":
        empieza_con_vocal = True

    resultado = {
        "palabra": palabra,
        "largo": len(palabra),
        "empieza_con_vocal": empieza_con_vocal,
        "mayuscula": palabra.isupper(), # Metodo para validar si la palabra esta toda en mayuscula
        "invertida": palabra[::-1] # Slicing: Se toma toda la cadena, -1 porque se empieza a recorrer desde el final
    }

    return resultado

# Recibe una palabra por parámetro de ruta y un número por query param(veces). Retorna un JSON con la palabra repetida la cantidad de veces indicada.
@app.route('/repetir/<string:palabra>')
def repetir_palagra(palabra):
    
    # Creo el QUERY param
    veces = request.args.get('veces', type=int)

    # Creo el resultado
    resultado = {
        "palabra": palabra,
        "veces": veces,
        "resultado": palabra * veces
    }

    # Devuelvo el resultado 
    return resultado

# Recibe un número por parámetro de ruta y un valor veces por query param. Retorna un JSON con la lista de potencias del número, desde el exponente cero hasta el exponente indicado. Para calcular potencias en Python pueden usar el operador **.
@app.route('/potencias/<int:numero>')
def potencias(numero):
    
    # Creamos el QUERY param
    veces = request.args.get('veces', type=int)

    # Creamos el array donde van a estar los resutlados de potenciar el numero ingresado
    elementos = []

    # range(0, veces + 1) asegura que el bucle repita la operación la cantidad de veces que le pedimos. 
    # El rango no incluye el número final, por eso sumamos 1. 
    for i in range(0,veces + 1): 
        elementos.append(numero ** i)

    # Creamos el resultado
    resultado = {
        "elementos": elementos,
        "cantidad": len(elementos) # Cantidad de elementos que tiene la lista
    }

    return resultado
if __name__ == '__main__':
    app.run(debug=True)