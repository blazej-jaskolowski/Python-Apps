# Get input from user
str1 = input("Enter a string: ")
str2 = input("Enter the same string again: ")

print("\nComparing strings...")
print(f"String 1: '{str1}'")
print(f"String 2: '{str2}'")

# Compare values and memory locations
print("\nComparisons:")
print(f"Same value? {str1 == str2}")
print(f"Same object? {str1 is str2}")
print(f"\nMemory locations:")
print(f"String 1: {id(str1)}")
print(f"String 2: {id(str2)}")

# Create string literal for comparison
str3 = "test"
str4 = "test"
print("\nString literal comparison:")
print(f"str3 = 'test', str4 = 'test'")
print(f"Same object? {str3 is str4}")
