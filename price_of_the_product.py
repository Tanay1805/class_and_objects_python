class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, code, name, price):
        self.products[code] = {'name': name, 'price': price}

    def display_menu(self):
        print("Product Code  Product Name  Price")
        for code, product in self.products.items():
            print(f"{code}             {product['name']}        ${product['price']}")

    def generate_bill(self, quantities):
        total_amount = 0
        print("\n\n********** Bill **********")
        print("Product Name  Quantity  Amount")
        for code, quantity in quantities.items():
            product = self.products[code]
            amount = quantity * product['price']
            total_amount += amount
            print(f"{product['name']}        {quantity}         ${amount}")
        print("**************************")
        print(f"Total Amount: ${total_amount}")


def get_user_input(store):
    quantities = {}
    for code in store.products.keys():
        quantity = int(input(f"Enter the quantity of {store.products[code]['name']} (0 if not needed): "))
        quantities[code] = quantity
    return quantities


if __name__ == "__main__":
    store = Store()

    # Adding products to the store
    store.add_product("P001", "Laptop", 800)
    store.add_product("P002", "Smartphone", 400)
    store.add_product("P003", "Headphones", 50)

    store.display_menu()

    user_quantities = get_user_input(store)

    store.generate_bill(user_quantities)
