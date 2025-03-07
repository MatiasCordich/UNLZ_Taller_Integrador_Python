# ------------------------- [CONVERTIR DE UN TIPO DE DATO A OTRO] -------------------------
'''
Mencionamos que Python es un lenguaje de programación de tipado DINÁMICO pero también, 
es un lenguaje cuyo tipado es FUERTE, es decir, aunque no especifique que tipo de dato es una variable, Python no permite ciertas operaciones entre tipos de datos que sean incompatibles sin antes convertirlos. 
'''

texto = "Hola, mi edad es"
numerito = 10

# print(texto + numerito) Esto me va a dar error porque no puedo concatenar un string con un int

# Para poder convertir un int a un string tengo que usar la funcion str()
print(texto + " " + str(numerito))


# Se puede hacer un pasaje de tipos de datos como se muestra en el ejemplo

numerito_2 = 99 # Comienza siendo un int
print(numerito_2)
print(type(numerito_2))

numerito_2 = float(99) # Se convirtio a float
print(numerito_2)
print(type(numerito_2))

numerito_2 = str(99) # Se convirtio a string
print(numerito_2)
print(type(numerito_2))