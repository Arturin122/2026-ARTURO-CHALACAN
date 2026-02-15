from inventario import Inventario
from producto import Producto


def menu():
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIOS ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(
                Producto(id_producto, nombre, cantidad, precio)
            )

        elif opcion == "2":
            inventario.eliminar_producto(input("ID a eliminar: "))

        elif opcion == "3":
            id_producto = input("ID: ")
            cantidad = input("Nueva cantidad (enter si no cambia): ")
            precio = input("Nuevo precio (enter si no cambia): ")
            inventario.actualizar_producto(
                id_producto,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            inventario.buscar_por_nombre(input("Nombre a buscar: "))

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
