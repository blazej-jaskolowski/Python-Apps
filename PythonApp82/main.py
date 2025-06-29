# Get input from user
print("Enter items separated by spaces:")
items = input().split()

# Convert to different containers
numbers = [float(x) for x in items]
tuple_container = tuple(numbers)
list_container = list(numbers)
set_container = set(numbers)
dict_container = {i: num for i, num in enumerate(numbers)}

print("\nCalculations:")
print(f"Tuple: {tuple_container}")
print(f"List: {list_container}")
print(f"Set: {set_container}")
print(f"Dictionary: {dict_container}")

# Calculate sums
tuple_sum = sum(tuple_container)
list_sum = sum(list_container)
set_sum = sum(set_container)
dict_sum = sum(dict_container.values())

print("\nSums:")
print(f"Tuple sum: {tuple_sum}")
print(f"List sum: {list_sum}")
print(f"Set sum: {set_sum}")
print(f"Dictionary sum: {dict_sum}")
