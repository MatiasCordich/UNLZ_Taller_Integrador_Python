'''
La case Perro es una clase HIJA de la clase Animal donde va a heredar: 

- Los atributos nombre y edad
- El método hacer_sonido
'''

from animal import Animal

# Para indicar que la clase Perro se extiende de la clase Animal simplemente tenemos que insertar la clase Animal dentro de los parametros. 

class Perro(Animal):

    # El constructor de Perro lo definimos con los atributos heredados y con los propios
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) # Así heredo el constructor de la clase Animal
        self.__raza = raza # Atributo propio de la clase Perro

    # Getters y Setters para raza
    def get_raza(self):
        return self.__raza

    def set_raza(self, nueva_raza):
        self.__raza = nueva_raza

    # Metodo propio de la clase HIJA
    def ladrar(self):
        return "¡Guau, guau!"

    
   