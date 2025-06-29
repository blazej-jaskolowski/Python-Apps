# Get input from user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print("\nCalculations:")
print(f"Finding midpoint between ({x1}, {y1}) and ({x2}, {y2})")
print("Formula: midpoint = ((x1 + x2)/2, (y1 + y2)/2)")

# Calculate midpoint
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

print("\nStep by step:")
print(f"x_midpoint = ({x1} + {x2})/2 = {mid_x}")
print(f"y_midpoint = ({y1} + {y2})/2 = {mid_y}")

print(f"\nFinal result: Midpoint = ({mid_x}, {mid_y})")
