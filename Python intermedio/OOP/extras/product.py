class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Inventory:
    products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(
                f"Product: {product.name}, Price: {product.price}, Stock: {product.stock}"
            )

    def calculate_total_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.stock
        return total_value


if __name__ == "__main__":
    inventory = Inventory()
    product1 = Product("Laptop", 1000, 10)
    product2 = Product("Mouse", 10, 20)
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.show_products()
    print(f"Total inventory value: {inventory.calculate_total_inventory_value()}")
    product3 = Product("Monitor", 200, 5)
    inventory.add_product(product3)
    inventory.show_products()
    print(f"Total inventory value: {inventory.calculate_total_inventory_value()}")
