# Get input from user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Show calculations
print(f"\nCalculations:")
print(f"Base = {base}")
print(f"Height = {height}")
print(f"Area formula = (base * height) / 2")
print(f"           = ({base} * {height}) / 2")

# Calculate area
area = (base * height) / 2

print(f"\nFinal result: Area = {area:.2f} square units")
