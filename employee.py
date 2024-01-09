class Employee:
    el = []

    def employee_details(self):
        self.name = input("Enter name of the employee:")
        self.age = int(input("Enter the age of the employee:"))
        self.role = input("Enter the role of the employee:")

    def add_employee(self):
        employee_info = {'name': self.name, 'age': self.age, 'role': self.role}
        self.el.append(employee_info)

employee_instance = Employee()
employee_instance.employee_details()
employee_instance.add_employee()
print("Employee List:", employee_instance.el)
