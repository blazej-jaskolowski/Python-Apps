# Get input from user
numbers = input("Enter decimal numbers separated by spaces: ").split()
numbers = [int(x) for x in numbers]

print("\nConverting to hexadecimal...")

# Different methods for each number
for num in numbers:
    print(f"\nNumber: {num}")
    
    # Method 1: Using hex()
    hex1 = hex(num)[2:].zfill(2)
    
    # Method 2: Using format
    hex2 = format(num, '02x')
    
    # Method 3: Using f-string
    hex3 = f"{num:02x}"
    
    print("Different methods:")
    print(f"Method 1 (hex): {hex1}")
    print(f"Method 2 (format): {hex2}")
    print(f"Method 3 (f-string): {hex3}")

print("\nNote: All results are shown in lowercase. Use .upper() for uppercase.")
