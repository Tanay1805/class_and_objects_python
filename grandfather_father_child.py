class Grandfather:
    def __init__(self, grandfather_property):
        self.grandfather_property = grandfather_property

    def display_grandfather_property(self):
        print(f"Grandfather's Property: {self.grandfather_property}")


class Father(Grandfather):
    def __init__(self, grandfather_property, father_property):
        super().__init__(grandfather_property)
        self.father_property = father_property

    def display_father_property(self):
        self.display_grandfather_property()
        print(f"Father's Property: {self.father_property}")


class Child(Father):
    def __init__(self, grandfather_property, father_property, child_property):
        super().__init__(grandfather_property, father_property)
        self.child_property = child_property

    def display_child_property(self):
        self.display_grandfather_property()
        self.display_father_property()
        print(f"Child's Property: {self.child_property}")


if __name__ == "__main__":
    child_instance = Child("Grandfather's Value", "Father's Value", "Child's Value")
    child_instance.display_child_property()
