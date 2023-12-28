from datetime import datetime, timedelta

class Employee:
    def __init__(self):
        self.employee_id = int(input("Enter your employee id: "))
        self.project_id = int(input("Enter your project id: "))
        entry_time_str = input("Enter the time you have entered (hh:mm:ss): ")
        self.entry_time = datetime.strptime(entry_time_str, "%H:%M:%S")
        self.exit_time = None
        self.hours_worked = 0

    def logging_hours(self):
        exit_time_str = input("Enter the time you have exited (hh:mm:ss): ")
        self.exit_time = datetime.strptime(exit_time_str, "%H:%M:%S")
        self.hours_worked = (self.exit_time - self.entry_time).total_seconds() / 3600

class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.time_entries = []

    def log_hours(self, employee_id, entry_time, exit_time):
        entry = {'employee_id': employee_id, 'entry_time': entry_time, 'exit_time': exit_time}
        self.time_entries.append(entry)

class TimeTrackingSystem:
    def __init__(self):
        self.employees = []
        self.projects = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_project(self, project):
        self.projects.append(project)

    def generate_timesheet(self, employee, start_date, end_date):
        timesheet = []
        for project in self.projects:
            project_entries = [entry for entry in project.time_entries
                               if start_date <= entry['entry_time'] <= end_date
                               and entry['employee_id'] == employee.employee_id]
            timesheet.extend(project_entries)
        return timesheet

    def calculate_overtime(self, employee, start_date, end_date, max_hours=40):
        total_hours = sum((entry['exit_time'] - entry['entry_time']).total_seconds() / 3600
                          for entry in self.generate_timesheet(employee, start_date, end_date))
        overtime_hours = max(0, total_hours - max_hours)
        return overtime_hours

# Example usage:
if __name__ == "__main__":
    emp = Employee()
    emp.logging_hours()

    project = Project(emp.project_id, "Sample Project")
    project.log_hours(emp.employee_id, emp.entry_time, emp.exit_time)

    time_tracking_system = TimeTrackingSystem()
    time_tracking_system.add_employee(emp)
    time_tracking_system.add_project(project)

    start_date = datetime.strptime(input("Enter start date for timesheet (YYYY-MM-DD): "), "%Y-%m-%d")
    end_date = datetime.strptime(input("Enter end date for timesheet (YYYY-MM-DD): "), "%Y-%m-%d")

    timesheet = time_tracking_system.generate_timesheet(emp, start_date, end_date)
    overtime = time_tracking_system.calculate_overtime(emp, start_date, end_date)

    print("\nEmployee Credentials:")
    print(f"Employee ID: {emp.employee_id}")
    print(f"Project ID: {emp.project_id}")
    print(f"Entry Time: {emp.entry_time.strftime('%H:%M:%S')}")
    print(f"Exit Time: {emp.exit_time.strftime('%H:%M:%S')}")
    print(f"Hours Worked: {emp.hours_worked} hours")

    print("\nTimesheet:")
    for entry in timesheet:
        print(f"Employee ID: {entry['employee_id']}, Entry Time: {entry['entry_time'].strftime('%H:%M:%S')}, Exit Time: {entry['exit_time'].strftime('%H:%M:%S')}")

    print(f"\nOvertime for Employee {emp.employee_id}: {overtime} hours")
