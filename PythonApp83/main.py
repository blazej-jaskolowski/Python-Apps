# Get input from user
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(x) for x in numbers]
test_value = float(input("Enter the test value: "))

print("\nCalculations:")
print(f"Numbers: {numbers}")
print(f"Testing if all numbers are greater than {test_value}")

# Check each number
all_greater = all(num > test_value for num in numbers)
print("\nChecking each number:")
for num in numbers:
    print(f"{num} > {test_value}: {num > test_value}")

print(f"\nFinal result: {all_greater}")
