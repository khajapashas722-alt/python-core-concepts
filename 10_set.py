unique_email = set()
running = True
print("Unique email collector")
print("Enter the email to collect and exit to stop the programm")
while running:
    enter_email = input("Enter the email").strip().lower()
    if enter_email == "exit":
        print("Goodbye")
        running = False
    elif enter_email in unique_email:
        print(f"{enter_email} already exists in the collection(duplicate detected)")
        continue
    elif not enter_email :
        print("You cant leave it to be null you must enter a email")
        continue
    else:
        unique_email.add(enter_email)
        print(f"Added new unique email: '{enter_email}'")
print("\n--Final Email Collection is--")
print(f"Total unique emails are {len(unique_email)}")
for email in sorted(unique_email):
    print(f"-{email}")