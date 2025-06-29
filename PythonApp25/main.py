# Get input from user
search_value = int(input("Enter value to search for: "))
input_string = input("Enter group of numbers separated by spaces: ")
numbers = [int(x) for x in input_string.split()]

# Show calculations
print(f"\nCalculations:")
print(f"Search value: {search_value}")
print(f"Group of numbers: {numbers}")
print(f"Checking if {search_value} exists in the group...")

# Check if value exists
result = search_value in numbers

print(f"\nFinal result: {result}")
