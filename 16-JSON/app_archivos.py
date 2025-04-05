texto = "Hola"

# Forma clásica de abrir y escribir en un archivo (requiere cerrar manualmente)
'''
f =  open("archivito.txt", "w")

f.write(texto)

f.close()
'''

# Con 'with open(...) as' se abre el archivo y se cierra automáticamente al salir del bloque
with open("archivito.txt", "w") as f:
    f.write(texto)

