# Programa para calcular el promedio semanal del clima
# utilizando Programación Tradicional (funciones).

def pedir_temperatura(dia):
    """
    Pide al usuario que ingrese la temperatura de un día específico.
    La entrada es validada para asegurarse de que sea un número.
    """
    while True:
        try:
            temp = float(input(f"Ingrese la temperatura de {dia}: "))
            return temp
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingrese un número.")


def ingresar_temperaturas(dias):
    """
    Ingresa las temperaturas para cada día de la semana
    usando la función pedir_temperatura().
    """
    temperaturas = []
    for dia in dias:
        temperatura = pedir_temperatura(dia)
        temperaturas.append(temperatura)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Si la lista está vacía, devuelve 0.
    """
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)


def mostrar_temperaturas(dias, temperaturas):
    """
    Muestra las temperaturas ingresadas para cada día de la semana.
    """
    print("\n=== Temperaturas de la semana ===")
    for dia, temp in zip(dias, temperaturas):
        print(f"{dia}: {temp:.2f} °C")


def main():
    """
    Función principal que organiza el flujo del programa.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = ingresar_temperaturas(dias_semana)

    mostrar_temperaturas(dias_semana, temperaturas)

    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal del clima es: {promedio:.2f} °C")


# Punto de inicio del programa
if __name__ == "__main__":
    main()

