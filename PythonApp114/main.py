# Get input from user
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(x) for x in numbers]

print("\nFiltering positive numbers...")
print(f"Original numbers: {numbers}")

# Method 1: Using list comprehension
positive_numbers1 = [x for x in numbers if x > 0]
print("\nMethod 1 (List comprehension):")
print(f"Positive numbers: {positive_numbers1}")

# Method 2: Using filter and lambda
positive_numbers2 = list(filter(lambda x: x > 0, numbers))
print("\nMethod 2 (Filter with lambda):")
print(f"Positive numbers: {positive_numbers2}")

print("\nChecking each number:")
for num in numbers:
    print(f"{num} is{' ' if num > 0 else ' not '}positive")
