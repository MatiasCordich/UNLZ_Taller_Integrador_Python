from mimodulo import info_numero, sumar_todos

info = info_numero(5)

print(info) # Ver el resultado

# Recorrer el resultado que me devuelve la funcion

for clave in info:
 
 # Imprimo el nombre de las claves del diccionario
 print(clave)

 # Imprimo cada valor del diccionario
 print(info[clave])

 # Imprimo todo
 print(f"{clave} : {info[clave]}")

# Hago una tupla con valores
tuplita = (14,16,2,44)

# Llamo la función sumar_todos de mimodulo.py
r = sumar_todos(tuplita)

print(r) # 76