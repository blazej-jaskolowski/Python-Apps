import math

# Get input from user
radius = float(input("Enter the radius of the sphere: "))

# Show calculations
print(f"\nCalculations:")
print(f"Radius = {radius}")
print(f"Volume formula = (4/3) * pi * radius^3")
print(f"           = (4/3) * {math.pi:.4f} * {radius}^3")
print(f"           = (4/3) * {math.pi:.4f} * {radius**3}")

# Calculate final result
volume = (4/3) * math.pi * radius**3

print(f"\nFinal result: {volume:.4f} cubic units")
