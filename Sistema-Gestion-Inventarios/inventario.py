from producto import Producto


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ID duplicado")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado")
                return
        print("Producto no encontrado")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado")
                return
        print("Producto no encontrado")

    def buscar_por_nombre(self, nombre):
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                self.mostrar_producto(p)

    def mostrar_producto(self, producto):
        print(f"ID: {producto.get_id()} | "
              f"Nombre: {producto.get_nombre()} | "
              f"Cantidad: {producto.get_cantidad()} | "
              f"Precio: ${producto.get_precio()}")

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío")
        for p in self.productos:
            self.mostrar_producto(p)
