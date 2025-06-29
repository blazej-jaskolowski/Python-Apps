# Get input from user
print("Enter three values:")
a = input("Value 1: ")
b = input("Value 2: ")
c = input("Value 3: ")

print("\nChecking values...")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Check equality
all_equal = a == b == c
some_equal = a == b or b == c or a == c

print("\nResults:")
print(f"All values are equal: {all_equal}")
print(f"Some values are equal: {some_equal}")

# Show detailed comparisons
print("\nDetailed comparisons:")
print(f"a == b: {a == b}")
print(f"b == c: {b == c}")
print(f"a == c: {a == c}")
