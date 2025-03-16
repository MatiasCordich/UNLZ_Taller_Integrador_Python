# ------------------------- [PROGRAMACIÓN ORIENTADA A OBJETOS] -------------------------

# Definimos una clase (molde para crear nuestros objetos de ese tipo en concreto)

class Coche: 

    # Atributos o propiedades
    # Características del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Portofino"
    velocidad = 325
    potencia = 620
    plazas = 2

    # Métodos, acciones que hace el objeto (coche)

    # El self en Python vendría a ser el equivalente al this en otros lenguajes. 
    def acelerar(self):
     self.velocidad += 1

    def frenar(self):
     self.velocidad -= 1

    def getVelocidad(self):
      return self.velocidad
    
# Fin de la definicion de la clase Coche

# Crear un objeto / Instanciar la clase

coche = Coche()

# Para acceder a las propiedades del coche simplemente hago lo siguiete

marca_coche = coche.marca
color_coche = coche.color
print(marca_coche, color_coche)


print(f"Velocidad actual: {coche.velocidad}")

# Ademas puedo acceder a sus metodos de la siguiente manera
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print(f"Velocidad nueva: {coche.velocidad}")