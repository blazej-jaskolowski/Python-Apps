# Get input from user
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(x) for x in numbers]

print("\nFinding numbers divisible by 15...")
print(f"Original numbers: {numbers}")

# Using lambda function
divisible_by_15 = list(filter(lambda x: x % 15 == 0, numbers))

print("\nChecking each number:")
for num in numbers:
    print(f"{num} is{' ' if num % 15 == 0 else ' not '}divisible by 15")

print(f"\nFinal result: {divisible_by_15}")
