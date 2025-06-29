print("Enter a number:")

try:
    number = float(input())
    print(f"\nSuccessfully converted to number: {number}")
    
    # Additional information
    if number.is_integer():
        print("This is an integer")
    else:
        print("This is a floating-point number")
except ValueError:
    print("\nError: This is not a valid number!")
    print("Examples of valid numbers: 42, -17, 3.14, -0.001")
