password = "ShaikKhajaPasha"
MAX_attempts = 3
attempts = 0
print("Simple Password Enter system")
while True:
    Guess = input("\nEnter the Correct password to enter : ")
    attempts += 1
    if (Guess == password):
        print("\n Correct! Entered the system successfully")
        break
    elif(attempts >= MAX_attempts):
        print("\nMaximum attempts are used. Account Locked")
        break
    else:
        print("\nPassword is incorrect Please Try again")
        continue