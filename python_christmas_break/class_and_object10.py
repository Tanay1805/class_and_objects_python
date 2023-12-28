class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")


class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")


class PersonInfo(Employee, Student):
    def __init__(self, name, age, id_number, salary=None, major=None):
        Employee.__init__(self, id_number, salary)
        Student.__init__(self, id_number, major)
        Person.__init__(self, name, age)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def display_person_info(self):
        self.display_info()
        if hasattr(self, 'salary'):
            self.display_employee_info()
        if hasattr(self, 'major'):
            self.display_student_info()


# User input
name = input("Enter name: ")
age = int(input("Enter age: "))
id_number = input("Enter employee or student ID: ")
role = input("Enter role (employee or student): ")

p = None  # Declare p variable

if role.lower() == 'employee':
    salary = float(input("Enter salary: "))
    p = PersonInfo(name=name, age=age, id_number=id_number, salary=salary)
elif role.lower() == 'student':
    major = input("Enter major: ")
    p = PersonInfo(name=name, age=age, id_number=id_number, major=major)
else:
    print("Invalid role entered. Please specify either 'employee' or 'student'.")

# Displaying the information
if p is not None:
    p.display_person_info()
