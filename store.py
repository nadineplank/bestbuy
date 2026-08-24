class Store:
    """Represents a store"""

    def __init__(self, product_list):
        """Initializes the store with a list of products"""
        self.products = product_list

    def add_product(self, product):
        """Adds a product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store"""
        self.products.remove(product)

    def get_total_quantity(self):
        """Gets the total quantity of the products that are in stock"""
        return sum(product.quantity for product in self.products)

    def get_all_products(self):
        """Gets all the products that are in stock"""

        return [product for product in self.products if product.active]

    def order(self, shopping_list):
        """Orders the shopping list"""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
