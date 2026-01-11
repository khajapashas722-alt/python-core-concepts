def check_result(average_score):
    passing_marks = 60
    if average_score >= passing_marks:
        return "Passed"
    else:
        return "Failed"
running = True
print("Student Result Checker")
while running:
    print("\n---Menu---")
    print("1. check students passed their exam or not")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2) : ")
    if choice == '1':
        try:
            enter_score = input("Enter your score (eg: 72.0) : ").strip()
            score = float(enter_score)
            if 0<=score<=100:
                final_status = check_result(score)
                print(f"The Entered score is {score}")
                if final_status == "Passed":
                    print(f"Status: You {final_status} the exam")
                elif final_status == "Failed":
                    print(f"Status: You {final_status} the exam")
            else:
                print("Enter a number between 0 and 100")
        except ValueError:
            print("Invalid input please enter a number")
    elif choice == '2':
        print("Goodbye")
        running = False
    else:
        print("Enter a valid choise (1 or 2)")