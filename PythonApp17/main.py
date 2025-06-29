# Get input from user
number = float(input("Enter a number: "))

# Show calculations
print(f"\nCalculations:")
print(f"Number = {number}")
print(f"Distance from 1000 = |1000 - {number}| = {abs(1000 - number)}")
print(f"Distance from 2000 = |2000 - {number}| = {abs(2000 - number)}")

# Check conditions
near_1000 = abs(1000 - number) <= 100
near_2000 = abs(2000 - number) <= 100

print(f"\nResults:")
print(f"Within 100 of 1000: {near_1000}")
print(f"Within 100 of 2000: {near_2000}")
print(f"\nFinal result: {near_1000 or near_2000}")
