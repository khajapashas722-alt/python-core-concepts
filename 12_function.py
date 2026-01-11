def adding_number(n1,n2):
    result = n1+n2
    return result
def subtracting_number(n1,n2):
    result = n1-n2
    return result
def multiply_number(n1,n2):
    result = n1*n2
    return result
def divide_number(n1,n2):
    result = n1/n2
    return result

def modulo_division(n1,n2):
    result = n1%n2
    return result

running = True
print("Resuable calculator Function")
while running:
    print("\n---Menu---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo division")
    print("6. Exit")
    choice = input("Enter your choice (1,2,3,4, or 5) :")
    if choice in ['1','2','3','4','5']:
        try:
            number1 = int(input("Enter the first number"))
            number2 = int(input("Enter the second number"))
            if choice == '1':
                answer = adding_number(number1,number2)
                print(f"\n{number1} + {number2} = {answer}")
            elif choice == '2':
                answer = subtracting_number(number1,number2)
                print(f"\n{number1} - {number2} = {answer}")
            elif choice == '3':
                answer = multiply_number(number1,number2)
                print(f"\n{number1} * {number2} = {answer}")
            elif choice == '4':
                try:
                    answer = divide_number(number1,number2)
                except ZeroDivisionError:
                    print("Error: Numbers cannot be divided by zero.")
                    continue
            elif choice == '5':
                answer = modulo_division(number1,number2)
                print(f"\n{number1} % {number2} = {answer}")
        except ValueError:
            print("Invalid input enter a valid input (1,2,3,4, or 5)")
    elif choice == '6':
        print("Goodbye")
        running = False
    else:
        print("Invalid choice please enter a valid choice")
    