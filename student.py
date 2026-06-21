students = []

# Add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = [name, roll, marks]
    students.append(student)

    print("Student added successfully!\n")


# View all students
def view_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for s in students:
            print("Name:", s[0], "Roll No:", s[1], "Marks:", s[2])
        print()


# Search student
def search_student():
    roll = input("Enter roll number to search: ")
    found = False

    for s in students:
        if s[1] == roll:
            print("Student Found:")
            print("Name:", s[0], "Marks:", s[2])
            found = True

    if not found:
        print("Student not found.\n")


# Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s[1] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


# Main menu
while True:
    print("----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")
