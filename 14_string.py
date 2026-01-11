def validate_username(username):
    MIN_LENGTH = 5
    MAX_LENGTH = 15
    clean_username = username.strip() 
    if len(clean_username) < MIN_LENGTH or len(clean_username) > MAX_LENGTH:
        print(f"Failed Validation: Must be between {MIN_LENGTH} and {MAX_LENGTH} characters long.")
        return False
    if not clean_username.isalnum():
        print(f"Failed Validation: Can only contain letters (a-z) and numbers (0-9).")
        return False
    print(f"Success! Username '{clean_username}' is valid.")
    return True
running = True
print("Username Validator")
while running:
    print("\n--- Menu ---")
    print("1. Validate a new username")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == '1':
        print("\nRules: 5-15 characters, letters and numbers only.")
        raw_username_input = input("Enter username to validate: ")
        standardized_username = raw_username_input.lower()
        print(f"\nStandardizing input to lowercase: '{standardized_username}'")
        is_valid = validate_username(standardized_username)
        if is_valid:
            print(f"You can register with this username: '{standardized_username}'")
    elif choice == '2':
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please enter 1 or 2.")