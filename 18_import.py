import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Random Password Generator")

while True:
    try:
        user_length_input = input("Enter desired password length (min 8, max 30) or 'exit': ").strip().lower()

        if user_length_input == 'exit':
            print("Goodbye!")
            break

        length = int(user_length_input)

        if 8 <= length <= 30:
            new_password = generate_password(length)
            print(f"\nGenerated Password: **`{new_password}`**")
        else:
            print("Please enter a length between 8 and 30.")

    except ValueError:
        print("Invalid input. Please enter a whole number length.")
