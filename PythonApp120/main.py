# Get input from user
text = input("Enter a string: ")
limit = int(input("Enter length limit: "))

print("\nLimiting string length...")
print(f"Original string: '{text}'")
print(f"Length limit: {limit}")

# Different methods
method1 = text[:limit]
method2 = text.ljust(limit)[:limit]
method3 = f"{text:.{limit}}"

print("\nDifferent methods:")
print(f"Method 1 (slicing): '{method1}'")
print(f"Method 2 (ljust): '{method2}'")
print(f"Method 3 (format): '{method3}'")
