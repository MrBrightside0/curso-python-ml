# Curso de Python - GEIIA
# Programa 07: Listas, Tuplas y Diccionarios

# 🔹 Listas (colecciones que se pueden modificar)
frutas = ["manzana", "pera", "uva"]
print("Lista frutas:", frutas)

frutas.append("plátano")   # agrega al final
print("Lista modificada:", frutas)

# 🔹 Tuplas (colecciones que NO se pueden modificar)
coordenadas = (10, 20)
print("Tupla:", coordenadas)

# 🔹 Diccionarios (clave: valor)
persona = {"nombre": "Ana", "edad": 22, "ciudad": "Monterrey"}
print("Diccionario:", persona)

# Acceder y modificar valores
print("Nombre:", persona["nombre"])
persona["edad"] = 23
print("Edad modificada:", persona["edad"])

# ======================
# 📝 EJERCICIO:
# Crea una lista con al menos 5 números enteros
# y un diccionario que guarde:
# {"maximo": número más grande, "minimo": número más pequeño}.
