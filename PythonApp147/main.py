# Get input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nChecking divisibility...")
print(f"Numbers: {num1}, {num2}")

# Check if second number is zero
if num2 == 0:
    print("\nError: Cannot divide by zero!")
else:
    # Check divisibility
    is_divisible = num1 % num2 == 0
    
    print("\nCalculation:")
    print(f"{num1} divided by {num2} = {num1/num2}")
    print(f"Remainder: {num1 % num2}")
    
    print(f"\nFinal result: {num1} is{' ' if is_divisible else ' not '}divisible by {num2}")
