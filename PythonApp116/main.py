print("Demonstrating Unicode characters:")

# Method 1: Using Unicode code point
print("\nMethod 1: Using Unicode code points")
print(f"Copyright symbol: {chr(169)}")
print(f"Euro symbol: {chr(8364)}")
print(f"Degree symbol: {chr(176)}")

# Method 2: Using Unicode escape sequence
print("\nMethod 2: Using Unicode escape sequences")
print(f"Copyright symbol: \u00A9")
print(f"Euro symbol: \u20AC")
print(f"Degree symbol: \u00B0")

# Print a range of Unicode characters
print("\nPrinting Unicode range (32-47):")
for i in range(32, 48):
    print(f"Code {i}: {chr(i)}")
