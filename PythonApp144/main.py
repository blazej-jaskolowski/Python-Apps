# Get input from user
value = input("Enter a value: ")

print("\nAnalyzing value...")
print(f"Value: {value}")

# Try converting to integer
try:
    int_value = int(value)
    is_int = True
except ValueError:
    is_int = False

print("\nType checks:")
print(f"Is string: {isinstance(value, str)}")
print(f"Can be integer: {is_int}")

if is_int:
    print(f"\nValue is both a string and can be converted to integer: {int_value}")
else:
    print("\nValue is a string and cannot be converted to integer")
