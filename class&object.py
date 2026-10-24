class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


s1 = Student("Karthik", 101, 89)
s2 = Student("Prema", 102, 95)

s1.display_details()
print()
s2.display_details()