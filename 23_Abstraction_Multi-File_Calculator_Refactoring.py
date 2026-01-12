def add_numbers(n1, n2):
    return n1 + n2

def subtract_numbers(n1, n2):
    return n1 - n2

def multiply_number(n1, n2):
    return n1 * n2

from utils.calculations import add_numbers, multiply_number 

print("🧩 Modular Calculator App 🧩")

num_a = 10
num_b = 5

sum_result = add_numbers(num_a, num_b)
product_result = multiply_number(num_a, num_b)

print(f"{num_a} + {num_b} = {sum_result}")
print(f"{num_a} * {num_b} = {product_result}")

try:
    subtract_numbers(num_a, num_b)
except NameError as e:
    print(f"\nCaught an expected error: {e}")
    print("This shows 'subtract_numbers' wasn't imported into this file's scope!")