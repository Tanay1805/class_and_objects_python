class LU:
    def __init__(self, lu_type):
        self.lu_type = lu_type

    def display_lu_type(self):
        print(f"Land Use Type: {self.lu_type}")


class ITM:
    def __init__(self, itm_course):
        self.itm_course = itm_course

    def display_itm_course(self):
        print(f"IT Management Course: {self.itm_course}")


class DerivedClass(LU, ITM):
    def __init__(self, lu_type, itm_course, derived_property):
        super().__init__(lu_type)
        super(ITM, self).__init__(itm_course)

        self.derived_property = derived_property

    def display_derived_properties(self):
        # Utilize methods from both base classes
        self.display_lu_type()
        self.display_itm_course()
        print(f"Derived Property: {self.derived_property}")


# Example usage of the classes
if __name__ == "__main__":
    derived_instance = DerivedClass("Residential", "ITM101", "Some Derived Property")

    derived_instance.display_derived_properties()
