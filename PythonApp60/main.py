import math

# Get input from user
a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))

print("\nCalculations:")
print(f"Finding hypotenuse of right triangle with sides {a} and {b}")
print("Using Pythagorean theorem: c² = a² + b²")

# Calculate steps
a_squared = a ** 2
b_squared = b ** 2
c = math.sqrt(a_squared + b_squared)

print(f"\nStep 1: Calculate a² = {a}² = {a_squared}")
print(f"Step 2: Calculate b² = {b}² = {b_squared}")
print(f"Step 3: Add a² + b² = {a_squared} + {b_squared} = {a_squared + b_squared}")
print(f"Step 4: Take square root = √{a_squared + b_squared} = {c}")

print(f"\nFinal result: Hypotenuse = {c:.2f}")
