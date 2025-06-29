# Get input from user
text = input("Enter a string: ")
char = input("Enter character to count: ")

print("\nCalculations:")
print(f"String: '{text}'")
print(f"Character to count: '{char}'")

# Count occurrences
count = text.count(char)

# Show positions
positions = [i for i, c in enumerate(text) if c == char]
print("\nCharacter positions:", positions if positions else "None")

print(f"\nFinal result: '{char}' appears {count} times")