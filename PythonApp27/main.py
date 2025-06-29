# Get input from user
elements = input("Enter elements separated by spaces: ").split()

# Show calculations
print(f"\nCalculations:")
print(f"List elements: {elements}")
print(f"Joining all elements...")

# Concatenate elements
result = ''.join(elements)

print(f"\nFinal result: '{result}'")
