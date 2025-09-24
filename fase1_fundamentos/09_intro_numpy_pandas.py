# Curso de Python - GEIIA
# Programa 09: Introducción a Numpy y Pandas

import numpy as np
import pandas as pd

# 🔹 Numpy (trabajo con arreglos numéricos)
arr = np.array([1, 2, 3, 4, 5])   # crea un array
print("Array Numpy:", arr)
print("Media:", arr.mean())       # promedio
print("Suma:", arr.sum())         # suma total

# 🔹 Pandas (manejo de tablas de datos)
datos = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [23, 21, 25]
}
df = pd.DataFrame(datos)   # crea un DataFrame tipo tabla
print("\nDataFrame Pandas:")
print(df)

# ======================
# 📝 EJERCICIO:
# Crea un array de Numpy con 10 números aleatorios entre 1 y 100
# y calcula su media y máximo.
# Luego, crea un DataFrame de Pandas con 3 columnas: Nombre, Edad y Carrera.
