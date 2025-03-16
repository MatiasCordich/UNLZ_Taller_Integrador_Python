# ------------------------- [ENCAPSULAMIENTO] -------------------------
'''
Nuestra clase Coche está cumpliendo con los pilares de POO. 

Ahora bien, nosotros tenemos métodos GETTERS con el fin de poder obtener el valor de un atributo. 

El problema es que todavía podemos acceder de forma directa a las propiedades de un objeto mediante el uso del punto (coche.color)

Para eso debemos utilizar lo que se llama ENCAPSULAMIENTO, es decir, definir los atributos de la clase como algo PRIVADO para que no se pueda acceder de forma directa, sólo se puede acceder con los GETTERS. Lo hacemos de la siguiente forma.

Además no vamos a definir valores por defecto a los atributos, vamos a definirlos directamente en el constructor. 
'''


class Coche: 

    # CONSTRUCTOR - Es el primer metodo que vamos a crear en nuestras clases, la estructura del constructor es la siguiente.
    # Los atributos los definimos directamente en el constructor
    def __init__(self, color, marca, modelo, velocidad, potencia, plazas):
      self.__color = color # Al utilizar doble guión bajo ( __ ) estamos definiendo al atributo como privado
      self.__marca = marca
      self.__modelo = modelo
      self.__velocidad = velocidad
      self.__potencia = potencia
      self.__plazas = plazas

    # De ahora en más si quiero acceder a los atributos dentro de la clase deberán llevar sí o sí el doblo guíon bajo __
    
    # SETTERS - Accedemos a la propiedades de nuestro objeto para definir o cambiar un valor. Hacemos SETTERS por la cantidad de propiedades que tenemos 

    def setColor(self, color):
      self.__color = color
    
    def setMarca(self, marca):
      self.__marca = marca

    def setModelo(self, modelo):
      self.__modelo = modelo

    def setVelocidad(self, velocidad):
      self.__velocidad = velocidad

    def setPotencia(self, potencia):
      self.__potencia = potencia
    
    def setPlazas(self, plazas):
      self.__plazas = plazas

    
    # GETTERS - Accedemos a las propiedades de nuestro objeto para obtener los valores de sus atributos. Hacemos GETTERS por la cantidad de propiedades que tenemos. 

    def getColor(self):
      return self.__color
    
    def getMarca(self):
      return self.__marca 

    def getModelo(self):
      return self.__modelo 

    def getVelocidad(self):
      return self.__velocidad 

    def getPotencia(self):
      return self.__potencia 
    
    def getPlazas(self):
      return self.__plazas 

    # MÉTODOS - Todas las funciones que no sean GETTERS ni SETTERS, van a ser funciones/métodos características del objeto
    def acelerar(self):
     self.__velocidad += 1

    def frenar(self):
     self.__velocidad -= 1

    def getInfo(self): 
           
      info = "---- Informacion del coche ----"
      info += "\n Marca: " + self.getMarca()
      info += "\n Modelo: " + self.getModelo()
      info += "\n Color: " + self.getColor()
      info += "\n Velocidad: " + str(self.getVelocidad())
      info += "\n Potencia: " + str(self.getPotencia())
      info += "\n Plazas: " + str(self.getPlazas())

      return info
    
# Fin de la definicion de la clase Coche