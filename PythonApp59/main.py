# Get input from user
feet = float(input("Enter height (feet): "))
inches = float(input("Enter height (inches): "))

print("\nCalculations:")
print(f"Converting {feet} feet and {inches} inches to centimeters")

# Convert to centimeters
total_inches = (feet * 12) + inches
centimeters = total_inches * 2.54

print(f"\nStep 1: Convert feet to inches")
print(f"Inches from feet = {feet} * 12 = {feet * 12}")
print(f"Total inches = {feet * 12} + {inches} = {total_inches}")

print(f"\nStep 2: Convert inches to centimeters")
print(f"Centimeters = {total_inches} * 2.54 = {centimeters:.2f}")

print(f"\nFinal result: {centimeters:.2f} cm")
