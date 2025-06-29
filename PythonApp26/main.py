# Get input from user
input_string = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_string.split()]

# Show calculations
print(f"\nCalculations:")
print(f"Numbers: {numbers}")
print(f"\nHistogram:")

# Create and display histogram
for num in numbers:
    print(f"{num:2d} | {'*' * num}")

print("\nFinal result shown above")
