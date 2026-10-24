students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    grade = input("Enter grade: ")

    students[name] = {
        "Marks": marks,
        "Grade": grade
    }

print("\nAll Student Details:")

for name, details in students.items():
    print("Name:", name)
    print("Marks:", details["Marks"])
    print("Grade:", details["Grade"])
    print()

highest_student = max(
    students, key=lambda name: students[name]["Marks"]
)

print("Student with Highest Marks:", highest_student)
print("Highest Marks:", students[highest_student]["Marks"])