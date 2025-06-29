# Get input from user
text = input("Enter a string: ")

print("\nChecking for lowercase letters...")
print(f"String: '{text}'")

# Different methods
has_lower1 = any(c.islower() for c in text)
has_lower2 = not text.upper() == text

print("\nLowercase letters found:")
print("Method 1 (using any()): ", has_lower1)
print("Method 2 (compare with upper): ", has_lower2)

if has_lower1:
    print("\nLowercase letters in string:")
    print([c for c in text if c.islower()])