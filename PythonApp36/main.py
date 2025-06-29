# Get input from user
a = input("Enter first value: ")
b = input("Enter second value: ")

# Show calculations
print(f"\nCalculations:")
print(f"Checking if both inputs are integers...")

try:
    num1 = int(a)
    num2 = int(b)
    result = num1 + num2
    print(f"Both values are integers")
    print(f"Sum = {num1} + {num2}")
    print(f"\nFinal result: {result}")
except ValueError:
    print("\nFinal result: Cannot add - both values must be integers")
