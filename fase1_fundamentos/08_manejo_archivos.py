# Curso de Python - GEIIA
# Programa 08: Manejo de Archivos

# Escribir en un archivo (modo "w" = write)
with open("datos.txt", "w") as archivo:
    archivo.write("Hola desde Python\n")
    archivo.write("Segunda línea de texto\n")

# Leer todo el contenido de un archivo (modo "r" = read)
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Leer línea por línea
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print("Línea:", linea.strip())

# ======================
# 📝 EJERCICIO:
# Crea un programa que pida al usuario su nombre y edad
# y los guarde en un archivo llamado "usuario.txt".
