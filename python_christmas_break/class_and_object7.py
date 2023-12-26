class Shoe:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def shoe_show(self):
        print(f"Color: {self.color}")
        print(f"Brand: {self.brand}")


class Converse(Shoe):
    def __init__(self, color, lowOrHighTop, tongueColor):
        super().__init__(color, brand='Converse')
        self.lowOrHighTop = lowOrHighTop
        self.tongueColor = tongueColor

    def shoe_type(self):
        self.shoe_show()
        print(f"Low or High Top: {self.lowOrHighTop}")
        print(f"Tongue Color: {self.tongueColor}")

class CombatShoe(Shoe):
    def __init__(self, color, millitarybranch, DesertorJungle):
        super().__init__(color, brand='Combat Shoe')
        self.millitarybranch = millitarybranch
        self.DesertorJungle = DesertorJungle

    def military(self):
        self.shoe_show()
        print(f"Military Branch: {self.millitarybranch}")
        print(f"Desert or Jungle: {self.DesertorJungle}")

class Sandal(Shoe):
    def __init__(self, color, OpenorClosed, waterproof):
        super().__init__(color, brand='Sandal')
        self.OpenorClosed = OpenorClosed
        self.waterproof = waterproof

    def sandal_type(self):
        self.shoe_show()
        print(f"Open or Closed: {self.OpenorClosed}")
        print(f"Waterproof: {self.waterproof}")

def get_user_input():
    color = input("Enter the color of the shoe: ")

    print("Choose the type of shoe:")
    print("1. Converse")
    print("2. Combat Shoe")
    print("3. Sandal")
    shoe_type = int(input("Enter your choice (1, 2, or 3): "))

    if shoe_type == 1:
        lowOrHighTop = input("Enter Low or High Top: ")
        tongueColor = input("Enter Tongue Color: ")
        return Converse(color, lowOrHighTop, tongueColor)

    elif shoe_type == 2:
        millitarybranch = input("Enter Military Branch: ")
        DesertorJungle = input("Enter Desert or Jungle: ")
        return CombatShoe(color, millitarybranch, DesertorJungle)

    elif shoe_type == 3:
        OpenorClosed = input("Enter Open or Closed: ")
        waterproof = input("Is it Waterproof? (True/False): ").lower() == 'true'
        return Sandal(color, OpenorClosed, waterproof)

    else:
        print("Invalid choice. Exiting.")
        return None
    
user_shoe = get_user_input()
if user_shoe:
    if isinstance(user_shoe, Shoe):
        user_shoe.shoe_show()
        if isinstance(user_shoe, Converse):
            user_shoe.shoe_type()
        elif isinstance(user_shoe, CombatShoe):
            user_shoe.military()
        elif isinstance(user_shoe, Sandal):
            user_shoe.sandal_type()
