class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Salary:", self.salary)


e1 = Employee(101, "Keerthi", 25000)
e2 = Employee(102, "Karthik", 30000)
e3 = Employee(103, "Anjali", 35000)

e1.display_details()
print()
e2.display_details()
print()
e3.display_details()