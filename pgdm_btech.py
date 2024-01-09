class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Department:
    def __init__(self, name):
        self.name = name
        self.students = []

    def admit_student(self, student):
        self.students.append(student)

    def get_student_count(self):
        return len(self.students)

# Function to admit students based on user input
def admit_students():
    departments = {}
    
    while True:
        name = input("Enter student name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        department = input("Enter department (PGDM/BTech): ").upper()
        if department not in departments:
            departments[department] = Department(department)

        student = Student(name, department)
        departments[department].admit_student(student)

    return departments

# Function to display student count in each department
def display_student_count(departments):
    for department_name, department in departments.items():
        student_count = department.get_student_count()
        print(f"Number of students in {department_name} department: {student_count}")

# Main program
if __name__ == "__main__":
    admitted_departments = admit_students()
    display_student_count(admitted_departments)
