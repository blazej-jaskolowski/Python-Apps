# Get input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("\nCalculations:")
print(f"Sorting numbers: {a}, {b}, {c}")

# Sort using min and max functions
minimum = min(min(a, b), c)
maximum = max(max(a, b), c)
middle = (a + b + c) - minimum - maximum

print("\nStep by step:")
print(f"Minimum: {minimum}")
print(f"Middle: {middle}")
print(f"Maximum: {maximum}")

print(f"\nFinal result: {minimum}, {middle}, {maximum}")
