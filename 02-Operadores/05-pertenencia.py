# ------------------------- [OPERADORES DE PERTENENCIA] -------------------------
'''
Estos operadores verifican si un valor esta dentro de una secuencia, es decir, si estan dentro de una 
- LISTA
- TUPLA
- STRING
- SET
- DICCIONARIO

Los operados son
- in
- not in

El resultado final sera un valor BOOLEANO. 
'''

# Tenemos nuestra lista 
lista = [1, 2, 3, 4]

print("3 en lista:", 3 in lista)  # True (3 está en la lista)

print("5 no en lista:", 5 not in lista)  # True (5 no está en la lista)

texto = "Hola mundo"
print("'H' en texto:", 'H' in texto)  # True ('H' está en el string)
print("'z' no en texto:", 'z' not in texto)  # True ('z' no está en el string)
 
mi_diccionario = {"clave1": 10, "clave2": 20}
print("'clave1' en diccionario:", "clave1" in mi_diccionario)  # True
