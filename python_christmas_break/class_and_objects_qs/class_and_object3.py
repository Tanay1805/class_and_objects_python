class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.show_menu()
        self.ask_to_add_more()

    def show_menu(self):
        print("1. Tomato\n2. Onion\n3. Potato\n4. Chilli")
        option = int(input("Enter your option:"))

        if option == 1:
            self.cart.append("Tomato")
        elif option == 2:
            self.cart.append("Onion")
        elif option == 3:
            self.cart.append("Potato")
        elif option == 4:
            self.cart.append("Chilli")
        else:
            print("Invalid option")

        print("Your cart:", self.cart)

    def ask_to_add_more(self):
        while True:
            add_more = input("Do you want to add more items? (yes/no): ").lower()
            if add_more != "yes":
                break

            self.show_menu()

    def remove_item(self):
        print("Do you want to delete anything?")
        print(self.cart)
        option = int(input("Enter the item to delete (1-4):"))

        if 1 <= option <= 4:
            item_to_remove = self.cart[option - 1]
            self.cart.remove(item_to_remove)
            print(f"{item_to_remove} removed from your cart")
        else:
            print("Invalid option")

        print("Your cart:", self.cart)


shopping = ShoppingCart()
shopping.remove_item()
