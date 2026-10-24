# Store 5 student names in the file
with open("students.txt", "w") as file:
    for i in range(5):
        name = input("Enter student name: ")
        file.write(name + "\n")

# Read and display student names
with open("students.txt", "r") as file:
    names = file.readlines()

print("\nStudent Names:")

for name in names:
    print(name.strip())

print("Total Number of Students:", len(names))