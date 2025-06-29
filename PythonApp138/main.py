# Get input from user
value = input("Enter True or False: ").lower()

print("\nConverting to boolean...")
# Convert string to boolean
bool_value = value in ['true', '1', 'yes', 'y']

# Convert to integer
int_value = int(bool_value)

print("\nConversions:")
print(f"Input string: {value}")
print(f"Boolean value: {bool_value}")
print(f"Integer value: {int_value}")
