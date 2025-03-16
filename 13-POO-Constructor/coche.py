class Coche: 

    # Atributos o propiedades
    # Características del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Portofino"
    velocidad = 325
    potencia = 620
    plazas = 2

    # CONSTRUCTOR - Es el primer metodo que vamos a crear en nuestras clases, la estructura del constructor es la siguiente.
    def __init__(self, color, marca, modelo, velocidad, potencia, plazas):
      self.color = color
      self.marca = marca
      self.modelo = modelo
      self.velocidad = velocidad
      self.potencia = potencia
      self.plazas = plazas

    # SETTERS - Accedemos a la propiedades de nuestro objeto para definir o cambiar un valor. Hacemos SETTERS por la cantidad de propiedades que tenemos 

    def setColor(self, color):
      self.color = color
    
    def setMarca(self, marca):
      self.marca = marca

    def setModelo(self, modelo):
      self.modelo = modelo

    def setVelocidad(self, velocidad):
      self.velocidad = velocidad

    def setPotencia(self, potencia):
      self.potencia = potencia
    
    def setPlazas(self, plazas):
      self.plazas = plazas

    
    # GETTERS - Accedemos a las propiedades de nuestro objeto para obtener los valores de sus atributos. Hacemos GETTERS por la cantidad de propiedades que tenemos. 

    def getColor(self):
      return self.color
    
    def getMarca(self):
      return self.marca 

    def getModelo(self):
      return self.modelo 

    def getVelocidad(self):
      return self.velocidad 

    def getPotencia(self):
      return self.potencia 
    
    def getPlazas(self):
      return self.plazas 

    # MÉTODOS - Todas las funciones que no sean GETTERS ni SETTERS, van a ser funciones/métodos características del objeto
    def acelerar(self):
     self.velocidad += 1

    def frenar(self):
     self.velocidad -= 1

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