# Get input from user
x = float(input("Enter value for x: "))
y = float(input("Enter value for y: "))

# Show calculations
print(f"\nCalculations:")
print(f"Formula: (x + y)² = (x + y)(x + y)")
print(f"Values: x = {x}, y = {y}")
print(f"Step 1: x + y = {x} + {y} = {x+y}")
print(f"Step 2: ({x+y})² = {x+y} * {x+y}")

# Calculate result
result = (x + y) * (x + y)

print(f"\nFinal result: ({x} + {y})² = {result}")
