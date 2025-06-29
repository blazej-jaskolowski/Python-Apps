# Get input from user
test_string = input("Enter a string to test: ")

print("\nTesting string:", test_string)

# Different numeric tests
is_digit = test_string.isdigit()
is_decimal = test_string.isdecimal()
is_numeric = test_string.isnumeric()

print("\nTest results:")
print(f"isdigit(): {is_digit} (only digits 0-9)")
print(f"isdecimal(): {is_decimal} (decimal characters)")
print(f"isnumeric(): {is_numeric} (any numeric characters)")

# Try converting
try:
    float_val = float(test_string)
    print(f"\nCan be converted to float: {float_val}")
except ValueError:
    print("\nCannot be converted to float")
