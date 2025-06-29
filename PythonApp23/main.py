# Get input from user
text = input("Enter a string: ")
copies = int(input("Enter number of copies (non-negative): "))

# Show calculations
print(f"\nCalculations:")
print(f"Original string: '{text}'")
print(f"Length of string: {len(text)}")

if len(text) < 2:
    result = text * copies
    print(f"String length less than 2, copying entire string")
else:
    result = text[:2] * copies
    print(f"Taking first 2 characters: '{text[:2]}'")

print(f"Making {copies} copies")

print(f"\nFinal result: '{result}'")
