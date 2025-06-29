# Get input from user
n = int(input("Enter a positive integer: "))

print("\nCalculating sum of cubes...")
print(f"Finding sum of cubes for numbers smaller than {n}")

# Calculate sum of cubes
sum_cubes = 0
print("\nCalculations:")
for i in range(1, n):
    cube = i ** 3
    sum_cubes += cube
    print(f"{i}^3 = {cube}")

print(f"\nFinal result: Sum of cubes = {sum_cubes}")
