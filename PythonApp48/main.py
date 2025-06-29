# Get input from user
value_str = input("Enter a number: ")

print("\nAttempting to parse input...")
print(f"Input string: '{value_str}'")

# Try parsing as integer first, then float
try:
    # Try integer
    int_value = int(value_str)
    print(f"Successfully parsed as integer: {int_value}")
    print(f"Type: {type(int_value)}")
except ValueError:
    try:
        # Try float
        float_value = float(value_str)
        print(f"Successfully parsed as float: {float_value}")
        print(f"Type: {type(float_value)}")
    except ValueError:
        print("Could not parse input as either integer or float")
