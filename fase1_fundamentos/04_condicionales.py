# Curso de Python - GEIIA
# Programa 04: Condicionales

# Las condicionales permiten ejecutar cierto código
# solo si se cumple una condición (True/False).

edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Eres mayor de edad ✅")   # Se ejecuta si la condición es True
else:
    print("Eres menor de edad ❌")   # Se ejecuta si la condición es False

# También podemos usar elif (else if)
nota = float(input("Escribe tu calificación: "))

if nota >= 90:
    print("Excelente 🏆")
elif nota >= 70:
    print("Aprobado 👍")
else:
    print("Reprobado 😢")

# ======================
# 📝 EJERCICIO:
# Haz un programa que pida un número al usuario
# y diga si es positivo, negativo o cero.
