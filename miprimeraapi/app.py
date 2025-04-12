from flask import Flask, request

# Creamos un objeto de tipo Flask y le pasamos la ubicación actual (__name__)
# __name__ es una variable que viene con FLASK, esta variable va a contener la ubicación del archivo donde estamos parado y se está ejecutando. 
app = Flask(__name__)


# Especificamos la ruta donde se va a ejecutar la lógica. Si usamos '/' esto quiere decir que es la ruta principal. 
@app.route('/')
def get_hola():
    return 'Hola, che. ¿Cómo andas? -> <button> CLICK AQUÍ </button>'

# Ruta que devuelve un diccionario Python (Flask lo convierte automáticamente a JSON)
@app.route("/dinosaurio")
def get_dinosarui():
 dino = {"nombre" : "T-Rex", "dieta": "Carnivoro"}
 return dino

# Otra forma de devolver JSON, esta vez escribiendo el string manualmente
@app.route('/dino2')
def get_dino2():
    return '{"nombre" : "T-Rex", "dieta": "Carnivoro"}'

# Ruta que devuelve una lista de números y un código de estado HTTP (402)
@app.route('/numeros')
def get_numeros():
    lista = []
    for i in range(20):
        lista.append(i)

    # Si yo quiero devolver una TUPLA debo devolver nó solo el contenido BODY, sino también el STATUS o el HEADER , al menos dos elementos. 
    return (lista, 402)
     
# Ruta dinámica con parámetro tipo entero en la URL
# Mediante el uso de <type:nombre_param> podemos especificar que tipo de dato va a ser el parámetro que le pasemos por la URL. Aunque de primeras siempre le pasemos un string, con esto convertimos el parametro. 
@app.route('/doble/<int:numero>')
def doblete(numero): # El parametro de la función la obtengo del PARAM
    return {"Original" : numero, "Doble": numero * 2}

# Ruta que usa parámetros por query string. Ejemplo: /multiplicar/5?por=3
@app.route('/multiplicar/<int:numero>')
def multiplicar(numero): # El parametro de la función la obtengo del QUERY PARAM

    # Obtenemos todos los parámetros enviados por query string.
    parametrosQuery = request.args

    # Convertimos el valor del parámetro 'por' a entero.
    multiplicar_por = int(parametrosQuery["por"])

    # Devolvemos un JSON con el número original y su resultado multiplicado.
    return {"Original" : numero, "Multplicado": numero * multiplicar_por}

# Como repetimos anteriormente, si estamos ejecutando el archivo main entonces corremos nuestro servidor. De paso le decimos que mientras corra nos debugge la ejecución. 
if __name__ == '__main__':
    app.run(debug=True)