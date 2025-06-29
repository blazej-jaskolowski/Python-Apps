print("Enter two integers separated by space:")
try:
    x, y = map(int, input().split())
    
    print("\nInput received:")
    print(f"First number: {x}")
    print(f"Second number: {y}")
    
    print("\nOperations with these numbers:")
    print(f"Sum: {x + y}")
    print(f"Product: {x * y}")
except ValueError:
    print("\nError: Please enter exactly two integers separated by space")
