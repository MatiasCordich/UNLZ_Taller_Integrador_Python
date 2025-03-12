# ------------------------- [LISTAS] -------------------------
'''
Las listas tienen sus propios métodos que nos va a servir para manipular los elementos de la misma. A continuación se muestran algunos métodos. 
'''

# Crear una lista inicial
lista = [1, 2, 3, 4, 5]

# Agregar elementos
lista.append(6)  # Agrega 6 al final
lista.insert(2, 10)  # Inserta 10 en la posicion 2
print(lista)  # [1, 2, 10, 3, 4, 5, 6]

# Eliminar elementos
lista.remove(3)  # Elimina la primera aparicion de 3
ultimo = lista.pop()  # Elimina y devuelve el ultimo elemento
print(lista)  # [1, 2, 10, 4, 5]

# Ordenar lista
lista.sort()  # Ordena ascendente
print(lista)  # [1, 2, 4, 5, 10]
lista.sort(reverse=True)  # Ordena descendente
print(lista)  # [10, 5, 4, 2, 1]

# Buscar elementos
indice = lista.index(4)  # Devuelve el indice de 4
print(indice)  # 2

# Contar elementos
cantidad = lista.count(5)  # Cuenta cuantas veces aparece 5
print(cantidad)  # 1

# Copiar lista
nueva_lista = lista.copy()
print(nueva_lista)  # [10, 5, 4, 2, 1]

# Extender lista
lista.extend([7, 8, 9])  # Agrega elementos de otra lista
print(lista)  # [10, 5, 4, 2, 1, 7, 8, 9]

# Obtener sublista
sublista = lista[2:5]  # Elementos de indice 2 a 4
print(sublista)  # [4, 2, 1]

# Limpiar lista
lista.clear()
print(lista)  # []


