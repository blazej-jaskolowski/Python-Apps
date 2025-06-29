# Get input from user
a = input("Enter first value: ")
b = input("Enter second value: ")

print("\nBefore swap:")
print(f"a = {a}")
print(f"b = {b}")

# Method 1: Using temporary variable
print("\nMethod 1: Using temporary variable")
temp = a
a = b
b = temp

print("After swap:")
print(f"a = {a}")
print(f"b = {b}")

# Method 2: Without temporary variable
print("\nMethod 2: Without temporary variable")
a, b = b, a
print("After second swap (back to original):")
print(f"a = {a}")
print(f"b = {b}")
