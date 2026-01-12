students = [
    {'name': 'Bob', 'age': 18, 'grade': 'B'},
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Charlie', 'age': 19, 'grade': 'C'},
    {'name': 'David', 'age': 18, 'grade': 'A'},
]

print("🧑‍🎓 Original List of Students (Unsorted):")
for s in students:
    print(s)

students_by_age = sorted(students, key=lambda x: x['age'])

print("\n🔢 Sorted List by Age:")
for s in students_by_age:
    print(s)

students_by_name = sorted(students, key=lambda student_dict: student_dict['name'])

print("\n nam Sorted List by Name:")
for s in students_by_name:
    print(s)
