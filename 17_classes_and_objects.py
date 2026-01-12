class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_info(self):
        print(f"Name: {self.name} | Marks: {self.marks}/100")
        if self.marks >= 60:
            print(f"Status: Passed")
        else:
            print(f"Status: Failed")

student1 = Student("Alice", 85)
student2 = Student("Bob", 45)

print("🎓 Student Class & Object Viewer 🎓")

print("\n--- Displaying Student 1 Info (Alice) ---")
student1.display_info()

print("\n--- Displaying Student 2 Info (Bob) ---")
student2.display_info()

student2.marks = 65
print("\n--- Bob's marks updated to 65. Re-displaying Bob's info ---")
student2.display_info()
