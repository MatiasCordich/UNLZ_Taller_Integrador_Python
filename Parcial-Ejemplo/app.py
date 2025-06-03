from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Configuración de la base de datos 
app.config["nombre"] = "Parcial"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prueba.sql" 

db = SQLAlchemy(app)

ma = Marshmallow(app)

# A partir del siguiente modelo y schema, asumiendo que la base de datos ya se encuentra configurada, armar los endpoints solicitados:

# Esto es una Modelo a partir de SQLAlchemy
class Auto(db.Model):
    id = Column(int, primary_key=True)
    patente = Column( String(length=10))
    precio =Column(Float(asdecimal=True))
    velocidad = Column(Float() )

# Esto es un Schema a partir de Marshmallow
class AutoSchema( ma.Schema ):
    id = fields.Integer()
    patente = fields.String()
    precio = fields.Float()
    velocidad = fields.Float()

@app.route('/')
def hello():
    return 'Hello World!'

'''
1. autos/financiar/{patente} (GET)
 - Recibe una patente por parámetro de ruta y un presupuesto por argumento para retornar un json con los siguientes atributos:
    patente: la patente del auto.
    presupuesto: el presupuesto ingresado
    alcanza: un boolean determinando si el importe ingresado alcanza para comprar el auto
    precio: el precio del auto
    precio_cuotas: el 150% del precio.
'''

@app.route('autos/financiar/<patente>', methods=['GET'])
def financiar_auto(patente):
    
    # Obtengo el argumento que seria presupuesto esto seria autos/financiar/AXZ434?presupuesto=45656
    prespuesto = float(request.args.get('presupuesto'))

    # Obtengo un auto por medio de su patente. 
    auto = db.session.query(Auto).filter_by(patente = patente).first

    # Creo la respuesta en base al auto obtenido
    response = {
        "patente": auto.patente,
        "presupuesto": prespuesto,
        "alcanza":  prespuesto >= auto.precio,
        "precio": auto.precio,
        "precio_cuotas": auto.precio * 1.5
    }

    # Se responde con response donde lo convertimos a JSON
    return jsonify(response)

'''
2. autos/editar/{id}
 - Recibe la id de un auto y un json con precio y velocidad. Una vez hecho esto, edita dichos datos en el auto y retorna el objeto modificado ocultando su id.
    Requisito: Usar Marshmallow
'''
@app.route('autos/editar/<int:id>', methods=['POST'])
def method_name(id):

    # Obtengo un auto por su ID
    auto = Auto.query.get(id)

    # Leer el JSON que me da el frontend y lo transforma a diciionario
    data = request.get_json()

    # A los compos precio y velocidad de auto le agrego los traidos del json
    auto.precio = data["precio"]
    auto.velocidad = data["velocidad"]

    # Se realizan los cambios
    db.session.commit()

    # Se crea un nuevo Schema a partir de AutoSchema donde se oculte el ID. 
    schema = AutoSchema(only=["patente", "precio", "velocidad"])

    # Serialiamos el modelo Auto a un JSON
    return schema.dump(auto)


'''
3. autos/totales
 - Retorna un json con los siguientes atributos:
    promedio: promedio de precios
    minimo: el precio más bajo de autos.
    cantidad: la cantidad de autos registrados
'''

@app.route('autos/totales', methods=['GET'])
def method_name():

    # Obtengo todos los autos
    autos = db.session.query(Auto).all()

    # Inicio un array donde voy a guardar todos los precios de los autos 
    precios = []

    # Recorro el array de autos y en cada auto extraigo su precio y lo inserto en el array de precios
    for a in autos:
        precios.append(a.precio)

    # Realizo la suma total de precios
    suma = 0
    for p in precios:
        suma += p

    # Con la suma total de precios lo divido por la cantidad de autos de ahi sale el promedio. 
    promedio = suma / len(precios)

    # Calculo el minimo con la función MIN()
    minimo = min(precios)

    # Calculo la cantidad de autos con la funcion LEN()
    cantidad = len(autos)

    total = {
        "promedio": promedio,
        "minimo": minimo,
        "cantidad": cantidad
    }

    # Devolvemos el total y lo convertimos JSON
    return jsonify(total)



if __name__ == '__main__':
    app.run(debug=True)