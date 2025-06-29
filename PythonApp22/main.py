# Get input from user
input_string = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_string.split()]

# Show calculations
print(f"\nCalculations:")
print(f"List: {numbers}")
print(f"Counting occurrences of 4...")

# Count number 4
count = numbers.count(4)
print(f"Number 4 appears {count} time(s) in positions:", end=" ")
positions = [i for i, x in enumerate(numbers) if x == 4]
print(positions if positions else "none")

print(f"\nFinal result: {count}")
