# Curso de Python - GEIIA
# Programa 02: Variables y Tipos de Datos

# Una variable es un espacio en memoria donde se guarda un valor.

nombre = "Ana"          # str → texto
edad = 20               # int → número entero
altura = 1.68           # float → número decimal
es_estudiante = True    # bool → lógico (True/False)

# Mostrar variables en pantalla
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?", es_estudiante)

# Saber qué tipo de dato es una variable con type()
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))

# Conversión de tipos (casting)
numero_str = "15"       # esto es texto
numero_int = int(numero_str)  # convertir a entero
print("Número convertido:", numero_int + 5)

# ======================
# 📝 EJERCICIO:
# Declara 3 variables con tus propios datos: nombre, semestre y promedio.
# Imprímelas en pantalla junto con su tipo de dato.
