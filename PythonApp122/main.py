# Get number input
n = int(input("Enter a number: "))

# Get dictionary input (key and value)
key = input("Enter dictionary key: ")
value = int(input("Enter dictionary value: "))
d = {key: value}

print("\nOriginal values:")
print(f"n = {n}")
print(f"d = {d}")

# Empty variables
n = 0
d.clear()

print("\nAfter emptying:")
print(f"n = {n}")
print(f"d = {d}")
