# Get input from user
n = int(input("Enter a positive integer n: "))

print("\nCalculations:")
print(f"Finding sum of first {n} positive integers")

# Method 1: Using formula
formula_sum = (n * (n + 1)) // 2
print(f"\nMethod 1: Using formula n(n+1)/2")
print(f"= {n} * ({n} + 1) / 2")
print(f"= {n} * {n+1} / 2")
print(f"= {formula_sum}")

# Method 2: Using iteration
print(f"\nMethod 2: Using iteration")
iteration_sum = 0
for i in range(1, n + 1):
    iteration_sum += i
    print(f"Adding {i}: Sum = {iteration_sum}")

print(f"\nFinal result: {formula_sum}")
