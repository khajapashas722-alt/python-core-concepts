student_marks = {}
running = True
print("Students Marks Dictionary")
while running:
    print("\n---Menu---")
    print("1.Add the student and their marks")
    print("2. View all students marks")
    print("3. View a specific student marks")
    print("4. Exit")
    choice = input("Enter your choice (1,2,3, or 4) : ")
    if choice == "1":
        name = input("Enter student name : ").strip().title()
        marks = input(f"Enter the marks of {name} : ").strip()
        if name and marks.isdigit():
            student_marks[name] = int(marks)
            print(f"Added/Updated the marks of {name}.")
        else:
            print("Invalid Entry. Name cannot be left empty and marks must be an integer")
    elif choice == "2":
        if not student_marks:
            print("No student details are found")
        else:
            print("\n---Student Marks---")
            for students,marks in student_marks.items():
                print(f"Student:{name} | Marks:{marks}")
            print("---------------------")
    elif choice == "3":
        student_name = input("Enter the name of the student : ").strip().title()
        if student_name in student_marks:
            marks= student_marks[student_name]
            print(f"\n{student_name}'s marks:{marks}")
        else:
            print(f"No student with the name {student_name} was found")
    elif choice == "4":
        print("Goodbye")
        running = False
    else:
        print("Invalid choice (1,2,3, or 4)")
