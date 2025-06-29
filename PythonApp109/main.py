# Get input from user
try:
    number = float(input("Enter a number: "))
    
    print("\nChecking number...")
    print(f"Number: {number}")
    
    if number > 0:
        result = "positive"
    elif number < 0:
        result = "negative"
    else:
        result = "zero"
    
    print(f"\nFinal result: The number is {result}")
except ValueError:
    print("\nError: Please enter a valid number")
