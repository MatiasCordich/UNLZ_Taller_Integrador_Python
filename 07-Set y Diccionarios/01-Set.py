# ------------------------- [SET] -------------------------
'''
Es otra estructura de datos similar a las listas pero con la diferencia de que los sets no tienen ÍNDICE ni ORDEN. 
'''

# Ejemplo - Definicion de un set

pistas = {"Monza", "Monaco", "Spa Francorchamps"}

print(type(pistas))

'''
Como no tienen un orden ni índice, cuando lo muestre por pantalla los elementos van a aparecer en un orden aleatorio cada vez qe ejecute el programa. 
'''
print(pistas)

# Metodos de los set
'''
Me agrega este elemento al set y me lo agrega en cualquier posición
'''
pistas.add("Silverstone")

'''
Como mencionamos, al no tener índice se le debe pasar por parámetro un valor par que lo vaya a buscar al set y lo elemine
'''
pistas.remove("Spa Francorchamps")