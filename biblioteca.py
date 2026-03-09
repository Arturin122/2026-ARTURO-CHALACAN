# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla
        self.categoria = categoria
        self.isbn = isbn

    def mostrar_info(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def mostrar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(libro.mostrar_info())


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado.")
        else:
            print("ID de usuario ya existe.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros.pop(isbn)
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            print("Libro prestado.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]

            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[isbn] = libro
                    print("Libro devuelto.")
                    return

            print("El usuario no tiene ese libro.")

    def buscar_libro(self, criterio, valor):
        resultados = []

        for libro in self.libros.values():

            if criterio == "titulo" and libro.info[0].lower() == valor.lower():
                resultados.append(libro)

            elif criterio == "autor" and libro.info[1].lower() == valor.lower():
                resultados.append(libro)

            elif criterio == "categoria" and libro.categoria.lower() == valor.lower():
                resultados.append(libro)

        if resultados:
            for libro in resultados:
                print(libro.mostrar_info())
        else:
            print("No se encontraron resultados.")

    def libros_prestados_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            print(f"Libros prestados a {usuario.nombre}:")
            usuario.mostrar_libros()
        else:
            print("Usuario no encontrado.")


# PRUEBA DEL SISTEMA

biblioteca = Biblioteca()

libro1 = Libro("1984", "George Orwell", "Distopía", "111")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "222")

biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

usuario1 = Usuario("Carlos", "U01")

biblioteca.registrar_usuario(usuario1)

biblioteca.prestar_libro("111", "U01")

biblioteca.libros_prestados_usuario("U01")

biblioteca.devolver_libro("111", "U01")
