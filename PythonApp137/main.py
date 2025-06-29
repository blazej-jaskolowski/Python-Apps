# Get input from user
key = input("Enter dictionary key: ")
value = input("Enter dictionary value: ")

# Create dictionary
my_dict = {key: value}
print("\nDictionary created:", my_dict)

# Extract key-value pair
k, v = my_dict.popitem()

print("\nExtracted values:")
print(f"Key: {k}")
print(f"Value: {v}")

print("\nDictionary after extraction:", my_dict)
