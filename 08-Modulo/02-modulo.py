# Importar un modulo. Segunda forma

from mimodulo import *

'''
Con este forma estamos diciendo que DESDE el modulo "mimodulo" quiero que me importes todas las funciones que tiene ese modulo mediante el asterisco (*).

Si quiero importar una función específica simplemente tengo que hacer lo siguiente:

from mimodulo import holaMundo
'''

# Como vemos simplemente ahora podemos invocar las funciones del modulo de forma directa
print(holaMundo("Jorge"))
print(calculadora(4,5, True))
print(calculadora(4,0))