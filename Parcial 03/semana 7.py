class Curso:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.activo = True
        print(f"Curso '{self.nombre}' creado con {self.creditos} créditos.")

    def cerrar_curso(self):
        self.activo = False
        print(f"Curso '{self.nombre}' cerrado.")

    def __del__(self):
        if self.activo:
            print(f"Curso '{self.nombre}' eliminado sin cerrar.")
        else:
            print(f"Curso '{self.nombre}' eliminado correctamente.")


class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        print(f"Estudiante {self.nombre}, {self.edad} años, inscrito en {self.curso.nombre}.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Curso: {self.curso.nombre}")

    def __del__(self):
        print(f"Estudiante {self.nombre} eliminado del sistema.")


# Programa principal
curso1 = Curso("Programación", 5)
estudiante1 = Estudiante("Ana", 20, curso1)

estudiante1.mostrar_info()

curso1.cerrar_curso()

del estudiante1
del curso1
