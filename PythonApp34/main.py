# Get input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Show calculations
print(f"\nCalculations:")
print(f"Numbers: {a}, {b}")
print(f"Sum = {a} + {b} = {a+b}")

# Check sum condition
sum_result = a + b
if 15 <= sum_result <= 20:
    print("Sum is between 15 and 20, returning 20")
    result = 20
else:
    result = sum_result

print(f"\nFinal result: {result}")
