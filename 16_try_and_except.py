def safe_divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")
        return None
    except TypeError:
        print("\nError: Invalid input type. Please use numbers.")
        return None
running = True
print("Safe Calculator")

while running:
    print("\n--- Safe Division Menu ---")
    print("1. Perform a safe division")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        try:
            n1 = float(input("Enter the numerator (top number): "))
            n2 = float(input("Enter the denominator (bottom number): "))
            answer = safe_divide(n1, n2)

            if answer is not None:
                print(f"\nResult: {n1} / {n2} = {answer}")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")
        
    elif choice == '2':
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please enter 1 or 2.")
