# Get input from user
text = input("Enter a string: ")

# Show calculations
print(f"\nCalculations:")
print(f"Original string: '{text}'")
print(f"Checking if string starts with 'Is'...")

# Process string
if text.lower().startswith('is'):
    result = text
    print("String already starts with 'Is' - keeping unchanged")
else:
    result = 'Is ' + text
    print("Adding 'Is' to the front of string")

print(f"\nFinal result: '{result}'")
