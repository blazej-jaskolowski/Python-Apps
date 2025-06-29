# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Show calculations
print(f"\nCalculations:")
print(f"Numbers: {num1}, {num2}, {num3}")
print(f"Regular sum = {num1} + {num2} + {num3} = {num1 + num2 + num3}")

# Calculate result
sum_normal = num1 + num2 + num3
if num1 == num2 == num3:
    final_sum = sum_normal * 3
    print(f"Numbers are equal, tripling the sum: {sum_normal} * 3 = {final_sum}")
else:
    final_sum = sum_normal
    print("Numbers are not equal, keeping regular sum")

print(f"\nFinal result: {final_sum}")
