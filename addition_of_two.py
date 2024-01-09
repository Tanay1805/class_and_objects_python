class UserInput:
    def add(self):
        self.a = int(input('Enter value of a: '))
        self.b = int(input('Enter value of b: '))

class Addition(UserInput):
    def perform_addition(self):
        self.add()
        self.result = self.a + self.b
        print(f"The sum of {self.a} and {self.b} is: {self.result}")

addition_instance = Addition()
addition_instance.perform_addition()
