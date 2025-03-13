# ------------------------- [FICHEROS] -------------------------
'''
Vamos a utilizar un modulo en Python para manejar ficheros, es decir, archivos. Para eso vamos a utilizar el modulo open que esta dentro del paquete io
'''

from io import open
import pathlib # Este modulo me permite trabajar con rutas absolutas usar la ubicacion precisa del archivo
import shutil # Este modulo nos va a servir para copiar, mover y eliminar archivos

# Creacion de la ruta
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

'''
¿Porqué debo convertir pathlib.Path().absolute() a string?

Lo que sucede es que pathlib.Path().absolute() es un objeto de tipo WindowsPath y por un principio básico de Python no se puede concatenar un string con otro tipo de dato. 

Por eso es fundamental pasarlo a string ya que asi nos aseguramos que la concatenacion se logre.
'''

#  Abrir el archivo
archivo = open(ruta, "a+")

'''
¿Para que sirve el "a+"?

Se los conoce como permisos. 

Este, en concreto, sirve para abrir un archivo en modo de LECTURA y ESCRITURA con las siguientes características:

Si el archivo existe, se abre en modo append (agregar), lo que significa que cualquier escritura se hará al final del archivo sin borrar su contenido.

Si el archivo no existe, se crea automáticamente.

Se puede leer y escribir en el archivo, pero al abrirlo, el puntero de escritura está al final del archivo.

'''

# Escribir algo en el archivo
archivo.write("******** Perro salchicha, gordo bachicha, toma solcito en la orilla del mar ********\n")

# Cerrar al archivo
archivo.close()

'''
Es importante cerrar los archivos una vez que hayanos finalizado  
'''

# Leer contenido de un archivo

# Abrir el archivo 
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

contenido = archivo_lectura.read()
print(contenido)

'''
Para que esto funcione tiene que comentarse la linea 54 y 55. 
'''
# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
print(lista)

# Copiar un archivo 

ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copia.txt"

shutil.copyfile(ruta_original, ruta_nueva)
