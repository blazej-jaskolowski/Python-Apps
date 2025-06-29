# Get input from user
number = input("Enter a number: ")
width = int(input("Enter desired width: "))

print("\nAdding leading zeros...")
print(f"Original number: {number}")
print(f"Desired width: {width}")

# Different methods
result1 = number.zfill(width)
result2 = str(number).rjust(width, '0')
result3 = f"{int(number):0{width}d}"

print("\nDifferent methods:")
print(f"Method 1 (zfill): {result1}")
print(f"Method 2 (rjust): {result2}")
print(f"Method 3 (f-string): {result3}")
