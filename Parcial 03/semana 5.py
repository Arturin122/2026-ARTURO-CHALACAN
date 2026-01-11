"""
Programa: Calculadora del área de un rectángulo
Descripción: Este programa calcula el área de un rectángulo a partir
de la base y la altura ingresadas por el usuario. Además, verifica
si el área supera un valor mínimo establecido.
"""

# Solicitar datos al usuario (string y float)
nombre_usuario = input("Ingrese su nombre: ")
base_rectangulo = float(input("Ingrese la base del rectángulo (en metros): "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo (en metros): "))

# Cálculo del área (float)
area_rectangulo = base_rectangulo * altura_rectangulo

# Valor mínimo de referencia (integer)
area_minima = 10

# Evaluación lógica (boolean)
es_area_suficiente = area_rectangulo >= area_minima

# Mostrar resultados
print("\nHola,", nombre_usuario)
print("El área del rectángulo es:", area_rectangulo, "metros cuadrados")

# Uso del boolean para tomar una decisión
if es_area_suficiente:
    print("El área es suficiente.")
else:
    print("El área es menor al valor mínimo recomendado.")
