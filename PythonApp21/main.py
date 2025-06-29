# Get input from user
number = int(input("Enter an integer: "))

# Show calculations
print(f"\nCalculations:")
print(f"Number = {number}")
print(f"Remainder when divided by 2 = {number} % 2 = {number % 2}")

# Determine if even or odd
if number % 2 == 0:
    result = "even"
else:
    result = "odd"

print(f"\nFinal result: {number} is an {result} number")
