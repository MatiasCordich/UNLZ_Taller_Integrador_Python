# ------------------------- [PAQUETE] -------------------------
'''
Así como los módulos son un conjunto de funcionalidades y de variables. 

Los paquetes son un conjunto de modulos orgnanizados de forma jerárquica permitiendo una mayor estructura y organiación en el código de proyectos más grandes. 

Para crear un paquete simplemente tengo que hacer lo siguiente:

- Crear una carpeta donde voy a alojar todos los modulos. En este caso creamos una carpeta llamada "paquete"

- Dentro de la carpeta creada vamos a crear un archivo especial llamado __init__.py asi tal cual y no se le tiene que meter ningun tipo de contenido. Este archivo es un indicador de que estamos creando un paquete

- Por último dentro de la carpeta vamos a crear todos los modulos que necesitemos. 

La estructura seria 

paquete
    __init__.py
    herramientas.py
    prueba.py

Cuando ejecuto mi archivo principal donde importe el paquete y los modulos se va a generar dentro de la carpeta "paquete" una carpeta llamada __pycache__ esa carpeta hay que dejarla como está. 
'''

# Importando un paquete
from paquete import pruebas
from paquete import herramientas

pruebas.probando()
herramientas.nombreCompleto("Sabrina", "Carpenter")

'''
Más adelante, vamos a instalar paquetes externos. Para ver los paquetes disponibles para Python puede acceder a la siguiente pagina:

https://pypi.org/


'''