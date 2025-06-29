import math

# Get input from user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Show calculations
print(f"\nCalculations:")
print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Formula: distance = √[(x₂-x₁)² + (y₂-y₁)²]")

# Calculate steps
dx = x2 - x1
dy = y2 - y1
distance = math.sqrt(dx**2 + dy**2)

print(f"Step 1: x₂-x₁ = {x2} - {x1} = {dx}")
print(f"Step 2: y₂-y₁ = {y2} - {y1} = {dy}")
print(f"Step 3: √[({dx})² + ({dy})²]")
print(f"Step 4: √[{dx**2} + {dy**2}]")
print(f"Step 5: √{dx**2 + dy**2}")

print(f"\nFinal result: {distance:.2f} units")
