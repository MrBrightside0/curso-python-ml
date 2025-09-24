# Curso de Python - GEIIA
# Programa 03: Operadores

# Los operadores permiten realizar acciones sobre valores o variables.

a = 10
b = 3

# 🔹 Operadores aritméticos
print("Suma:", a + b)          # + suma → 10 + 3 = 13
print("Resta:", a - b)         # - resta → 10 - 3 = 7
print("Multiplicación:", a * b)# * multiplicación → 10 * 3 = 30
print("División:", a / b)      # / división real → 10 / 3 = 3.333...
print("División entera:", a // b) # // división entera → 10 // 3 = 3
print("Módulo:", a % b)        # % residuo de la división → 10 % 3 = 1
print("Potencia:", a ** b)     # ** potencia → 10^3 = 1000

# 🔹 Operadores relacionales
print("¿a > b?", a > b)        # > mayor que → True
print("¿a == b?", a == b)      # == igualdad → False
print("¿a != b?", a != b)      # != distinto de → True

# 🔹 Operadores lógicos
x = True
y = False
print("AND:", x and y)         # and → True si ambos son True
print("OR:", x or y)           # or → True si al menos uno es True
print("NOT:", not x)           # not → invierte el valor lógico

# ======================
# 📝 EJERCICIO:
# Pide dos números al usuario y muestra:
# 1. Su suma
# 2. Su multiplicación
# 3. Si el primero es mayor que el segundo
