# Get input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Show calculations
print(f"\nCalculations:")
print(f"Numbers: {a}, {b}, {c}")

# Check for equality and calculate
if a == b or b == c or a == c:
    result = 0
    print("Two numbers are equal, sum will be zero")
else:
    result = a + b + c
    print(f"Sum = {a} + {b} + {c}")

print(f"\nFinal result: {result}")
