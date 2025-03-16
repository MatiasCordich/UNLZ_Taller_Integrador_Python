# ------------------------- [HERENCIA] -------------------------
'''
La clase Animal será una clase BASE, donde va a tener atributos y métodos que van a ser heredados hacia las clases que utilicen la clase Animal. 
'''
 
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Setters
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa")

    # Métodos de la clase BASE
    def hacer_sonido(self):
        return "Hace un sonido..."