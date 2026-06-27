class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


students = []

# ---------------- LOAD DATA ----------------
def load_data():
    try:
        file = open("students.txt", "r")
        for line in file:
            data = line.strip().split(",")
            name = data[0]
            age = int(data[1])
            marks = int(data[2])
            students.append(Student(name, age, marks))
        file.close()
    except:
        pass


# ---------------- SAVE DATA ----------------
def save_data():
    file = open("students.txt", "w")
    for s in students:
        file.write(s.name + "," + str(s.age) + "," + str(s.marks) + "\n")
    file.close()


# ---------------- ANALYTICS ----------------
def show_topper():
    if len(students) == 0:
        print("No students found!")
        return

    topper = students[0]
    for s in students:
        if s.marks > topper.marks:
            topper = s

    print("\n🏆 TOPPER STUDENT")
    topper.display()


def show_average():
    if len(students) == 0:
        print("No students found!")
        return

    total = 0
    for s in students:
        total += s.marks

    print("\n📊 AVERAGE MARKS:", total / len(students))


def show_pass_fail():
    pass_count = 0
    fail_count = 0

    for s in students:
        if s.marks >= 40:
            pass_count += 1
        else:
            fail_count += 1

    print("\n✅ PASS:", pass_count)
    print("❌ FAIL:", fail_count)


def sort_students():
    sorted_list = sorted(students, key=lambda x: x.marks, reverse=True)

    print("\n📈 SORTED STUDENTS")
    for s in sorted_list:
        s.display()
        print("-------------------")


# Load existing data
load_data()


# ---------------- MAIN MENU ----------------
while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Show Topper")
    print("7. Show Average")
    print("8. Pass/Fail Report")
    print("9. Sort Students")
    print("10. Exit")

    choice = input("Enter your choice: ")

    # ADD
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))

        students.append(Student(name, age, marks))
        save_data()
        print("Student added successfully ✅")

    # VIEW
    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            for s in students:
                s.display()
                print("-------------------")

    # SEARCH
    elif choice == "3":
        name = input("Enter name to search: ")
        found = False

        for s in students:
            if s.name.lower() == name.lower():
                print("\nStudent Found ✅")
                s.display()
                found = True
                break

        if not found:
            print("Not found ❌")

    # DELETE
    elif choice == "4":
        name = input("Enter name to delete: ")
        found = False

        for s in students:
            if s.name.lower() == name.lower():
                students.remove(s)
                save_data()
                print("Deleted successfully ✅")
                found = True
                break

        if not found:
            print("Not found ❌")

    # UPDATE
    elif choice == "5":
        name = input("Enter name to update: ")
        found = False

        for s in students:
            if s.name.lower() == name.lower():
                print("Enter new details:")

                s.name = input("Enter new name: ")
                s.age = int(input("Enter new age: "))
                s.marks = int(input("Enter new marks: "))

                save_data()
                print("Updated successfully ✅")
                found = True
                break

        if not found:
            print("Not found ❌")

    # TOPPER
    elif choice == "6":
        show_topper()

    # AVERAGE
    elif choice == "7":
        show_average()

    # PASS/FAIL
    elif choice == "8":
        show_pass_fail()

    # SORT
    elif choice == "9":
        sort_students()

    # EXIT
    elif choice == "10":
        save_data()
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice!")