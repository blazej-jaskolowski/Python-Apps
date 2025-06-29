# Get input from user
number = int(input("Enter an integer: "))

print("\nChecking if number fits in 64 bits...")
print(f"Number: {number}")

# Check if fits in 64 bits
min_64bit = -2**63
max_64bit = 2**63 - 1

fits_64bit = min_64bit <= number <= max_64bit

print("\nLimits:")
print(f"Minimum 64-bit value: {min_64bit}")
print(f"Maximum 64-bit value: {max_64bit}")

print(f"\nFinal result: Number {'' if fits_64bit else 'does not '}fits in 64 bits")
