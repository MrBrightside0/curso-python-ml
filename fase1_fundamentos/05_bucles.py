# Curso de Python - GEIIA
# Programa 05: Bucles

# Los bucles permiten repetir instrucciones varias veces.

# 🔹 Bucle for (repite un bloque de código un número de veces)
for i in range(5):   # range(5) genera [0,1,2,3,4]
    print("Iteración:", i)

# 🔹 Bucle while (repite mientras se cumpla una condición)
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1   # incrementa contador

# 🔹 Uso de break (detiene el bucle)
for i in range(10):
    if i == 3:
        break       # rompe el ciclo
    print("Break en", i)

# 🔹 Uso de continue (salta una iteración)
for i in range(5):
    if i == 2:
        continue    # salta el número 2
    print("Continue en", i)

# ======================
# 📝 EJERCICIO:
# Escribe un programa que imprima todos los números del 1 al 20,
# pero que use "continue" para saltarse los múltiplos de 3.
