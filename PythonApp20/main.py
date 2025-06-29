# Get input from user
text = input("Enter a string: ")
copies = int(input("Enter number of copies (non-negative): "))

# Validate input
if copies < 0:
    print("\nError: Number of copies must be non-negative")
    exit()

# Show calculations
print(f"\nCalculations:")
print(f"Original string: '{text}'")
print(f"Number of copies: {copies}")

# Create result
result = text * copies

print(f"\nFinal result: '{result}'")
