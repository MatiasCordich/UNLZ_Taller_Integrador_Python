# ------------------------- [MODULO DE FECHAS] -------------------------
'''
Vamos a utlizar un modulo que nos viene con Python que es el de fechas. 
'''

# Modulo fechas
import datetime

# Mostrar fecha actual
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)

# Como fecha_completa ahora es un objeto puedo acceder a las propiedades de la misma, por ejemplo; si quiero acceder al año, mes o dia de la fecha
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

# Puedo formatear la fecha de la manera que queramos
fecha_personalizada = fecha_completa.strftime("%d/%m/%y ")

print(fecha_personalizada)

# Acceder a la hora actual 
print(datetime.datetime.now().time())