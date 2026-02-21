from producto import Producto
import os


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Constructor del inventario.
        - archivo: nombre del archivo donde se guardan los productos.
        """
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ===============================
    #      MANEJO DE ARCHIVOS
    # ===============================

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, se crea vacío
                open(self.archivo, "w").close()
                print(" Archivo de inventario creado.")
                return

            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        try:
                            id_p, nombre, cantidad, precio = linea.split(",")
                            producto = Producto(
                                id_p,
                                nombre,
                                int(cantidad),
                                float(precio)
                            )
                            self.productos.append(producto)
                        except ValueError:
                            print(" Línea corrupta ignorada:", linea)

            print("✅ Inventario cargado desde archivo.")

        except PermissionError:
            print("❌ Error: Sin permisos para leer el archivo.")

    def guardar_en_archivo(self):
        """Guarda todo el inventario en el archivo."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)

            print(" Cambios guardados en archivo.")

        except PermissionError:
            print("❌ Error: Sin permisos para escribir en el archivo.")
        except Exception as e:
            print("❌ Error inesperado al guardar:", e)

    # ===============================
    #  OPERACIONES DEL INVENTARIO
    # ===============================

    def agregar_producto(self, producto):
        """Agrega un producto verificando ID único."""
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: ID duplicado.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID."""
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("✅ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza cantidad y/o precio."""
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("✅ Producto actualizado.")
                return

        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre (coincidencia parcial)."""
        encontrados = []

        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)

        if not encontrados:
            print("❌ No se encontraron productos.")
        else:
            for p in encontrados:
                self.mostrar_producto(p)

    def mostrar_producto(self, producto):
        """Muestra un producto."""
        print(f"ID: {producto.get_id()} | "
              f"Nombre: {producto.get_nombre()} | "
              f"Cantidad: {producto.get_cantidad()} | "
              f"Precio: ${producto.get_precio():.2f}")

    def mostrar_todos(self):
        """Muestra todo el inventario."""
        if not self.productos:
            print(" Inventario vacío.")
        else:
            for p in self.productos:
                self.mostrar_producto(p)
