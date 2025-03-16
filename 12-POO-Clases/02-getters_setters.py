# ------------------------- [GETTERS Y SETTERS] -------------------------
'''
En el ejemplo anterior definimos una clase Coche que tenia propiedades y métodos. 

El primer inconveniente con esto es que no es recomendable acceder a las propiedades de forma directa. 

Seria mucho mejor acceder a las mismas a través de métodos, para eso entran los GETTERS Y SETTERS. 
'''

class Coche: 

    # Atributos o propiedades
    # Características del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Portofino"
    velocidad = 325
    potencia = 620
    plazas = 2

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
    
# Fin de la definicion de la clase Coche

# Crear un objeto / Instanciar la clase

coche = Coche()

# Accedemos a las propiedades y definimos un nuevo color al coche mediante un SETTER
coche.setColor("amarillo")

# Accedemos a los valores de las propiedades del objeto mediante los GETTERS
print(coche.getMarca(),coche.getColor(), coche.getModelo())

print(f"Velocidad actual: {coche.getVelocidad()}")

# Ademas puedo acceder a sus metodos de la siguiente manera
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print(f"Velocidad nueva: {coche.getVelocidad()}")