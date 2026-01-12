def log_file_generator(filename):

    print(f"--- Opening file: {filename} ---")
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip() 
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

with open("app_logs.txt", "w") as f:
    f.write("Log Entry 1\n")
    f.write("Log Entry 2: Error\n")
    f.write("Log Entry 3\n")
    f.write("Log Entry 4: Success\n")

# Main execution
print("Log File Processor (using a Generator)")

log_processor = log_file_generator("app_logs.txt")

for entry in log_processor:
    print(f"Processing line: {entry}")
    if "Error" in entry:
        print("🚨 Alert: Found an error log!")

print("\nFinished processing all logs.")