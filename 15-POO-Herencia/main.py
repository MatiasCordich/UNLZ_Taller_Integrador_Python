from perro import Perro

# Crear un objeto de la clase Perro
mi_perro = Perro("Chicho", 3, "Labrador")

# Usar getters para obtener los valores
print(f"Nombre: {mi_perro.get_nombre()}, Edad: {mi_perro.get_edad()}, Raza: {mi_perro.get_raza()}")

# Usar métodos heredados y propios
print(mi_perro.hacer_sonido())  # Método heredado
print(mi_perro.ladrar())  # Método propio

# Cambiar valores con setters
mi_perro.set_nombre("Max")
mi_perro.set_edad(5)
mi_perro.set_raza("Golden Retriever")

# Ver cambios
print(f"Nuevo Nombre: {mi_perro.get_nombre()}, Nueva Edad: {mi_perro.get_edad()}, Nueva Raza: {mi_perro.get_raza()}")