print("🔢 Square of Numbers Generator 🔢")

original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"\nOriginal numbers: {original_numbers}")

squares_loop = []
for num in original_numbers:
    squares_loop.append(num ** 2)

print(f"Generated via loop: {squares_loop}")

squares_comprehension = [num ** 2 for num in original_numbers]

print(f"Generated via comprehension: {squares_comprehension}")


even_squares = [num ** 2 for num in original_numbers if num % 2 == 0]

print(f"\nSquares of even numbers only: {even_squares}")
