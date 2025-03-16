# Vamos a importar nuestra clase Coche como un modulo.

from coche import Coche

# Crear un objeto / Instanciar la clase

coche_1 = Coche("Amarillo", "Lamborghini", "Urus", 305, 650, 4)

coche_2 = Coche("Rojo", "Ferrari", "488 Pista", 340, 720, 2)

coche_3 = Coche("Azul", "Porsche", "911 Turbo S", 330, 650, 2)

coche_4 = Coche("Negro", "McLaren", "720S", 341, 720, 2)


# Obtenemos la info completa del coche


print(coche_1.getInfo())

print(coche_2.getInfo())

print(coche_3.getInfo())

print(coche_4.getInfo())

# Detectar el tipado del objeto

coche_4 = "Aleatorio"

if type(coche_4) == Coche:
    print("Es un coche")
else:
   print("No es un coche") 

