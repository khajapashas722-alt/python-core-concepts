days_of_week = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
running = True
print("Days of the Week")
print(f"There are {len(days_of_week)} in the tuple")
while running:
    print("-----Menu-----")
    print("1. Chose the day using the number")
    print("2. Exit")
    choice = input("Enter your choise (1 or 2) : ")
    if choice == "1":
        day_sel_str = input("Enter the day you want the see : ")
        try:
            day_sel_int = int(day_sel_str)
            if 1<=day_sel_int<=7:
                selected_index  = day_sel_int - 1
                print(f"The selected day number is {day_sel_int} and the day is {days_of_week[selected_index]}")
            else:
                print("Enter a valid number between 1 and 7")
        except ValueError:
            print("Invalid Enter. Please enter a valid whole number")
    elif choice == "2":
        print("Goodbye")
        running = False
    else:
        print("Invalid input Enter a valid input")