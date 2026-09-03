class Product:
    """Represents a product"""

    def __init__(self, name, price, quantity):
        """Initializes a product with name, price and quantity"""
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("Invalid input")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self):
        """Gets the quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity of the product"""
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        """Checks if the product is active"""
        return self.active

    def activate(self):
        """Activate the product"""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def show(self):
        """Show the product, price and quantity"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Buy a certain quantity of this product

        Arguments:
            quantity {int} -- number of items to buy

        Returns:
            Total price of the purchase
        Raises:
            ValueError -- If quantity is less than available stock"""

        if quantity > self.quantity:
            raise ValueError("Not enough in stock")

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
