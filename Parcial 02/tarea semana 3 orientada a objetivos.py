# Programa POO para calcular el promedio semanal del clima

class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self._temperatura = temperatura  # Encapsulamiento

    def obtener_temperatura(self):
        return self._temperatura


class SemanaClima:
    def __init__(self):
        self.registros = []

    def ingresar_datos(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves",
                "Viernes", "Sábado", "Domingo"]

        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.registros.append(ClimaDiario(dia, temp))

    def promedio_semanal(self):
        total = sum(d.obtener_temperatura() for d in self.registros)
        return total / len(self.registros)


def main():
    semana = SemanaClima()
    semana.ingresar_datos()
    print(f"\nPromedio semanal: {semana.promedio_semanal():.2f} °C")


main()
