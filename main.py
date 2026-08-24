import store
import products
import sys

class StoreUI:
    """Represents the UI for the store"""

    def __init__(self, store_obj):
        """Initializes the store UI"""
        self.store = store_obj

    def display_products(self):
        """Displays all the products in the store"""
        all_products = self.store.get_all_products()
        for index, product in enumerate(all_products):
            print(
                f"{index + 1}. {product.name}, "
                f"Price: ${product.price}, "
                f"Quantity: {product.quantity}"
            )
        return all_products

    def start(self):
        """Starts the UI"""
        menu = """
           Store Menu
           ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """

        print(menu)
        user_choice = int(input("Please choose a number: "))

        # Handle user menu selection
        if user_choice == 1:
            self.display_products()
            self.start()

        elif user_choice == 2:
            print(f"Total of {self.store.get_total_quantity()} items in store")
            self.start()

        elif user_choice == 3:
            all_products = self.display_products()
            print("------")
            print("When you want to finish order, enter empty text.")
            shopping_list = []

            while True:
                product_choice = input("Which product # do you want? ")

                if product_choice == "":
                    break

                product_choice = int(product_choice)
                quantity = int(input("What amount do you want? "))
                shopping_list.append((all_products[product_choice - 1], quantity))
                print("Product added to the list")
                print(" ")
            try:
                total_price = self.store.order(shopping_list)
                print("*********")
                print(f"Order made! Total payment: ${total_price}")
            except ValueError:
                print("Error while making order! Quantity larger than what exists")

            self.start()

        elif user_choice == 4:
            sys.exit()

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

ui = StoreUI(best_buy)
ui.start()
