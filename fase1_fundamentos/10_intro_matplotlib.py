# Curso de Python - GEIIA
# Programa 10: Visualización básica con Matplotlib

import matplotlib.pyplot as plt

# Datos para graficar
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 🔹 Gráfico de línea
plt.plot(x, y, label="y = 2x", color="blue", marker="o")
plt.title("Gráfica de Línea")   # título del gráfico
plt.xlabel("Eje X")             # etiqueta eje X
plt.ylabel("Eje Y")             # etiqueta eje Y
plt.legend()                    # muestra leyenda
plt.show()

# ======================
# 📝 EJERCICIO:
# Haz un gráfico de barras que muestre el número de alumnos
# en 3 carreras: IA (20), Mecatrónica (15) e Industrial (10).
