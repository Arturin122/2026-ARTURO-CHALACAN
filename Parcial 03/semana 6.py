
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__edad = 0      # Encapsulación

    def get_edad(self):
        return self.__edad

    def sonido(self):       # Método para polimorfismo
        return "Hace un sonido"


class Perro(Animal):        # Herencia
    def sonido(self):       # Polimorfismo (sobrescritura)
        return "Ladra"


# Programa principal
if __name__ == "__main__":
    animal = Animal("Animal genérico")
    perro = Perro("Firulais")

    animales = [animal, perro]

    for a in animales:
        print(f"{a.nombre}: {a.sonido()}")
