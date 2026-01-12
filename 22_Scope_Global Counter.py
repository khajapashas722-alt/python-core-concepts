hit_counter = 0

def log_hit_and_increment():
    global hit_counter 

    hit_counter += 1
    print(f"--- Action logged --- Current global counter value: {hit_counter}")

print("Website Hit Logger (Scope Test)")
print(f"Initial counter value: {hit_counter}")

log_hit_and_increment() # Counter becomes 1
log_hit_and_increment() # Counter becomes 2
log_hit_and_increment() # Counter becomes 3

print(f"\nFinal global counter value accessible here too: {hit_counter}")
