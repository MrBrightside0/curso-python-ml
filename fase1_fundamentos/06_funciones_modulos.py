# Curso de Python - GEIIA
# Programa 06: Funciones y Módulos

# Una función es un bloque de código que podemos reutilizar.

# Definición de función
def saludar(nombre):
    print("Hola", nombre)

# Llamada de función
saludar("Ana")
saludar("Luis")

# Función con retorno (devuelve un valor)
def cuadrado(x):
    return x ** 2

print("El cuadrado de 5 es:", cuadrado(5))

# Función con varios parámetros
def suma(a, b):
    return a + b

print("Suma:", suma(4, 7))

# ======================
# 📝 EJERCICIO:
# Crea una función llamada "es_par" que reciba un número
# y regrese True si es par y False si es impar.
# Luego prueba tu función con varios números.
