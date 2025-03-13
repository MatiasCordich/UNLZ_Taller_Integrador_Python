# ------------------------- [MODULOS] -------------------------
'''
Los módulos son funcionalidades ya hechas para ser reutilizadas lo que permite organizar el código en archivos separados para mejorar la matenibilidad y reutilización. 

Para importar un modulo tenemos que usar la siguiente nomemclatura

import nombre_modulo

Los módulos pueden ser:
- Estándar: Los módulos que ya vienen incluídos en Python como el math, os, sys,etc.
- De terceros: Se instalan con el comando "pip", como numpy, pandas, etc.
- Personalizados: Son los archivos .py que nosotros mismos creamos.

En Python existen muchos módulos, se pueden consultar en el siguiente link: 

https://docs.python.org/3/library/

'''

# Importacion de un modulo propio
import mimodulo

# Utilizaciion de los metodos de mi modulo
print(mimodulo.holaMundo("Pepe"))

print(mimodulo.calculadora(4,5, True))
print(mimodulo.calculadora(4,0)) # Recordemos que el tercer parametro es opcioneal 

'''
En el archivo 02-modulo.py se ve otra forma de importar modulos. 
'''