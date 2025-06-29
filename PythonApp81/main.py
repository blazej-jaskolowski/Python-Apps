# Get number of strings from user
n = int(input("Enter number of strings to concatenate: "))

# Get the strings
strings = []
print("\nEnter the strings:")
for i in range(n):
    s = input(f"String {i+1}: ")
    strings.append(s)

print("\nCalculations:")
print("Strings to concatenate:", strings)

# Method 1: Using +
result1 = ""
print("\nMethod 1: Using + operator")
for s in strings:
    result1 += s
    print(f"Adding '{s}': {result1}")

# Method 2: Using join
result2 = "".join(strings)
print(f"\nMethod 2: Using join()")
print(f"''.join({strings})")

print(f"\nFinal result: '{result2}'")
 