# Get input from user
number = int(input("Enter an integer: "))

print("\nCalculations:")
print(f"Finding sum of digits in {number}")

# Convert to string to process digits
digits = str(abs(number))  # abs() handles negative numbers
digit_sum = sum(int(d) for d in digits)

print("\nStep by step:")
print(f"Digits: {' + '.join(digits)}")
print(f"Sum: {' + '.join(digits)} = {digit_sum}")

print(f"\nFinal result: {digit_sum}")
