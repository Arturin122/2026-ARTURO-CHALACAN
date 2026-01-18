# Ejemplo POO en Python

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.__encendido = False   # Encapsulación

    def encender(self):
        self.__encendido = True

    def tipo(self):               # Método para polimorfismo
        return "Vehículo"


class Moto(Vehiculo):             # Herencia
    def tipo(self):               # Polimorfismo
        return "Moto"


# Programa principal
if __name__ == "__main__":
    v1 = Vehiculo("Genérico")
    v2 = Moto("Yamaha")

    lista = [v1, v2]

    for v in lista:
        print(f"{v.marca}: {v.tipo()}")
