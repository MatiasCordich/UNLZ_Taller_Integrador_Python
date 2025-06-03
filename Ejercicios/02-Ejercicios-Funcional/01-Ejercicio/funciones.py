'''
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
'''

# Función que aplica descuento al precio
def aplicar_descuento(precio, descuento):
 return precio - precio * descuento / 100

# Función que aplica IVA
def aplicar_descuento(precio, porcentaje):
 return precio + precio * porcentaje / 100

# La tercera función debe recibir dos cosas
# Un diccionario que debe tener precios con sus respectivos porcentajes
# Aplica la función dada, ya sea del IVA como de los descuentos
def precio_final(canasta, funcion):
 
 # Variable acumuladora
 total = 0

 # Recorremos la canasta (diccionario)
 for precio, porcentaje in canasta.items():
  total += funcion(precio,porcentaje)
  return total

  
