# Get input from user
x = int(input("Enter an integer: "))
width = int(input("Enter desired width of binary number: "))

print("\nConverting to binary...")
print(f"Number: {x}")
print(f"Width: {width}")

# Different methods
binary1 = format(x, f'0{width}b')
binary2 = bin(x)[2:].zfill(width)
binary3 = f"{x:0{width}b}"

print("\nDifferent methods:")
print(f"Method 1 (format): {binary1}")
print(f"Method 2 (zfill): {binary2}")
print(f"Method 3 (f-string): {binary3}")

print("\nBinary representation explanation:")
print(f"Decimal: {x}")
print(f"Binary: {binary1}")
print("Position values:", end=" ")
for i, digit in enumerate(binary1[::-1]):
    if digit == '1':
        print(f"2^{i}", end=" + ")
print("\b\b ")
