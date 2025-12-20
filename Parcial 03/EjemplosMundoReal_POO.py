class Product:
    """Representa un producto en la tienda."""

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_sold = False

    def sell(self):
        """Marca el producto como vendido si está disponible."""
        if not self.is_sold:
            self.is_sold = True
            return True
        return False

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Cashier:
    """Representa al cajero de la tienda."""

    def __init__(self, name):
        self.name = name

    def process_sale(self, product):
        """Procesa la venta de un producto."""
        return product.sell()


class Customer:
    """Representa a un cliente de la tienda."""

    def __init__(self, name):
        self.name = name
        self.purchased_products = []

    def buy_product(self, product, cashier):
        """Permite al cliente comprar un producto."""
        if cashier.process_sale(product):
            self.purchased_products.append(product)
            print(f"{self.name} compró el producto: {product.name}")
        else:
            print(f"El producto {product.name} no está disponible.")


# Ejemplo de uso
producto1 = Product("Laptop", 1200)
cajero = Cashier("Carlos")
cliente = Customer("María")

cliente.buy_product(producto1, cajero)

