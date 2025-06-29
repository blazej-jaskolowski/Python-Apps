import math
from functools import reduce

# Get input from user
numbers = input("Enter integers separated by spaces: ").split()
numbers = [int(x) for x in numbers]

print("\nCalculating product...")
print(f"Numbers: {numbers}")

# Method 1: Using math.prod (Python 3.8+)
product1 = math.prod(numbers)
print("\nMethod 1: Using math.prod()")
print(f"Product: {product1}")

# Method 2: Using reduce with multiplication
product2 = reduce(lambda x, y: x * y, numbers)
print("\nMethod 2: Using reduce()")
print(f"Product: {product2}")

print(f"\nFinal result: {product1}")
