NOTES_FILE = "my_notes.txt"

def write_notes_to_file(note_content):
    try:
        with open(NOTES_FILE, 'a') as file:
            file.write(note_content + "\n---\n")
        print(f"Note saved successfully to {NOTES_FILE}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_notes_from_file():
    try:
        with open(NOTES_FILE, 'r') as file:
            content = file.read()
            if content:
                print("\n--- Your Saved Notes ---")
                print(content, end="")
                print("--------------------------")
            else:
                print(f"\n{NOTES_FILE} is currently empty.")
    except FileNotFoundError:
        print(f"\n{NOTES_FILE} not found. No notes saved yet.")
    except IOError as e:
        print(f"Error reading file: {e}")
running = True
print("Notes Saver App")
while running:
    print("\n--- Menu ---")
    print("1. Write a new note")
    print("2. Read all saved notes")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    if choice == '1':
        print("\nEnter your note below. Press Enter when finished.")
        new_note = input("Note: ")
        if new_note.strip():
            write_notes_to_file(new_note)
        else:
            print("Note cannot be empty.")
    elif choice == '2':
        read_notes_from_file()
    elif choice == '3':
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

