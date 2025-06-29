# Get input from user
value = input("Enter a value: ")

print("\nObject Analysis:")

# Try converting to different types
try:
    int_val = int(value)
    print("\nAs Integer:")
    print(f"Identity (id): {id(int_val)}")
    print(f"Type: {type(int_val)}")
    print(f"Value: {int_val}")
except ValueError:
    try:
        float_val = float(value)
        print("\nAs Float:")
        print(f"Identity (id): {id(float_val)}")
        print(f"Type: {type(float_val)}")
        print(f"Value: {float_val}")
    except ValueError:
        print("\nAs String:")
        print(f"Identity (id): {id(value)}")
        print(f"Type: {type(value)}")
        print(f"Value: {value}")
