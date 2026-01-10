todo_list = []
running = True
print("Simple To-Do List App")
while running:
    print("-----Menu-----")
    print("1. Display the To-Do List")
    print("2. Add Tasks in the To-Do List")
    print("3. Exit")
    choice = input("Enter your choice (1,2,3) : ")
    if choice == "1":
        if not todo_list:
            print("Your To-Do list is empty")
        else:
            print("-----Your To-Do List-----")
            for index in range(len(todo_list)):
                todo_index = index + 1
                todo_description = todo_list[index]
                print(f"{todo_index}. {todo_description}")
            print("-------------------------")
    elif choice == "2":
        new_task = input("Enter the task you want to add :\n")
        todo_list.append(new_task)
        print(f"The added task is {new_task}")
    elif choice == "3":
        print("Goodbye")
        running = False
    else:
        print("invalid choise choose between 1,2 and 3")